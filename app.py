# 20 Questions AI Game - Python Version
# A simpler version using Shiny, shinychat, and chatlas with a single model.

from shiny.express import render, ui
from shinychat.express import Chat
from chatlas import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(".env")  # Load from current directory

# Verify API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("WARNING: OPENAI_API_KEY not found in environment!")
    print("Please check your .env file.")

# System prompt for the 20 Questions game
SYSTEM_PROMPT = """You are playing the classic 20 Questions game with the user, but with reversed roles.
In this game, YOU will think of something and the USER will ask yes/no questions to guess what it is.

Rules:
1. At the start, secretly choose something by FIRST randomly selecting a category (object, animal, person, or place), THEN picking a common item from that category. Vary the categories - don't always pick objects!
2. Keep track of how many questions the user has asked (maximum 20).
3. The initial greeting has already been shown to the user - the game has started and you've already thought of something.
4. Answer the user's questions honestly with 'Yes', 'No', or a very brief clarification if needed. Be playful and funny.
5. If the user guesses correctly before 20 questions, congratulate them and offer to play again.
6. If they reach 20 questions without guessing correctly, reveal your answer and offer to play again.
7. Be friendly, enthusiastic, and make the game fun!
8. If the user asks to play again or start over, think of a NEW thing from a DIFFERENT category than the previous game to add variety.
9. Read the conversation history carefully to understand what thing was chosen and what questions were already asked.
10. IMPORTANT: Do NOT repeat the initial greeting or say "I've thought of something" again - the game has already started.
11. IMPORTANT: Randomly vary between objects, animals, people, and places across different games to keep it interesting!
"""

# Initialize the chat model
chat_model = ChatOpenAI(
    model="gpt-4o-mini",
    system_prompt=SYSTEM_PROMPT
)

# Set Shiny page options
_ = ui.page_opts(title="20 Questions AI Game")  # Assign to _ to prevent rendering

# Initial greeting shown in UI
initial_greeting = "Let's play 20 questions! I will think of something and you ask the questions."

# Create chat instance with initial greeting
chat = Chat(
    id="chat",
    messages=[
        {"content": initial_greeting, "role": "assistant"},
    ],
)

# Display the chat interface
chat.ui()

# Handle user input
@chat.on_user_submit
async def handle_user_input(user_input: str):
    """Process user input and get AI response"""
    try:
        # chatlas maintains conversation state, so we just call chat with the new user input
        # It will automatically use the conversation history
        response = chat_model.chat(user_input)
        
        # Extract the text content from the ChatResponse object
        response_text = response.content if hasattr(response, 'content') else str(response)
        
        # Append the response to the chat UI (role is automatically "assistant" for appended messages)
        await chat.append_message(response_text)
    except Exception as e:
        error_msg = f"Error: {str(e)}. Please check your API key and try again."
        await chat.append_message(error_msg)
        print(f"Error in chat: {e}")
        import traceback
        traceback.print_exc()

