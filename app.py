from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()  # ← This must run BEFORE OpenAI() is called
client = OpenAI()

def generate_product_insights(user_input):
    
    response = client.responses.create(
        model="gpt-5",
        instructions="You are a seasoned product marketing expert helping someone write a positioning strategy.",
        input=f"""
    Based on this idea: {user_input}

    Create the following:
    1. Product description
    2. Category overview
    3. Competitor landscape
    4. Target persona overview
    5. Three unique differentiators
    """
    )

    print(response.output_text)

generate_product_insights("I want to create a positioning strategy for a new product called 'The Perfect Cupcake'.")