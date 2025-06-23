from crewai import Agent, Task, Crew
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4")

# Agents
triage_agent = Agent(
    role="Alert Triage Agent",
    goal="Identify and summarize legitimate security incidents from raw alerts",
    backstory="A vigilant SOC analyst specialized in triaging noisy security alerts.",
    llm=llm
)

threat_intel_agent = Agent(
    role="Threat Intelligence Agent",
    goal="Enrich identified incidents with relevant threat intelligence data",
    backstory="An expert in correlating IOCs with global threat databases.",
    llm=llm
)

incident_analyst = Agent(
    role="Incident Analyst Agent",
    goal="Analyze the incident to determine root cause and affected assets",
    backstory="An experienced analyst skilled at understanding attack vectors.",
    llm=llm
)

remediation_planner = Agent(
    role="Remediation Planner Agent",
    goal="Recommend concrete remediation steps based on the analysis",
    backstory="A cybersecurity engineer focused on mitigating threats efficiently.",
    llm=llm
)

reporting_agent = Agent(
    role="Incident Report Agent",
    goal="Generate a structured incident report suitable for executives",
    backstory="A report writer trained to communicate technical findings clearly.",
    llm=llm
)

# Tasks
task1 = Task(
    description="Triage the following alert and determine if it's a valid incident:

"
                "ALERT: Unusual login from IP 203.0.113.55 to admin@example.com at 3AM UTC.",
    agent=triage_agent
)

task2 = Task(
    description="Enrich the alert with threat intel. Include any known threats related to IP 203.0.113.55.",
    agent=threat_intel_agent,
    context=[task1]
)

task3 = Task(
    description="Analyze the incident and identify the root cause, attack vector, and affected systems.",
    agent=incident_analyst,
    context=[task1, task2]
)

task4 = Task(
    description="Plan and recommend detailed remediation actions to contain and recover from the incident.",
    agent=remediation_planner,
    context=[task3]
)

task5 = Task(
    description="Write a final incident report including summary, root cause, and remediation actions.",
    agent=reporting_agent,
    context=[task1, task2, task3, task4]
)

# Crew Execution
crew = Crew(
    agents=[triage_agent, threat_intel_agent, incident_analyst, remediation_planner, reporting_agent],
    tasks=[task1, task2, task3, task4, task5]
)

crew.kickoff()
