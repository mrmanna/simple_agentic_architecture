#!/usr/bin/env python3
import json
import pika
import time

# RabbitMQ connection details
RABBITMQ_HOST = 'localhost'
RABBITMQ_USER = 'user'
RABBITMQ_PASS = 'password'
QUEUE_NAME = 'task_queue'

# Set up RabbitMQ connection

def handle_task(task_data):
    """
    A simple function that simulates 'handling' a task.
    """
    task_name = task_data.get("task_name", "NoName")
    task_description = task_data.get("task_description", "NoDescription")
    # For demo, we simply print the task. In a real scenario, this could trigger
    # any business logic, like sending emails, scheduling processes, etc.
    print(f"[WORKER] Handling Task => Name: '{task_name}', Description: '{task_description}'")
    time.sleep(1)  # simulate some processing time

def main():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME)

    def callback(ch, method, properties, body):
        task_data = json.loads(body.decode('utf-8'))
        handle_task(task_data)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=False)
    print("[WORKER] Waiting for tasks. Press CTRL+C to exit.")
    channel.start_consuming()

if __name__ == "__main__":
    main()
