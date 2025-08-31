import streamlit as st
from components.text_box import editable_text_box
from generator import PositioningGenerator

if 'generator' not in st.session_state:
    st.session_state.generator = PositioningGenerator()
generator = st.session_state.generator

def render_prod_insight():
    st.markdown("<br>", unsafe_allow_html=True) 
    st.subheader("Step 2: Generate product insight")
    st.markdown("Turn your product description into product insights on market category, competitors, persona, and differentiators. You'll be able to make edits afterwards to improve clarity or add details.")

    if "generate_insight_clicked" not in st.session_state:
        st.session_state.generate_insight_clicked = False

    if not st.session_state.insight_generated:
        if st.button("Generate", key="generate_product_insight", use_container_width=True):
            if not st.session_state.get("product_desc_complete", False):
                st.error("Save your product description to generate product insight.")
            else:
                st.session_state.generate_insight_clicked = True
                st.rerun()

    if st.session_state.generate_insight_clicked and not st.session_state.insight_generated:
        if not st.session_state.get("product_desc_complete", False):
            st.error("Save your product description to generate product insight.")
        else:
            user_input = st.session_state.get("product_desc_text", "")
            with st.spinner("Generating product insight..."):
                st.session_state.category_text = generator.generate_category_overview(user_input)
                st.session_state.competitor_text = generator.generate_competitor_landscape(user_input)
                st.session_state.persona_text = generator.generate_target_persona(user_input)
                st.session_state.differentiators_text = generator.generate_unique_differentiators(user_input)

                st.session_state.insight_generated = True
                st.session_state.generate_insight_clicked = False

            # Show success message immediately after spinner finishes
            st.success("Insight generation complete. Scroll down to create your positioning statement!")
            st.session_state.product_insight_complete = {
                'category': True,
                'competitor': True,
                'persona': True,
                'differentiators': True
            }

    if st.session_state.get("insight_generated", False):
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

        if st.session_state.differentiators_text:
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
