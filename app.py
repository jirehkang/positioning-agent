import streamlit as st
from agent import PositioningAgent
from components import editable_text_box
from progress_tracker import render_progress_tracker

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

st.title("Positioning Statement Generator")

st.markdown(
    """
    **Turn fuzzy ideas into a clear message!**
    
    This tool helps you think through what your product does, who it's for, and what makes it different. The progress tracker on the left helps you see how each step contributes to a solid positioning statement.
    """
)

st.markdown("<br>", unsafe_allow_html=True) 

# product description
st.subheader("1. Describe your product")
editable_text_box(
    saved_content="",
    placeholder="Slack is where teams talk, share files, and connect their tools...", 
    session_text_key="saved_text",
    session_edit_key="editing",
    session_status_confirmed="product_desc_confirmed",
    area_label="Include your product name, key features, and problems you're solving. Aim to keep it within 1-2 sentences!",
    default_edit_mode=True,
    success_message="Description saved! Now click Generate Product Insight."
)

# product insights
st.markdown("<br>", unsafe_allow_html=True) 
st.subheader("Step 2: Generate product insight")
if st.button("Generate", key="generate_product_insight", use_container_width=True):
    user_input = st.session_state.get("saved_text", "")
    if not st.session_state.get("product_desc_confirmed", False):
        st.error("Enter your product description to generate product insight.")
    else:
        st.session_state.insight_generated = True
        st.success("Product insight generation complete!")

if st.session_state.insight_generated:
    user_input = st.session_state.get("saved_text", "")
    st.markdown("##### Category Overview")
    if "category_text" not in st.session_state:
        st.session_state.category_text = agent.generate_category_overview(user_input)
    editable_text_box(
        saved_content=st.session_state.category_text,
        session_text_key="category_text",
        session_edit_key="category_editing",
        session_status_confirmed="category",
        area_label="Product Category Overview",
        default_edit_mode=False,
        success_message="Category saved!"
    )

    st.markdown("##### Competitor Landscape")
    if "competitor_text" not in st.session_state:
        st.session_state.competitor_text = agent.generate_competitor_landscape(user_input)
    editable_text_box(
        saved_content=st.session_state.competitor_text,
        session_text_key="competitor_text",
        session_edit_key="competitor_editing",
        session_status_confirmed="competitor",
        area_label="Competitor Landscape",
        default_edit_mode=False,
        success_message="Competitor landscape saved!"
    )

    st.markdown("##### Target Persona")
    if "persona_text" not in st.session_state:
        st.session_state.persona_text = agent.generate_target_persona(user_input)
    editable_text_box(
        saved_content=st.session_state.persona_text,
        session_text_key="persona_text",
        session_edit_key="persona_editing",
        session_status_confirmed="persona",
        area_label="Target Persona",
        default_edit_mode=False,
        success_message="Persona saved!"
    )

    st.markdown("##### Unique Differentiators")
    if "differentiators_text" not in st.session_state :
        st.session_state.differentiators_text = agent.generate_unique_differentiators(user_input)
    editable_text_box(
        saved_content=st.session_state.differentiators_text,
        session_text_key="differentiators_text",
        session_edit_key="differentiators_editing",
        session_status_confirmed="differentiators",
        area_label="Unique Differentiators",
        default_edit_mode=False,
        success_message="Differentiators saved!"
    )
        

# positioning statement
st.markdown("<br>", unsafe_allow_html=True) 
st.subheader("Step 3: Generate positioning statement")
if st.button("Generate", key="generate_positioning_statement", 
use_container_width=True):
    if not st.session_state.get("product_desc_confirmed", False):
        st.error("Enter your product description and generate product insights to see your positioning statement.")
    else:
        st.session_state.positioning_generated = True
        st.success("🎉 Congrats on creating your positioning statement!")
        st.info(
            "😉 Remember, a positioning statement isn't a one-and-done exercise. Revisit and refine your messaging as you gather more insights about your product, market, and customers. Keep iterating!"
        )
        st.session_state.insight_steps_done = {
            'category': True,
            'competitor': True,
            'persona': True,
            'differentiators': True
        }

if st.session_state.positioning_generated:
    combined = agent.get_combined_insights()
    user_input = st.session_state.get(combined, "")
    if "positioning_text" not in st.session_state:
        st.session_state.positioning_text = agent.generate_category_overview(user_input)
    editable_text_box(
        saved_content=st.session_state.positioning_text,
        session_text_key="positioning_text",
        session_edit_key="positioning_editing",
        session_status_confirmed="positioning_done",
        area_label="Edit",
        default_edit_mode=False,
        success_message="Changes saved!"
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