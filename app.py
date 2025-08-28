import streamlit as st
from agent import PositioningAgent

agent = PositioningAgent()

st.title("Positioning Statement Agent")
st.subheader("Describe your product")

user_input = st.text_area(
    "Describe your product or feature",
    placeholder="Slack is where teams talk, share files, and connect their tools..."
)

if user_input:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate Category Overview"):
            agent.category_output = agent.generate_category_overview(user_input)

        if st.button("Generate Persona"):
            agent.persona_output = agent.generate_target_persona(user_input)

    with col2:
        if st.button("Generate Competitor Landscape"):
            agent.competitor_output = agent.generate_competitor_landscape(user_input)

        if st.button("Generate Differentiators"):
            agent.differentiators_output = agent.generate_unique_differentiators(user_input)

    # Display outputs
    if agent.category_output:
        st.text_area("Category Overview", value=agent.category_output, height=150)

    if agent.competitor_output:
        st.text_area("Competitor Landscape", value=agent.competitor_output, height=150)

    if agent.persona_output:
        st.text_area("Target Persona", value=agent.persona_output, height=150)

    if agent.differentiators_output:
        st.text_area("Unique Differentiators", value=agent.differentiators_output, height=150)

    # Final positioning
    if st.button("Generate Positioning Statement"):
        combined = agent.get_combined_insights()
        statement = agent.generate_positioning_statement(combined)
        st.text_area("Positioning Statement", value=statement, height=100)