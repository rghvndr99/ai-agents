"""
Email Assistant Module with Custom Tool

This module creates an AI-powered email assistant using CrewAI framework.
The assistant transforms informal or unprofessional emails into well-structured,
professional communications suitable for workplace environments.
It includes a custom tool for text capitalization.

Author: Raghav
Date: 2025
"""

from crewai import Agent, Crew, Task, Process, LLM
from dotenv import load_dotenv

# Load environment variables from .env file
# This includes API keys and other configuration settings
load_dotenv()

# Initialize the Language Model (LLM) configuration
# Using Google's Gemini 2.0 Flash model with low temperature for consistent outputs
llm = LLM(    
    model="gemini/gemini-2.0-flash",  # Google's latest Gemini model
    temperature=0.1  # Low temperature for more deterministic, professional outputs
)

# Sample informal email that needs professional transformation
# This represents the type of unprofessional communication the agent will improve
email = "shut up and get lost, no need to come to office tomorrow"

# Import BaseTool for creating custom tools
from crewai.tools import BaseTool

class MyCustomTool(BaseTool):
    """
    Custom tool for capitalizing the first letter of each word in text.
    This tool can be used by agents to format text properly.
    """
    name: str = "Capitalise first letter"
    description: str = "Takes the input and capitalise first letter of each word"

    def _run(self, text: str) -> str:
        """
        Execute the tool's main functionality.
        
        Args:
            text (str): Input text to be capitalized
            
        Returns:
            str: Text with first letter of each word capitalized
        """
        print(text, '****')  # Debug output to show input
        return text.title()  # Capitalize first letter of each word

# Create an instance of the custom tool
jr = MyCustomTool()

# Test the custom tool with sample text
test_result = jr.run('HERE IS SEEE')
print(f"Tool output: {test_result}")

# Create the email assistant agent
# This agent specializes in professional email writing and communication
# It now has access to the custom capitalization tool
email_agent = Agent(
    role="email_assistant",  # Agent's primary role identifier
    goal="Write a professional email by removing ABBRs",  # Main objective
    backstory="An experienced and professional email writter",  # Agent's background context
    verbose=True,  # Enable detailed logging for debugging
    tools=[jr],  # Provide the custom tool to the agent
    llm=llm  # Assign the configured language model
)

# Define the email writing task
# This task contains all the instructions and specifications for the agent
email_writing_task = Task(
    name="Email Writing Task",  # Task identifier
    description=f"take the following email and write in best formal manner: '{email}'",  # Task instructions
    expected_output=(
        "A well-written email text that is ready to be sent, includes an appropriate greeting, "
        "body content, and closing signature. Ensure tone and structure are aligned with the instructions."
    ),  # Detailed output requirements
    input_spec={
        # Optional input parameters that can be provided to customize the email
        "recipient_name": "Name of the recipient (e.g., John)",
        "email_subject": "Subject line of the email",
        "email_purpose": "Purpose or context of the email (e.g., follow-up after meeting)",
        "key_points": "List of bullet points or content to include in the body",
        "tone": "Tone of the email (e.g., formal, friendly, urgent)",
        "sender_name": "Name of the sender (to be used in closing)"
    },
    agent=email_agent  # Assign the task to the email assistant agent
)

# Create the crew (team) of agents
# In this case, we have a single agent with a custom tool
# CrewAI supports multi-agent collaboration with shared tools
crewAgent = Crew(
    agents=[email_agent],  # List of agents in the crew
    tasks=[email_writing_task],  # List of tasks to be executed
    verbose=True  # Enable detailed logging for the entire crew execution
)

# Execute the crew and get the result
# The kickoff() method starts the task execution process
# The agent can now use the custom capitalization tool during processing
result = crewAgent.kickoff()

# Display the final result
# This will show the professionally transformed email
print(result)
