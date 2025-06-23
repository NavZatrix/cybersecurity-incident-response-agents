# test_incident_response.py
# Basic test to simulate the alert triage logic from the main workflow

from langchain.chat_models import ChatOpenAI

def mock_triage_alert(alert_text):
    llm = ChatOpenAI(model="gpt-4")
    response = llm.predict(f"As an alert triage agent, analyze the following alert and determine if it indicates a valid security incident:\n{alert_text}")
    return response

if __name__ == "__main__":
    sample_alert = """ALERT: Unusual login from IP 203.0.113.55 to admin@example.com at 3AM UTC."""
    result = mock_triage_alert(sample_alert)
    print("Triage Result:\n", result)
