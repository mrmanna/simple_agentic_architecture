# AI Agent

## Introduction

While talking with fellow software engineers, there's a widespread misconception that AI Agents are exclusively the domain of machine learning - as if you need complex data science pipelines to build them. However, once you peek under the hood, you see a familiar landscape of publisher-subscriber patterns, message queues, and function calls to trigger events. It's essentially the same event-driven architecture we've practiced for years, just wrapped in new terminology.

In fact, what we traditionally call a "consumer service" (an application that subscribes to an event bus and reacts to incoming messages) is now being marketed or referred to as an "AI Agent" in some circles. The naming may be driven by business hype or by attempts to highlight the "AI" component. But the core behavior remains the same: listen for an event, perform an action.

In this project, I'll demonstrate how the main trick - known as function calling - lets an AI model (like LLaMA) produce structured data that we then publish to a queue (RabbitMQ). From there, a separate subscriber (our Python worker) handles the task. If you've built event-driven systems before, this will feel quite familiar.

So, despite the hype, you're absolutely correct to say that this is largely software engineering. Sure, there may be optional machine learning or "intelligence" components to refine decisions, but the architecture - the decoupling of services, the event bus, the consumer logic - remains a classic software engineering pattern. Calling it an "AI Agent" doesn't magically change the underlying principles, and as you'll see, it's far from bluffing. It's simply applying function calling in the AI layer to trigger events the same way we always have.

### Observer Pattern

The Observer Pattern is used to create a subscription mechanism that allows multiple components to listen for and react to events. In this project, RabbitMQ acts as the message broker, facilitating communication between the publisher (AI model) and the consumer (task handler).

### Event-Driven Architecture

Event-Driven Architecture is a design paradigm that promotes the production, detection, and reaction to events. This architecture is particularly useful for building scalable and responsive systems. In this project, tasks are published as events to RabbitMQ, and consumers handle these tasks asynchronously, ensuring that the system can scale and respond to varying workloads.

## Setup Guide

### Prerequisites

- Docker
- Docker Compose
- Python 3.x
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/simpleaiagent.git
   cd simpleaiagent
   ```

2. **Set up RabbitMQ using Docker Compose:**
   ```bash
   docker-compose up -d
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage Guide

### Running the Publisher

The publisher sends tasks to RabbitMQ. To run the publisher:

```bash
python ai_model_with_publisher.py
```

### Running the Consumer

The consumer listens for tasks from RabbitMQ and processes them. To run the consumer:

```bash
python ai_agent_or_consumer.py
```

### Example

1. **Start the RabbitMQ service:**
   ```bash
   docker-compose up -d
   ```

2. **Run the publisher to send a task:**
   ```bash
   python ai_model_with_publisher.py
   ```

3. **Run the consumer to process the task:**
   ```bash
   python ai_agent_or_consumer.py
   ```

You should see logs indicating that the task has been published and processed.

## Conclusion

### Conclusion

This project demonstrates how software engineering principles, such as the Observer Pattern and Event-Driven Architecture, can be applied to build a scalable and maintainable system for task management. By leveraging RabbitMQ for communication and task handling, we show how traditional consumer services are now being referred to as AI Agents through the function calling feature. This approach highlights that, despite the AI terminology, the underlying principles remain rooted in classic software engineering patterns.

