
# AI Agents" Is Just Marketing: For Software Engineers, This is Event-Driven Architecture (Agentic Architecture)

Basically there is no 'AI Agent', those who know use the term "Agentic Architecture" to emphasize that these subscribers are agents acting on behalf of an AI model, rather than being inherently "intelligent" themselves. Still, "AI Agent" has become popular (often for marketing or buzzword reasons). As a software developer, remember that when people say "AI Agent," they're usually talking about a subscriber/worker that executes tasks dictated by an AI model - not a fully autonomous, self-thinking entity on its own.

Some might argue they've seen AI Agents with features like "memory" or "chaining" of tasks. But remember, you could implement these same capabilities - tracking conversation state, chaining function calls, and orchestrating tasks - in any well-designed consumer as part of the event-driven workflow. "Memory" just means storing and retrieving context (e.g., in a database or cache), while "chaining" is about coordinating multiple steps or services. Neither requires the consumer itself to be "intelligent." Instead, it's still just reacting to events and managing state, which any software engineer can build without needing advanced ML expertise.

---
## Setup Guide

### Prerequisites

- Docker
- Docker Compose
- Python 3.x
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mrmanna/simple_agentic_architecture.git
   cd ssimple_agentic_architecture
   ```

2. **Set up RabbitMQ using Docker Compose:**
   ```bash
   docker compose -f rabbitmq-docker-compose.yaml up -d
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
python worker_agent.py
```


