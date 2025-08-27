from openai import OpenAI
from dotenv import load_dotenv 
import gradio as gr

load_dotenv()  # ← This must run BEFORE OpenAI() is called
client = OpenAI()

def generate_category_overview(user_input):
    
    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a seasoned product marketing expert helping someone write a positioning strategy.",
        input=f"""
    Based on this idea: {user_input}

    Outline the market you compete in and highlight any differentiators. For example, unlike market X, our market is inherently anxious and cash-strapped.
    """
    )

    return response.output_text

def generate_competitor_landscape(user_input):

    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a seasoned product marketing expert helping someone write a positioning strategy.",
        input=f"""
    Based on this idea: {user_input}

    If customers aren't buying from you, who are they going to? List the top contenders here along with their weaknesses in comparison to you.
    """
    )

    return response.output_text

def generate_target_persona(user_input):

    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a seasoned product marketing expert helping someone write a positioning strategy.",
        input=f"""
    Based on this idea: {user_input}, generate a target persona. 
    
    A good persona includes a fictional name and photo, demographic details (age, location, job), psychographic information (goals, motivations, frustrations, interests), and behavioral patterns such as buying habits and preferred content or communication channels. It often features a narrative or quote from a real user to make the persona feel authentic and provides space for information about their work environment and challenges.
    """
    )

    return response.output_text

def generate_unique_differentiators(user_input):

    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a seasoned product marketing expert helping someone write a positioning strategy.",
        input=f"""
    Based on this idea: {user_input}, generate three unique differentiators. 

    What about your product makes you stand out from the competition? The emphasis here is on the unique, if your competitor offers the exact same thing, it doesn't belong here. Include the challenge (what problem(s) are your customers facing because of a lack of this feature?) and value (how does your unique attribute solve that challenge? Draw on emotion, utopian visions, and real-life quotes where possible.) in each differentiator. 
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

def display_insights(user_input):
    product_information = generate_product_information(user_input)
    return product_information

def display_positioning_statement(product_information):
    return generate_positioning_statement(product_information)


with gr.Blocks() as demo:
    gr.Markdown("# Positioning Statement Agent")

    with gr.Row():
        user_input = gr.Textbox(label="Describe your product or feature", info="Include the name, key features, and problems you're solving. Aim to keep it within 1-2 sentences.", placeholder="Slack is where teams talk, share files, and connect their tools. It solves the mess of scattered communication with one streamlined workspace.")
        insights_output = gr.TextArea(label="Generated Marketing Content", lines=15)

    generate_button = gr.Button("Generate Content")
    generate_button.click(display_product_information, inputs=user_input, outputs=insights_output)

    gr.Markdown("## Once you're ready, generate a Positioning Statement:")

    final_input = gr.TextArea(label="Paste final summary for Positioning Statement", lines=6)
    final_output = gr.TextArea(label="Positioning Statement", lines=2)
    final_button = gr.Button("Generate Positioning Statement")
    final_button.click(display_positioning_statement, inputs=final_input, outputs=final_output)

demo.launch()