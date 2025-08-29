import streamlit as st
from agent import PositioningAgent
from components import text_box_start_saved, text_box_start_unsaved
from progress_tracker import render_progress_tracker

if 'agent' not in st.session_state:
    st.session_state.agent = PositioningAgent()

# Session state for progress tracking
if 'product_desc_confirmed' not in st.session_state:
    st.session_state.product_desc_confirmed = False
if 'insight_steps_done' not in st.session_state:
    st.session_state.insight_steps_done = {'category': False, 'competitor': False, 'persona': False, 'differentiators': False}
if 'positioning_done' not in st.session_state:
    st.session_state.positioning_done = False

if "editing" not in st.session_state:
    st.session_state.editing = True
if "saved_text" not in st.session_state:
    st.session_state.saved_text = ""

agent = st.session_state.agent

render_progress_tracker()

st.title("Positioning Statement Generator")

st.markdown(
    """
    **Turn fuzzy ideas into a clear message.**
    
    This tool helps you think through what your product does, who it's for, and what makes it different. Along the way, the progress tracker helps you stay focused and see how each step contributes to a solid positioning statement.
    """
)

st.markdown("<br>", unsafe_allow_html=True) 

# product description

st.subheader("1. Describe product description")

text_box_start_unsaved(
    saved_content="Temp",
    placeholder="Slack is where teams talk, share files, and connect their tools...", 
    session_text_key="saved_text",
    session_edit_key="editing",
    area_label="Include your product name, key features, and problems you're solving. Aim to keep it within 1-2 sentences!"
)

# product insights

st.markdown("<br>", unsafe_allow_html=True) 
st.subheader("Step 2: Generate product insight")

# category overview

st.markdown("##### Category Overview")
st.text_area("Write your product category or click the generate button", value=getattr(agent,'category_output', ''), height=200)


# competitor landscape
st.markdown("##### Competitor Landscape")
st.text_area("Write your competitor landscape or click the generate button", value=getattr(agent,'competitor_landscape', ''), height=200)


# target persona   
st.markdown("##### Target Persona")
st.text_area("Write target or click generate", value=getattr(agent, 'target_persona', ''), height=200)


# positioning statement
st.markdown("<br>", unsafe_allow_html=True) 
st.subheader("Step 3: Generate positioning statement")
if st.button("Generate", use_container_width=True):
    if not st.session_state.get("product_desc_confirmed", False) or not all(st.session_state.insight_steps_done.values()):
        st.warning("Please confirm your product idea and complete all product insights before generating your positioning statement.")
    else:
        combined = agent.get_combined_insights()
        statement = agent.generate_positioning_statement(combined)
        st.text_area("Positioning Statement", value=statement, height=200)
        st.success("🎉 Congrats on creating a full positioning statement!")
        st.info(
            "😉 Remember, a positioning statement isn't a one-and-done exercise. Revisit and refine your messaging as you gather more insights about your product, market, and customers. Keep iterating!"
        )
        st.session_state.positioning_done = True
st.divider()

st.markdown(
    """

    <div style="text-align: center; color: gray; font-size: 0.9em;">
        © 2025 Jireh Kang · <a href="https://github.com/jirehkang/positioning-agent" target="_blank">GitHub Repo</a>
    </div>
    """,
    unsafe_allow_html=True
)