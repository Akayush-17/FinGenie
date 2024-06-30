import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "sk-proj-ZTE9GcZUEiWH0KkKb4Q5T3BlbkFJlxgMicc6OYgVNWqi1f5B"

# Prompt for financial advisory conversations
FINANCE_PROMPT = """
You are chatting with a financial advisory bot. Please provide me with your financial goals, current investments, risk tolerance, and any specific financial queries or concerns you have.

Objective:
To revolutionize financial advisory services using generative AI to provide personalized, data-driven financial advice to customers.

Challenge:
- Analyze customer financial data and market trends to generate tailored investment strategies.
- Offer real-time advisory services that adapt to changing financial conditions and customer goals.
- Ensure transparency and explainability in the AI-driven advisory process to build customer trust and confidence.
"""

@textbase.chatbot("finance-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Chatbot logic for generating financial advisory responses"""

    # Extract user messages and concatenate for conversation history
    user_messages = [message.content for message in message_history if message.role == "user"]
    conversation_history = "\n".join(user_messages)

    # Generate GPT-3.5 Turbo response with finance prompt
    bot_response = models.OpenAI.generate(
        system_prompt=FINANCE_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state

# Entry point of the script
if __name__ == "__main__":
    try:
        cli()  # Call the command line interface function
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("Keyboard interrupt received. Terminating the server...")
        sys.exit(1)
