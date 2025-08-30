import streamlit as st
from components.text_box import editable_text_box
from agent import PositioningAgent

if 'agent' not in st.session_state:
    st.session_state.agent = PositioningAgent()
agent = st.session_state.agent

def render_prod_insight():
    st.markdown("<br>", unsafe_allow_html=True) 
    st.subheader("Step 2: Generate product insight")
    st.markdown("Based on your product description, generate insight on your product's market category, competitors, persona, and differentiators. After they're generated, you'll have the option to adjust them as needed for accuracy.")

    if "generate_insight_clicked" not in st.session_state:
        st.session_state.generate_insight_clicked = False

    if not st.session_state.insight_generated:
        if st.button("Generate", key="generate_product_insight", use_container_width=True):
            st.session_state.generate_insight_clicked = True

    if st.session_state.generate_insight_clicked:
        if not st.session_state.get("product_desc_confirmed", False):
            st.error("Enter your product description to generate product insight.")
        else:
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
