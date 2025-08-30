import streamlit as st
from agent import PositioningAgent
from components.text_box import editable_text_box
from components.progress_tracker import render_progress_tracker
from prod_desc import render_prod_desc
from prod_insight import render_prod_insight
from positioning import render_positioning

if 'agent' not in st.session_state:
    st.session_state.agent = PositioningAgent()

# Session states
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
if "insight_generated" not in st.session_state:
    st.session_state.insight_generated = False
if "positioning_generated" not in st.session_state:
    st.session_state.positioning_generated = False

agent = st.session_state.agent

render_progress_tracker()

st.title("Positioning AI Agent")
st.markdown(
    """
    **Turn fuzzy ideas into a clear positioning statement!**
    
    Describe your product, and this tool will help you turn it into market, competitor, and persona insights that build a strong positioning statement.
    """
)
st.markdown("<br>", unsafe_allow_html=True) 

render_prod_desc()
render_prod_insight()
render_positioning()

st.markdown("<br>", unsafe_allow_html=True) 
st.divider()
st.markdown(
    """

    <div style="text-align: center; color: gray; font-size: 0.9em;">
        © 2025 Jireh Kang · <a href="https://github.com/jirehkang/positioning-agent" target="_blank">GitHub Repo</a>
    </div>
    """,
    unsafe_allow_html=True
)