from openai import OpenAI
from dotenv import load_dotenv 
import gradio as gr

load_dotenv()
client = OpenAI()

class PositioningAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = "gpt-4.1-nano"
        self.default_instructions = "You are a seasoned product marketing expert helping someone write a positioning strategy. Don't use em dashes(—) and don't add Markdown styling to the responses."
        self.category_output = ""
        self.competitor_output = ""
        self.persona_output = ""
        self.differentiators_output = ""

    def generate(self, user_input):
        response = self.client.responses.create(
            model = self.model,
            instructions = self.default_instructions,
            input=user_input
        )
        return response.output_text 

    def generate_category_overview(self, user_input):
        
        prompt=f"""
        Based on this idea: {user_input}

        Describe the market you compete in and highlight any differentiators. For example, unlike market X, our market is inherently anxious and cash-strapped.
        """

        return self.generate(prompt)

    def generate_competitor_landscape(self, user_input):

        prompt=f"""
        Based on this idea: {user_input}

        If customers aren't buying from you, who are they going to? List the top contenders here along with their weaknesses in comparison to you.
        """

        return self.generate(prompt)
    
    def generate_target_persona(self, user_input):

        prompt=f"""
        Based on this idea: {user_input}, generate a target persona. 
        
        A good persona includes a fictional name and photo, demographic details (age, location, job), psychographic information (goals, motivations, frustrations, interests), and behavioral patterns such as buying habits and preferred content or communication channels. It often features a narrative or quote from a real user to make the persona feel authentic and provides space for information about their work environment and challenges.
        """
        
        return self.generate(prompt)

    def generate_unique_differentiators(self, user_input):

        prompt=f"""
        Based on this idea: {user_input}, generate three unique differentiators. 

        What about your product makes you stand out from the competition? The emphasis here is on the unique, if your competitor offers the exact same thing, it doesn't belong here. Include the challenge (what problem(s) are your customers facing because of a lack of this feature?) and value (how does your unique attribute solve that challenge? Draw on emotion, utopian visions, and real-life quotes where possible.) in each differentiator. 
        """

        return self.generate(prompt)
    
    
    def generate_all_insights(self, user_input):
        self.category_output = self.generate_category_overview(user_input)
        self.competitor_output = self.generate_competitor_landscape(user_input)
        self.persona_output = self.generate_target_persona(user_input)
        self.differentiators_output = self.generate_unique_differentiators(user_input)

    def get_combined_insights(self):
        combined = f"Category Overview:\n{self.category_output}\n\nCompetitor Landscape:\n{self.competitor_output}\n\nTarget Persona:\n{self.persona_output}\n\nUnique Differentiators:\n{self.differentiators_output}"
        return combined

    def generate_positioning_statement(self, combined):

        prompt=f"""
            Based on this product information: {combined}

            Create a positioning statement for the product. The positioning statement should generally follow the format of:
            "For [target audience] who [need or desire], [brand/product] is the [market definition] that [unique value proposition], because [reason to believe]."
            """

        return self.generate(prompt)
    
agent = PositioningAgent()

with gr.Blocks() as demo:
    gr.Markdown("# Positioning Statement Agent")
    gr.Markdown("## Describe your product and generate product insight:")

    with gr.Row():
        user_input = gr.TextArea(label="Describe your product or feature", info="Include the name, key features, and problems you're solving. Aim to keep it within 1-2 sentences.", placeholder="Slack is where teams talk, share files, and connect their tools. It solves the mess of scattered communication with one streamlined workspace.", lines=10)
    
    with gr.Row():
        with gr.Column():
            category_output = gr.TextArea(label="Category Overview", lines=2)
            category_button = gr.Button("Generate Category")
            category_button.click(agent.generate_category_overview, inputs=user_input, outputs=category_output)

        with gr.Column():
            competitor_output = gr.TextArea(label="Competitor Landscape", lines=10)
            competitor_button = gr.Button("Generate Competitor")
            competitor_button.click(agent.generate_competitor_landscape, inputs=user_input, outputs=competitor_output)

        with gr.Column():
            persona_output = gr.TextArea(label="Target Persona", lines=10)
            persona_button = gr.Button("Generate Persona")
            persona_button.click(agent.generate_target_persona, inputs=user_input, outputs=persona_output)

        with gr.Column():
            differentiators_output = gr.TextArea(label="Unique Differentiators", lines=10)
            differentiators_button = gr.Button("Generate Differentiators")
            differentiators_button.click(agent.generate_unique_differentiators, inputs=user_input, outputs=differentiators_output)

    gr.Markdown("## Once you're ready, generate a Positioning Statement:")
    
    final_input = gr.State()
    final_output = gr.TextArea(label="Positioning Statement", lines=2)
    final_button = gr.Button("Generate")
    final_button.click(agent.generate_positioning_statement, inputs=final_input, outputs=final_output)

demo.launch()