from openai import OpenAI
from dotenv import load_dotenv 

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