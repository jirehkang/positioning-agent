import streamlit as st
from components.text_box import editable_text_box
from agent import PositioningAgent

if 'agent' not in st.session_state:
    st.session_state.agent = PositioningAgent()
agent = st.session_state.agent

def render_positioning():
    st.markdown("<br>", unsafe_allow_html=True) 
    st.subheader("Step 3: Generate positioning statement")
    st.markdown("If you're satisfied with the product description and insight, generate your positioning statement.")

    if "generate_positioning_clicked" not in st.session_state:
        st.session_state.generate_positioning_clicked = False

    if not st.session_state.positioning_generated:
        if st.button("Generate", key="generate_positioning_statement", 
        use_container_width=True):
            st.session_state.generate_positioning_clicked = True

    if st.session_state.generate_positioning_clicked and not st.session_state.positioning_generated:
        if not st.session_state.get("product_desc_complete", False) or not st.session_state.get("insight_generated", False):
            st.error("Please complete your product description and generate product insights before generating your positioning statement.")
        else:
            with st.spinner("Generating your positioning statement..."):
                print("DEBUG: prod_desc_text:\n", st.session_state.get("prod_desc_text", ""))
                print("DEBUG: category_text:\n", st.session_state.get("category_text", ""))
                print("DEBUG: differentiators_text:\n", st.session_state.get("differentiators_text", ""))
                print("DEBUG: competitor_text:\n", st.session_state.get("competitor_text", ""))
                print("DEBUG: persona_text:\n", st.session_state.get("persona_text", ""))
                user_input = "\n\n".join([
                    st.session_state.get("prod_desc_text", ""),
                    st.session_state.get("category_text", ""),
                    st.session_state.get("differentiators_text", ""),
                    st.session_state.get("competitor_text", ""),
                    st.session_state.get("persona_text", "")
                ])
                print("DEBUG: user_input for positioning statement:\n", user_input)
                st.session_state.positioning_text = agent.generate_positioning_statement(user_input)
                st.session_state.positioning_generated = True
                st.session_state.positioning_complete = True
                st.session_state.generate_positioning_clicked = False  # Reset flag

            st.success("🎉 Congrats on creating your positioning statement!")
            st.info(
                "😉 Remember, a positioning statement isn't a one-and-done exercise. Keep iterating as you gather more insights about your product, market, and customers!"
            )

    if st.session_state.get("positioning_generated", False):    
        st.markdown("##### Positioning Statement")
        editable_text_box(
            saved_content=st.session_state.positioning_text,
            session_text_key="positioning_text",
            session_edit_key="positioning_editing",
            session_status_confirmed="positioning_complete",
            area_label="Edit positioning statement",
            label_visibility="collapsed",
            default_edit_mode=False,
            success_message="Changes saved!"
        )
