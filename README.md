# CrewJokers Crew

This is a simple project that uses **Deepseek-R1:7b** (set up locally through [Ollama](https://ollama.com/)) to tell a joke and then evaluate it. The project is managed using also **Poetry** dependency management.

---

## Features

- Uses Deepseek-R1:7b for joke generation.
- Evaluates the humor level of the generated jokes.
- Supports both local AI model setup (Ollama) and remote OpenAI API integration.

---

## Prerequisites

- **Python**: Ensure you have Python installed (versions >=3.10 and <=3.13 are supported).
- **Poetry**: Dependency management and virtual environment tool.
- **Ollama**: For running the Deepseek-R1:7b model locally.
- **Virtual Environment Setup**: Alternative support for `requirements.txt`.

---

## Installation

### 1. Install Poetry

Install Poetry using `pip` (if not already installed):

```bash
pip install poetry
```

### Clone the Repository and Navigate to the Directory
```
git clone <repository-url>
cd <repository-directory>
```

#### Create and Activate the Virtual Environment

```
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

#### Install dependencies
```
pip install -r requirements.txt
```

### Install Poetry

Install Poetry using `pip` (if not already installed):

```bash
pip install poetry

poetry lock
poetry install
```


### Running project

```
poetry run crew_jokers 
```