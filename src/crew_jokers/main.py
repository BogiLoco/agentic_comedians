from crew_jokers.crew import CrewJokersCrew


def run():
    inputs = {
        'topic': 'Horse'
    }
    CrewJokersCrew().crew().kickoff(inputs=inputs)