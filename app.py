import streamlit as st
from agent import PositioningAgent

if 'agent' not in st.session_state:
    st.session_state.agent = PositioningAgent()

agent = st.session_state.agent
st.title("Positioning Statement Agent")
st.markdown('''

        ''')

# Progress tracker section
st.markdown("### 3 Steps to Building a Positioning Statement")
progress_steps = [
    "1. Enter product idea: This part you have to provide yourself. AI Agent needs some input after all!",
    "2. Define product insights: You can either fill these parts yourselves or ask the AI Agent to generate for you based on your product idea.",
    "3. Generate positioning statement: This is where all your hard work comes together. See the magic happen when you click Generate!"
]
for step in progress_steps:
    st.markdown(f"- {step}")
st.markdown("---")

st.subheader("Step 1: Enter product idea")
user_input = st.text_area(
    "Describe your product or feature",
    placeholder="Slack is where teams talk, share files, and connect their tools...",
    help="For best results, include your product name, key features, and problems you're solving. Aim to keep it within 1-2 sentences!"
)
st.button("Confirm")

st.subheader("Step 2: Define product insight")
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("Category Overview")
with col2:
    if st.button("Generate"):
        agent.category_output = agent.generate_category_overview(user_input)
st.text_area("Write your product category or click the generate button", value=getattr(agent, 'category_output', ''), height=150)

col1, col2 = st.columns([3,1])
with col1:
    st.markdown("Competitor Landscape")
with col2:
    if st.button("Generate Competitor Landscape"):
        agent.competitor_output = agent.generate_competitor_landscape(user_input)
st.text_area("Write competitor or click generate", value=getattr(agent, 'competitor_output', ''), height=150)

col1, col2 = st.columns([3,1])
with col1:
    st.markdown("Target Persona")
with col2:
    if st.button("Generate Target Persona"):
        agent.persona_output = agent.generate_target_persona(user_input)
st.text_area("Write target or click generate", value=getattr(agent, 'persona_output', ''), height=150)

col1, col2 = st.columns([3,1])
with col1:
    st.markdown("Unique Differentiators")
with col2:
    if st.button("Generate Differentiators"):
        agent.differentiators_output = agent.generate_unique_differentiators(user_input)
st.text_area("Write differentiators or click generate", value=getattr(agent, 'differentiators_output', ''), height=150)

# Final positioning
st.subheader("Step 3: Generate positioning statement")
if st.button("Generate Positioning Statement"):
    combined = agent.get_combined_insights()
    statement = agent.generate_positioning_statement(combined)
    st.text_area("Positioning Statement", value=statement, height=100)
    st.success("Congrats on creating a full positioning statement!")
    st.info(
        "Remember, a positioning statement isn't a one-and-done exercise. Revisit and refine your messaging as you gather more insights about your product, market, and customers. Keep iterating!"
    )

st.divider()

st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 0.9em;">
        © 2025 Jireh Kang · <a href="https://github.com/jirehkang/positioning-agent" target="_blank">GitHub Repo</a>
    </div>
    """,
    unsafe_allow_html=True
)