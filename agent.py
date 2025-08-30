from openai import OpenAI
from dotenv import load_dotenv 

load_dotenv()
client = OpenAI()

class PositioningAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = "gpt-4.1-nano"
        self.default_instructions = "You are a seasoned product marketing expert helping someone write a positioning strategy. Don't use em dashes(—) and don't add Markdown styling to the responses. Do not start with a conversational opener but go straight to answering the prompt. Do not end with a conversational closer."
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

        Describe the market the product competes in and highlight any differentiators. For example, unlike market X, our market is inherently anxious and cash-strapped. Keep response within 650 characters (without spaces).
        """

        return self.generate(prompt)

    def generate_competitor_landscape(self, user_input):

        prompt=f"""
        Based on this idea: {user_input}, list the top three competitors in the product's market. Also include each competitor's strengths and weaknesses in comparison to your product. Keep response within 650 characters (without spaces).
        """

        return self.generate(prompt)
    
    def generate_target_persona(self, user_input):

        prompt=f"""
        Based on this idea: {user_input}, generate a target persona for the product. 
        
        A good persona includes a fictional name, demographic details (age, location, job), psychographic information (goals, motivations, frustrations, interests), and behavioral patterns such as buying habits and preferred content or communication channels. It often features a narrative or quote from a real user to make the persona feel authentic and provides space for information about their work environment and challenges. 

        Keep response within 700 characters (without spaces) and structure the response in the following format: 
            Name: 
            Age: 
            Location: 
            Job: 
            Goals: 
            Motivations: 
            Frustrations: 
            Interests: 
            Behavior: 
            Quote:
            Work environment:
        """
        
        return self.generate(prompt)

    def generate_unique_differentiators(self, user_input):

        prompt=f"""
        Based on this idea: {user_input}, generate three unique differentiators of the product. 

        What about the product makes it stand out from the competition? If the competitor offers the exact same thing, it's not unique and doesn't belong here. 
        
        For each differentiator, include its challenge and value. As for the challenge, what problem(s) are customers facing because of a lack of this feature? As for the value, how does the unique attribute solve that challenge Draw on emotion, utopian visions, and real-life quotes where possible.

        Keep response within 800 characters (without spaces).
        """

        return self.generate(prompt)

    def generate_positioning_statement(self, user_input):

        prompt=f"""
            Based on this product information: {user_input}

            Create a positioning statement for the product. The positioning statement should generally follow the format of:
            "For [target audience] who [need or desire], [brand/product] is the [market definition] that [unique value proposition], because [reason to believe]."
            """

        return self.generate(prompt)