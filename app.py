import streamlit as st
from agent import PositioningAgent

if 'agent' not in st.session_state:
    st.session_state.agent = PositioningAgent()

agent = st.session_state.agent
st.title("Positioning Statement Agent")
st.header("Describe your product")

user_input = st.text_area(
    "Describe your product or feature",
    placeholder="Slack is where teams talk, share files, and connect their tools..."
)

col1, col2 = st.columns([3,1])
with col1:
    st.subheader("Category Overview")
with col2:
    if st.button("Generate Category Overview"):
        agent.category_output = agent.generate_category_overview(user_input)
st.text_area("Write your product category or click the generate button", value=getattr(agent, 'category_output', ''), height=150)

col1, col2 = st.columns([3,1])
with col1:
    st.subheader("Competitor Landscape")
with col2:
    if st.button("Generate Competitor Landscape"):
        agent.competitor_output = agent.generate_competitor_landscape(user_input)
st.text_area("Write competitor or click generate", value=getattr(agent, 'competitor_output', ''), height=150)

col1, col2 = st.columns([3,1])
with col1:
    st.subheader("Target Persona")
with col2:
    if st.button("Generate Target Persona"):
        agent.persona_output = agent.generate_target_persona(user_input)
st.text_area("Write target or click generate", value=getattr(agent, 'persona_output', ''), height=150)

col1, col2 = st.columns([3,1])
with col1:
    st.subheader("Unique Differentiators")
with col2:
    if st.button("Generate Differentiators"):
        agent.differentiators_output = agent.generate_unique_differentiators(user_input)
st.text_area("Write differentiators or click generate", value=getattr(agent, 'differentiators_output', ''), height=150)

# Final positioning
if st.button("Generate Positioning Statement"):
    combined = agent.get_combined_insights()
    statement = agent.generate_positioning_statement(combined)
    st.text_area("Positioning Statement", value=statement, height=100)