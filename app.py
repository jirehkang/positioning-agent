import streamlit as st
from agent import PositioningAgent
from components.text_box import editable_text_box
from components.progress_tracker import render_progress_tracker

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

# product description
st.subheader("Step 1. Describe your product")
editable_text_box(
    saved_content="",
    placeholder="Slack is where teams talk, share files, and connect their tools...", 
    session_text_key="saved_text",
    session_edit_key="editing",
    session_status_confirmed="product_desc_confirmed",
    area_label="For best results, include your product name, key features, and problems you're solving.",
    default_edit_mode=True,
    success_message="Changes saved. You can now generate product insight!"
)

# product insights
st.markdown("<br>", unsafe_allow_html=True) 
st.subheader("Step 2: Generate product insight")
st.markdown("Based on your product description, generate insight on your product's market category, competitors, persona, and differentiators. After they're generated, you'll have the option to adjust them as needed for accuracy.")

if "generate_insight_clicked" not in st.session_state:
    st.session_state.generate_insight_clicked = False

if not st.session_state.insight_generated:
    if st.button("Generate", key="generate_product_insight", use_container_width=True):
        st.session_state.generate_insight_clicked = True

if st.session_state.generate_insight_clicked and st.session_state.insight_generated:
        user_input = st.session_state.get("saved_text", "")
        if not st.session_state.get("product_desc_confirmed", False):
            st.error("Enter your product description to generate product insight.")

if st.session_state.generate_insight_clicked:
    user_input = st.session_state.get("saved_text", "")
    if "category_text" not in st.session_state:
        st.session_state.category_text = agent.generate_category_overview(user_input)
    if st.session_state.category_text:
        st.markdown("##### Market Category Overview")
        editable_text_box(
            saved_content=st.session_state.category_text,
            session_text_key="category_text",
            session_edit_key="category_editing",
            session_status_confirmed="category",
            area_label="Product Category Overview",
            default_edit_mode=False,
            height=230,
            success_message="Changes saved!"
        )

    if "competitor_text" not in st.session_state:
        st.session_state.competitor_text = agent.generate_competitor_landscape(user_input)
    if st.session_state.competitor_text:
        st.markdown("##### Competitor Landscape")
        editable_text_box(
            saved_content=st.session_state.competitor_text,
            session_text_key="competitor_text",
            session_edit_key="competitor_editing",
            session_status_confirmed="competitor",
            area_label="Competitor Landscape",
            default_edit_mode=False,
            height=230,
            success_message="Changes saved!"
        )


    if "persona_text" not in st.session_state:
        st.session_state.persona_text = agent.generate_target_persona(user_input)
    if st.session_state.persona_text:
        st.markdown("##### Target Persona")
        editable_text_box(
            saved_content=st.session_state.persona_text,
            session_text_key="persona_text",
            session_edit_key="persona_editing",
            session_status_confirmed="persona",
            area_label="Target Persona",
            default_edit_mode=False,
            height=230,
            success_message="Changes saved!"
        )

    if "differentiators_text" not in st.session_state :
        st.session_state.differentiators_text = agent.generate_unique_differentiators(user_input)
    if st.session_state.persona_text:
        st.markdown("##### Unique Differentiators")
        editable_text_box(
            saved_content=st.session_state.differentiators_text,
            session_text_key="differentiators_text",
            session_edit_key="differentiators_editing",
            session_status_confirmed="differentiators",
            area_label="Unique Differentiators",
            default_edit_mode=False,
            height=230,
            success_message="Changes saved!"
        )
    
    st.session_state.insight_generated = True        
    st.session_state.insight_steps_done = {
        'category': True,
        'competitor': True,
        'persona': True,
        'differentiators': True
    }
    st.success("Product insight generation complete!")

# positioning statement
st.markdown("<br>", unsafe_allow_html=True) 
st.subheader("Step 3: Generate positioning statement")
st.markdown("If you're satisfied with the product description and product insight, click the button below to generate your positioning statement.")

if "generate_positioning_clicked" not in st.session_state:
    st.session_state.generate_positioning_clicked = False

if not st.session_state.positioning_generated:
    if st.button("Generate", key="generate_positioning_statement", 
    use_container_width=True):
        st.session_state.generate_positioning_clicked = True

if st.session_state.generate_positioning_clicked and not st.session_state.positioning_generated:
    combined = agent.get_combined_insights()
    user_input = st.session_state.get(combined, "")
    if not st.session_state.get("product_desc_confirmed", False):
        st.error("Enter your product description and generate product insights to see your positioning statement.")
    else:
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
        st.session_state.positioning_generated = True
        st.success("🎉 Congrats on creating your positioning statement!")
        st.info(
            "😉 Remember, a positioning statement isn't a one-and-done exercise. Revisit and refine your messaging as you gather more insights about your product, market, and customers. Keep iterating!"
        )



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