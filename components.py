import streamlit as st

def generate_clear_buttons(
    generate_callback,
    clear_callback,
    generate_key,
    clear_key,
    success_flag_key=None,
):

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Generate", key=generate_key, use_container_width=True):
            generate_callback()
            if success_flag_key:
                st.session_state[success_flag_key] = True
    with col2:
        if st.button("Clear", key=clear_key, use_container_width=True):
            clear_callback()

    if success_flag_key and st.session_state.get(success_flag_key, False):
        st.success("✅ Generated successfully!")
        del st.session_state[success_flag_key]