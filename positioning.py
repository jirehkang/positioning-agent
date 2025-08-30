import streamlit as st
from components.text_box import editable_text_box
from agent import PositioningAgent

if 'agent' not in st.session_state:
    st.session_state.agent = PositioningAgent()
agent = st.session_state.agent

def render_positioning():
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
        if not st.session_state.get("product_desc_complete", False):
            st.error("Enter your product description and generate product insights to see your positioning statement.")
        else:
            st.session_state.positioning_text = agent.generate_category_overview(user_input)
            editable_text_box(
                saved_content=st.session_state.positioning_text,
                session_text_key="positioning_text",
                session_edit_key="positioning_editing",
                session_status_confirmed="positioning_complete",
                area_label="Edit",
                default_edit_mode=False,
                success_message="Changes saved!"
            )
            st.session_state.positioning_generated = True
            st.success("🎉 Congrats on creating your positioning statement!")
            st.info(
                "😉 Remember, a positioning statement isn't a one-and-done exercise. Revisit and refine your messaging as you gather more insights about your product, market, and customers. Keep iterating!"
            )
