from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.llms import Ollama


model = Ollama(model="deepseek-r1:7b")
@CrewBase
class CrewJokersCrew():
	"""CrewJokers crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def comedian(self) -> Agent:
		return Agent(
			config=self.agents_config['comedian'],
			verbose=True,
			llm = model
		)

	@agent
	def audience(self) -> Agent:
		return Agent(
			config=self.agents_config['audience'],
			verbose=True,
			llm = model
		)

	@task
	def tell_joke(self) -> Task:
		return Task(
			config=self.tasks_config['tell_joke'],
			agent=self.comedian()
		)

	@task
	def evaluate_joke(self) -> Task:
		return Task(
			config=self.tasks_config['evaluate_joke'],
			agent=self.audience(),
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewJokers crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)