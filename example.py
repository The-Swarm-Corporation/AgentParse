from code_guardian.main import CodeGuardian
import os

from dotenv import load_dotenv
from swarms import Agent, OpenAIChat


load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Create an instance of the OpenAIChat class
model = OpenAIChat(
    openai_api_key=api_key,
    model_name="gpt-4o-mini",
    temperature=0.1,
    max_tokens=2000,
)

# Initialize the agent for generating unit tests
agent = Agent(
    agent_name="Unit-Test-Generator-Agent",  # Changed agent name
    system_prompt="Generate example scripts for the following code, make sure you cover all methods, and add comments, return only in python. You're creating examples for the agentparse library remember to import agentparse",  # Updated system prompt
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="unit_test_agent.json",  # Updated saved state path
    user_name="swarms_corp",
    retry_attempts=1,
    context_length=200000,
    return_step_meta=False,
    # output_type="json",
)


# from swarm_models.base_embedding_model import BaseEmbeddingModel
from agentparse.yaml_model import (
    YamlModel,
    create_yaml_schema_from_dict,
    pydantic_type_to_yaml_schema,
)
from agentparse.yaml_output_parser import YamlOutputParser
from agentparse.json_output_parser import JsonOutputParser
from agentparse.main import file_to_string, chunk_text_dynamic

modules = [
    YamlModel,
    create_yaml_schema_from_dict,
    pydantic_type_to_yaml_schema,
    YamlOutputParser,
    JsonOutputParser,
    file_to_string,
    chunk_text_dynamic,
]

#############################


# Initialize CodeGuardian and run
guardian = CodeGuardian(
    classes=modules,  # classes to test
    # agent=agent,  # agent to use
    dir_path="examples",  # directory to save tests
    package_name="agentparse",  # package name
    module_name="agentparse",  # module name
    # agent=prebuilt_agent,
    # model=model,
    agent=agent,
)

guardian.run()
