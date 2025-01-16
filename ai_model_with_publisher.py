#!/usr/bin/env python3
import json
import pika
import logging
import ollama

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# RabbitMQ connection details
RABBITMQ_HOST = 'localhost'
RABBITMQ_USER = 'user'
RABBITMQ_PASS = 'password'
QUEUE_NAME = 'task_queue'

# Set up RabbitMQ connection
credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

# Define the function to publish a task to RabbitMQ
def publish_task(task_name: str, task_description: str) -> None:
    """
    Publishes a task to RabbitMQ.

    Args:
        task_name (str): Name or short title of the task.
        task_description (str): Details about the task.
    """
    task = {
        "task_name": task_name,
        "task_description": task_description
    }
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=json.dumps(task))
    logging.info(f"Task published => Name: '{task_name}', Description: '{task_description}'")

def main():
    # Initialize the Ollama client
    client = ollama.Client(host="http://localhost:11434")

    # Define the available functions
    available_functions = {
        'publish_task': publish_task,
    }

    # Send a chat request to the model with the function reference
    response = client.chat(
        model="llama3.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Create a task with name 'Example Task' and description 'This is an example task description.'"}
        ],
        tools=[publish_task],  # Pass the function reference directly
    )

    # Process the model's response and execute the function call if present
    for tool_call in response.message.tool_calls or []:
        function_to_call = available_functions.get(tool_call.function.name)
        if function_to_call:
            function_to_call(**tool_call.function.arguments)
        else:
            logging.warning(f"Function not found: {tool_call.function.name}")

if __name__ == "__main__":
    logging.info("Starting the task publisher...")
    main()
    logging.info("Task publisher finished.")
