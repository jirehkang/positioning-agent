import streamlit as st
from agent import PositioningAgent

if 'agent' not in st.session_state:
    st.session_state.agent = PositioningAgent()

# Session state for progress tracking
if 'product_idea_confirmed' not in st.session_state:
    st.session_state.product_idea_confirmed = False
if 'insight_steps_done' not in st.session_state:
    st.session_state.insight_steps_done = {'category': False, 'competitor': False, 'persona': False, 'differentiators': False}
if 'positioning_done' not in st.session_state:
    st.session_state.positioning_done = False

agent = st.session_state.agent
st.title("Positioning Statement Agent")
st.markdown('''

        ''')

# Progress tracker section (dynamic)
st.markdown("### 📊 Your Progress")

step1_status = "✅" if st.session_state.product_idea_confirmed else "⬜"
st.markdown(f"{step1_status} Step 1: Enter product idea")

step2_complete = all(st.session_state.insight_steps_done.values())
step2_status = "✅" if step2_complete else "⬜"
st.markdown(f"{step2_status} Step 2: Define product insights")

step3_status = "✅" if st.session_state.positioning_done else "⬜"
st.markdown(f"{step3_status} Step 3: Generate positioning statement")

st.markdown("---")

st.subheader("Step 1: Enter product idea")
user_input = st.text_area(
    "Describe your product or feature",
    placeholder="Slack is where teams talk, share files, and connect their tools...",
    help="For best results, include your product name, key features, and problems you're solving. Aim to keep it within 1-2 sentences!"
)
if st.button("Confirm"):
    st.session_state.product_idea_confirmed = True
    st.success("✅ Product idea confirmed! You can now define your product insights.")

st.subheader("Step 2: Define product insight")
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("Category Overview")
with col2:
    if st.button("Generate", key="category_overview"):
        agent.category_output = agent.generate_category_overview(user_input)
        st.session_state.insight_steps_done['category'] = True
        st.success("✅ Category overview generated!")
st.text_area("Write your product category or click the generate button", value=getattr(agent, 'category_output', ''), height=150)

col1, col2 = st.columns([3,1])
with col1:
    st.markdown("Competitor Landscape")
with col2:
    if st.button("Generate", key="competitor_landscape"):
        agent.competitor_output = agent.generate_competitor_landscape(user_input)
        st.session_state.insight_steps_done['competitor'] = True
        st.success("✅ Competitor landscape generated!")
st.text_area("Write competitor or click generate", value=getattr(agent, 'competitor_output', ''), height=150)

col1, col2 = st.columns([3,1])
with col1:
    st.markdown("Target Persona")
with col2:
    if st.button("Generate", key="target_persona"):
        agent.persona_output = agent.generate_target_persona(user_input)
        st.session_state.insight_steps_done['persona'] = True
        st.success("✅ Target persona generated!")
st.text_area("Write target or click generate", value=getattr(agent, 'persona_output', ''), height=150)

col1, col2 = st.columns([3,1])
with col1:
    st.markdown("Unique Differentiators")
with col2:
    if st.button("Generate", key="unique_differentiators"):
        agent.differentiators_output = agent.generate_unique_differentiators(user_input)
        st.session_state.insight_steps_done['differentiators'] = True
        st.success("✅ Differentiators generated!")
st.text_area("Write differentiators or click generate", value=getattr(agent, 'differentiators_output', ''), height=150)

# Final positioning
st.subheader("Step 3: Generate positioning statement")
if st.button("Generate Positioning Statement"):
    st.session_state.positioning_done = True
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