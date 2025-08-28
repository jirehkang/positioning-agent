import streamlit as st
from agent import PositioningAgent
from components import generate_clear_buttons

if 'agent' not in st.session_state:
    st.session_state.agent = PositioningAgent()

# Session state for progress tracking
if 'product_desc_confirmed' not in st.session_state:
    st.session_state.product_desc_confirmed = False
if 'insight_steps_done' not in st.session_state:
    st.session_state.insight_steps_done = {'category': False, 'competitor': False, 'persona': False, 'differentiators': False}
if 'positioning_done' not in st.session_state:
    st.session_state.positioning_done = False

agent = st.session_state.agent
st.set_page_config(layout="wide")

left_col, right_col = st.columns([1, 3])

with left_col:

    st.title("Positioning Statement Generator")
    st.markdown('''

            ''')
    st.markdown("#### 📊 Your Progress")

    step1_status = "✅" if st.session_state.product_desc_confirmed else "⬜"
    st.markdown(f"{step1_status} Step 1: Enter product description")

    step2_complete = all(st.session_state.insight_steps_done.values())
    step2_status = "✅" if step2_complete else "⬜"
    st.markdown(f"{step2_status} Step 2: Define product insights")

    step3_status = "✅" if st.session_state.positioning_done else "⬜"
    st.markdown(f"{step3_status} Step 3: Generate positioning statement")


with right_col:
    
    # product description
    st.subheader("Step 1: Enter product description")
    
    user_input = st.text_area(
        label="Include product name, key features, and problems you're solving. Aim to keep it concise: 1-2 sentences at max.",
        value=st.session_state.get("user_input", ""),
        placeholder="Slack is where teams talk, share files, and connect their tools..."
    )

    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Confirm", use_container_width=True):
            st.session_state.product_desc_confirmed = True
            st.session_state.user_input = user_input
            st.session_state.show_confirm_success = True 
            st.rerun()
    with col2:    
        if st.button("Clear", key="clear_product_description", use_container_width=True):
            del st.session_state.product_desc_confirmed
            st.session_state.user_input = ""
            st.rerun()

    if st.session_state.get("show_confirm_success", False): 
        st.success("✅ Product description confirmed! You can now define your product insights.") 
        del st.session_state.show_confirm_success 


    # product insights

    st.markdown("""
                """)
    st.subheader("Step 2: Define product insights")

    # category overview

    st.markdown("##### Category Overview")
    st.text_area("Write your product category or click the generate button", value=getattr(agent, 'category_output', ''), height=200)

    generate_clear_buttons(
        generate_callback=lambda: (
            st.warning("Please enter and confirm your product description first.") if not user_input.strip() else (
                setattr(agent, "category_output", agent.generate_category_overview(user_input)),
                st.session_state.insight_steps_done.update({"category": True}),
                st.rerun()
            )
        ),
        clear_callback=lambda: (
            setattr(agent, "category_output", ""),
            st.session_state.insight_steps_done.update({"category": False}),
            st.rerun()
        ),
        generate_key="category_generate_btn",
        clear_key="category_clear_btn",
        success_flag_key="category_success"
    )

    # competitor landscape

    st.markdown("##### Competitor Landscape")
    st.text_area("Write your competitor landscape or click the generate button", value=getattr(agent, 'competitor_landscape', ''), height=200)

    generate_clear_buttons(
        generate_callback=lambda: (
            st.warning("Please enter and confirm your product description first.") if not user_input.strip() else (
                setattr(agent, "competitor_landscape", agent.generate_competitor_landscape(user_input)),
                st.session_state.insight_steps_done.update({"competitor": True}),
                st.rerun()
            )
        ),
        clear_callback=lambda: (
            setattr(agent, "competitor_landscape", ""),
            st.session_state.insight_steps_done.update({"competitor": False}),
            st.rerun()
        ),
        generate_key="competitor_generate_btn",
        clear_key="competitor_clear_btn",
        success_flag_key="competitor_success"
    )

    # target persona   

    st.markdown("##### Target Persona")
    st.text_area("Write target or click generate", value=getattr(agent, 'target_persona', ''), height=200)

    generate_clear_buttons(
        generate_callback=lambda: (
            st.warning("Please enter and confirm your product description first.") if not user_input.strip() else (
                setattr(agent, "target_persona", agent.generate_target_persona(user_input)),
                st.session_state.insight_steps_done.update({"persona": True}),
                st.rerun()
            )
        ),
        clear_callback=lambda: (
            setattr(agent, "target_persona", ""),
            st.session_state.insight_steps_done.update({"persona": False}),
            st.rerun()
        ),
        generate_key="persona_generate_btn",
        clear_key="persona_clear_btn",
        success_flag_key="persona_success"
    )

    # unique differentiators 

    st.markdown("##### Unique Differentiators")
    st.text_area("Write differentiators or click generate", value=getattr(agent, 'unique_differentiators', ''), height=200)

    generate_clear_buttons(
        generate_callback=lambda: (
            st.warning("Please enter and confirm your product description first.") if not user_input.strip() else (
                setattr(agent, "unique_differentiators", agent.generate_unique_differentiators(user_input)),
                st.session_state.insight_steps_done.update({"differentiators": True}),
                st.rerun()
            )
        ),
        clear_callback=lambda: (
            setattr(agent, "unique_differentiators", ""),
            st.session_state.insight_steps_done.update({"differentiators": False}),
            st.rerun()
        ),
        generate_key="differentiators_generate_btn",
        clear_key="differentiators_clear_btn",
        success_flag_key="differentiators_success"
    )

    # Final positioning 

    st.markdown("""
                """)
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