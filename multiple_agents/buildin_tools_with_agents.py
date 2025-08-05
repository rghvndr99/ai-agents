
from crewai import Agent, Crew, Task, Process, LLM
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# Load environment variables from .env file
# This includes API keys and other configuration settings
load_dotenv()

# Initialize the Language Model (LLM) configuration
# Using Google's Gemini 2.0 Flash model with low temperature for consistent outputs
llm = LLM(    
    model="gemini/gemini-2.0-flash",  # Google's latest Gemini model
    temperature=0.1  # Low temperature for more deterministic, professional outputs
)

researchAgent = Agent(
    role="Senior Research Analyst",
    goal="Conduct thorough research on given {topic} and gather comprehensive information",
    backstory=(
        "You are a seasoned research analyst with expertise in gathering, analyzing, "
        "and synthesizing information from various sources. You have a keen eye for "
        "detail and can identify key insights and trends."
    ),
    tools=[SerperDevTool()],
    verbose=True,
    llm=llm
)

writerAgent = Agent(
    role="Writer Assistant",
    goal="Write an article ",
    backstory=(
        "You are an expert in professional article writer"
    ),
    verbose=True,
    llm=llm
)

researchTask=Task(
    description=" Find 3-5 interesting and recent facts about {topic}.",
    expected_output="2-3 bullet point summary",
    agent=researchAgent
)

writterTask=Task(
    description="Write a comprehensive and profession article on {topic}",
    expected_output="A hundred word article",
    agent=writerAgent,
    context= [researchTask]
)



# Create the crew (team) of agents
# In this case, we have a single agent with a custom tool
# CrewAI supports multi-agent collaboration with shared tools
crewAgent = Crew(
    agents=[researchAgent,writerAgent],  # List of agents in the crew
    tasks=[researchTask,writterTask],  # List of tasks to be executed
    verbose=True  # Enable detailed logging for the entire crew execution
)

# Execute the crew and get the result
# The kickoff() method starts the task execution process
# The agent can now use the custom capitalization tool during processing
crewAgent.kickoff(inputs= {
    "topic": "The future of electrical vehicles"
})

