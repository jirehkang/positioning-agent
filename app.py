from openai import OpenAI
from dotenv import load_dotenv 
import os
import gradio as gr

load_dotenv()  # ← This must run BEFORE OpenAI() is called
client = OpenAI()

def generate_product_information(user_input):
    
    response = client.responses.create(
        model="gpt-4o",
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

    return response.output_text

def generate_positioning_statement(product_information):

    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a seasoned product marketing expert helping someone write a positioning statement.",
        input=f"""
        Based on this product information: {product_information}

        Create a positioning statement for the product. The positioning statement should generally follow the format of:
        "For [target audience] who [need or desire], [brand/product] is the [market definition] that [unique value proposition], because [reason to believe]."
        """
    )

    return response.output_text

def display_product_information(user_input):
    product_information = generate_product_information(user_input)
    return product_information

def display_positioning_statement(product_information):
    return generate_positioning_statement(product_information)


with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Positioning Agent")

    with gr.Row():
        user_input = gr.Textbox(label="Describe your product/idea", placeholder="It's an app that helps people...")
        insights_output = gr.TextArea(label="Generated Marketing Content", lines=15)

    generate_button = gr.Button("Generate Content")
    generate_button.click(display_product_information, inputs=user_input, outputs=insights_output)

    gr.Markdown("## Once you're ready, generate a Positioning Statement:")

    final_input = gr.TextArea(label="Paste final summary for Positioning Statement", lines=6)
    final_output = gr.TextArea(label="Positioning Statement", lines=2)
    final_button = gr.Button("Generate Positioning Statement")
    final_button.click(display_positioning_statement, inputs=final_input, outputs=final_output)

demo.launch()