# AI Agents

A multi-agent AI system powered by CrewAI for collaborative task execution and intelligent automation.

## Overview

This project leverages CrewAI to create a team of AI agents that can collaborate on complex tasks, combining their specialized skills to achieve sophisticated objectives.

## Features

- Multi-agent collaboration using CrewAI framework
- Configurable agent roles, goals, and tools
- Task orchestration and workflow management
- Support for various LLM providers via LiteLLM
- Extensible architecture for custom tools and integrations

## Installation

Ensure you have Python >=3.12 installed on your system.

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-agents
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Configuration

Add your API keys to the `.env` file:
```
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
```

## Usage

Run the AI agents system:
```bash
python main.py
```

## Project Structure

```
ai-agents/
├── src/
│   ├── agents/          # Agent configurations
│   ├── tasks/           # Task definitions
│   ├── tools/           # Custom tools
│   └── crew.py          # Main crew orchestration
├── config/
│   ├── agents.yaml      # Agent configurations
│   └── tasks.yaml       # Task definitions
├── .env                 # Environment variables
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
