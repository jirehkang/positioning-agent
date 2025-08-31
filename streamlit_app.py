import streamlit as st
from components.text_box import editable_text_box
from components.progress_tracker import render_progress_tracker
from prod_desc import render_prod_desc
from prod_insight import render_prod_insight
from positioning import render_positioning

# Session states
if 'product_desc_complete' not in st.session_state:
    st.session_state.product_desc_complete = False
if 'product_insight_complete' not in st.session_state:
    st.session_state.product_insight_complete = {
        'category': False, 
        'competitor': False, 
        'persona': False, 
        'differentiators': False
    }
if 'positioning_complete' not in st.session_state:
    st.session_state.positioning_complete = False
if "editing" not in st.session_state:
    st.session_state.editing = True
if "saved_text" not in st.session_state:
    st.session_state.saved_text = ""
if "insight_generated" not in st.session_state:
    st.session_state.insight_generated = False
if "positioning_generated" not in st.session_state:
    st.session_state.positioning_generated = False

st.title("Positioning Generator")

# Reset All button logic
if st.button("🔄 Reset All", key="reset_all"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
st.markdown(
    """
    **Turn fuzzy ideas into a clear positioning statement!**
    
    Describe your product, and this tool will help you turn it into market, competitor, and persona insights that build a strong positioning statement.
    """, 
    help="Approach inspired by Product Marketing Alliance's article [Your Guide to Positioning](https://www.productmarketingalliance.com/your-guide-to-positioning/)."
)
st.markdown("<br>", unsafe_allow_html=True) 

render_prod_desc()
render_prod_insight()
render_positioning()
render_progress_tracker()

st.markdown("<br>", unsafe_allow_html=True) 
st.divider()
st.markdown(
    """

    <div style="text-align: center; color: gray; font-size: 0.9em;">
        © 2025 Jireh Kang · <a href="https://github.com/jirehkang/positioning-generator" target="_blank">GitHub Repo</a>
    </div>
    """,
    unsafe_allow_html=True
)