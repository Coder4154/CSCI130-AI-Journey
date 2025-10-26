# hello_ai.py
# Patrick Sherman
# CSCI 130 - Week 1 Project
# Date: 10/26/2025

import random
import datetime

def greeting_agent():

    # Get current time
    current_hour = datetime.datetime.now().hour

    # Determine time of day
    if current_hour < 12:
        time_period = "morning"
    elif current_hour < 17:
        time_period = "afternoon"
    else:
        time_period = "evening"

    # Get user's name
    name = input("What's your name? ")

    # Generate personalized greeting
    greetings = [
        f"Good {time_period}, {name}! Welcome to AI class!",
        f"Hello {name}! Hope you're having a great {time_period}!",
        f"Hi {name}! Ready to learn AI this {time_period}?"
    ]

    # Select and display random greeting
    print(random.choice(greetings))

    # Simple conversation
    mood = input("\nHow are you feeling about learning AI? ")

    # Simple response based on keywords (reflex agent behavior)
    if any(word in mood.lower() for word in ["excited", "good", "happy", "motivated"]):
        print("That's wonderful! Your enthusiasm will help you learn!")
    elif any(word in mood.lower() for word in ["nervous", "worried", "scared", "unsure"]):
        print("Don't worry! We'll take it step by step.")
    else:
        print(f"Thanks for sharing! Let's make this a great learning experience!")

    # Display AI facts
    ai_facts = [
        "AI can analyze large amounts of data much faster than humans.",
        "Machine learning is a subset of AI focused on learning from data.",
        "AI is used in healthcare for diagnosing diseases and analyzing medical images.",
        "Self-driving cars use AI to understand and navigate their surroundings.",
        "Natural Language Processing allows AI to understand and generate human language."
    ]

    print("Fun AI Fact:")
    print(random.choice(ai_facts))


# Call the function
greeting_agent()
