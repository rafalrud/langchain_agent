# LangChain Agent for Network Automation
This repository contains a Python script that demonstrates how to create an AI agent capable of executing network automation tasks using PyATS (Python Automated Test System) commands. The agent is built using LangChain and the Claude 3.5 Sonnet model from Anthropic.

## Features

- Uses LangChain to create an AI agent for network automation
- Integrates with PyATS for executing network commands
- Employs the Claude 3.5 Sonnet model for natural language processing
- Demonstrates execution of a simple "show ip interface brief" command

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- An Anthropic API key for accessing the Claude model

## Installation

1. Clone the repository:
``` Shell 
git clone https://github.com/rafalrud/langchain_agent.git
cd langchain_agent
```
2. Install the required Python packages:
``` Shell
pip install -r requirements.txt
```
3. Set up your environment variables:

Rename `.env.example` to `.env`. Open `.env` and replace `YOUR_API_KEY_HERE` with your actual Anthropic API key

## Configuration
### Testbed Configuration
The `testbed.yaml` file contains the configuration for the network devices you want to interact with. Ensure this file is properly set up with your network device details before running the script.

### Usage
To run the script, use the following command:
``` Python
python agent.py
```

This will execute the AI agent, which will run the PyATS command show ip interface brief on the devices specified in your testbed.yaml file.
## File Descriptions

- `agent.py`: The main Python script that sets up and runs the LangChain agent.
- `.env`: Contains environment variables, including your Anthropic API key.
requirements.txt: Lists all Python dependencies required for this project.
- `testbed.yaml`: Configuration file for PyATS, specifying network devices and their details.

## Contact
If you have any questions or feedback, please open an issue in this repository.