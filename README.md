
# AgentParse


[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)



**AgentParse** is a high-performance parsing library designed to map various structured data formats (such as Pydantic models, JSON, YAML, and CSV) into agent-understandable blocks. By leveraging **AgentParse**, engineers can ensure seamless data ingestion for LLM agents, enabling fast and accurate processing of real-world data.

With a focus on enterprise-grade scalability and flexibility, **AgentParse** provides the tools necessary to build robust systems that support a wide array of business applications. From financial reports to IoT sensor data, **AgentParse** can handle it all with ease.

## Why AgentParse?

In an era where multi-agent systems are increasingly driving enterprise operations, parsing diverse and complex data formats quickly and accurately is critical. Traditional parsing methods can be rigid, error-prone, and often incompatible with large-scale LLM agents.

**AgentParse** is built with agent engineers and enterprise users in mind, providing a solution that:
- **Adapts** to various input formats with minimal configuration
- **Transforms** structured data into formats optimized for LLM agents
- **Scales** across thousands of agents and high-throughput applications
- **Ensures** compliance and data integrity across pipelines

Whether you're building swarms of agents for financial modeling, customer support automation, or real-time decision-making systems, **AgentParse** helps ensure your agents always have access to clean, reliable, and well-structured data.

## Key Features

### 🔄 Multi-Format Parsing

**AgentParse** supports multiple data formats out of the box, allowing agent systems to ingest data from various sources:

- **JSON**: A widely-used format for APIs and web applications.
- **YAML**: A human-readable data format often used in configuration files.
- **CSV**: Structured tabular data, common in financial and operational datasets.
- **Pydantic Models**: Direct parsing of Python's Pydantic models, ensuring type validation and data structure conformity.

### 🚀 Seamless Agent Integration

Easily transform incoming data into **agent-ready blocks**. Agents can immediately interpret and act on parsed data without needing additional transformations or manual configuration.

### 📊 Enterprise-Grade Scalability

Built with high-performance enterprises in mind, **AgentParse** is capable of handling:
- **High-throughput environments** where data ingestion and parsing must occur in real time.
- **Distributed architectures**, where agents deployed across multiple servers can leverage the same data parsing pipeline.

### 🛡️ Data Validation & Error Handling

**AgentParse** provides built-in mechanisms for **data validation** and **error handling**, ensuring that your data is consistent and error-free before it reaches your agents. For example, it automatically validates data against Pydantic models and ensures that no invalid data is passed to agents.

### 🛠️ Customizable Pipelines

Integrate **AgentParse** into your existing pipelines, customize transformations, and add post-processing steps. Easily adapt the library to fit the specific requirements of your use case.

---

## Installation

To install **AgentParse**, simply run:

```bash
pip install -U agentparse
```

Make sure you are using Python 3.7 or above.

---

## Getting Started

### 1. Parse a JSON Object

Here’s how to parse a simple JSON object into an agent-understandable block:

```python
from agentparse import AgentParser

data = """
{
    "name": "John Doe",
    "age": 30,
    "role": "Engineer"
}
"""

parser = AgentParser()
agent_block = parser.parse_json(data)
print(agent_block)
```

Output:

```
AgentBlock(data={'name': 'John Doe', 'age': 30, 'role': 'Engineer'})
```

### 2. Parse a YAML Configuration

```python
from agentparse import AgentParser

yaml_data = """
name: John Doe
age: 30
role: Engineer
"""

parser = AgentParser()
agent_block = parser.parse_yaml(yaml_data)
print(agent_block)
```

Output:

```
AgentBlock(data={'name': 'John Doe', 'age': 30, 'role': 'Engineer'})
```

### 3. Parse a CSV File

```python
from agentparse import AgentParser

csv_data = """
name,age,role
John Doe,30,Engineer
Jane Doe,25,Analyst
"""

parser = AgentParser()
agent_block = parser.parse_csv(csv_data)
print(agent_block)
```

Output:

```
AgentBlock(data=[{'name': 'John Doe', 'age': 30, 'role': 'Engineer'}, {'name': 'Jane Doe', 'age': 25, 'role': 'Analyst'}])
```

### 4. Parse a Pydantic Model

AgentParse allows you to parse Pydantic models directly into agent-understandable blocks:

```python
from pydantic import BaseModel
from agentparse import AgentParser

class User(BaseModel):
    name: str
    age: int
    role: str

user = User(name="John Doe", age=30, role="Engineer")

parser = AgentParser()
agent_block = parser.parse_pydantic(user)
print(agent_block)
```

Output:

```
AgentBlock(data={'name': 'John Doe', 'age': 30, 'role': 'Engineer'})
```

---

## Advanced Usage

### Custom Data Processing

If your agent requires custom data transformations, **AgentParse** allows you to extend its capabilities by adding custom processing steps.

```python
from agentparse import AgentParser, AgentBlock

def custom_transform(data):
    # Custom logic to modify the parsed data
    data['role'] = data['role'].upper()
    return AgentBlock(data)

parser = AgentParser()
parser.add_custom_step(custom_transform)

# Parsing a JSON object
data = '{"name": "John Doe", "age": 30, "role": "Engineer"}'
agent_block = parser.parse_json(data)
print(agent_block)
```

This flexibility allows enterprise engineers to tailor the parsing process to their specific needs.

### Batch Processing for High-Throughput Systems

**AgentParse** supports batch processing, enabling efficient parsing of large datasets across distributed systems:

```python
from agentparse import AgentParser

data_batch = [
    '{"name": "John Doe", "age": 30, "role": "Engineer"}',
    '{"name": "Jane Doe", "age": 25, "role": "Analyst"}'
]

parser = AgentParser()
agent_blocks = parser.batch_parse_json(data_batch)
print(agent_blocks)
```

This is ideal for applications where real-time agent systems need to process thousands or millions of data entries simultaneously.

---

## Integration with Multi-Agent Systems

**AgentParse** integrates seamlessly with agent orchestration frameworks such as [Swarms](https://github.com/kyegomez/swarms), enabling multi-agent systems to process parsed data collaboratively. The parsed agent blocks can be distributed across multiple agents to handle complex workflows, such as financial analysis, marketing automation, or IoT data processing.

### Example: Using with Swarms Framework

```python
from agentparse import AgentParser
from swarms import Swarm

# Initialize parser and swarm
parser = AgentParser()
swarm = Swarm()

# Parse a CSV file and distribute data to agents
csv_data = "name,age,role\nJohn Doe,30,Engineer\nJane Doe,25,Analyst"
agent_block = parser.parse_csv(csv_data)
swarm.distribute(agent_block.data)
```

This example shows how easily **AgentParse** can be combined with multi-agent frameworks to create scalable, real-time systems that understand and act on data from multiple formats.

---

## Enterprise Use-Cases

### 1. **Financial Data Parsing**

Agents can use **AgentParse** to ingest CSV reports from accounting systems and transform them into actionable insights. For example, CSV data containing revenue projections can be parsed and passed to forecasting agents, enabling more accurate financial predictions.

### 2. **Customer Support Automation**

Integrate **AgentParse** with customer support LLM agents to process JSON or YAML configurations from CRM systems. Parsed data can be used to dynamically generate customer responses or action workflows.

### 3. **IoT Data Processing**

**AgentParse** can help process large volumes of sensor data from industrial IoT devices, transforming CSV or JSON telemetry data into blocks that agents can analyze for predictive maintenance or operational efficiency improvements.

---

## Roadmap

### Upcoming Features:
- **Streaming Data Parsing**: Real-time parsing from streaming sources like Kafka or WebSockets.
- **Enhanced Data Validation**: More extensive validation mechanisms for large-scale enterprise applications.
- **New Formats**: Support for additional data formats like Avro, Parquet, and XML.

---

## Contributing

We welcome contributions to improve **AgentParse**! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and add tests.
4. Commit your changes (`git commit -m "Add new feature"`)
5. Push your branch (`git push origin feature/your-feature-name`)
6. Create a pull request on GitHub.

For detailed contribution guidelines, please refer to [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## License

**AgentParse** is licensed under the [MIT License](./LICENSE).