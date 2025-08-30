import streamlit as st

def render_progress_tracker():
    with st.sidebar.container():

        st.markdown("<br><br>", unsafe_allow_html=True) 

        st.markdown("### 📊 Your Progress")

        step1_status = "✅" if st.session_state.product_desc_confirmed else "⬜"
        st.markdown(f"{step1_status} Step 1: Describe your product")

        step2_complete = all(st.session_state.insight_steps_done.values())
        step2_status = "✅" if step2_complete else "⬜"
        st.markdown(f"{step2_status} Step 2: Generate product insight")

        step3_status = "✅" if st.session_state.positioning_done else "⬜"
        st.markdown(f"{step3_status} Step 3: Generate positioning statement")