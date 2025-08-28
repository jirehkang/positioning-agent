import streamlit as st

def generate_clear_buttons(
    generate_callback,
    clear_callback,
    generate_key,
    clear_key,
):

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Generate", key=generate_key, use_container_width=True):
            generate_callback()
    with col2:
        if st.button("Clear", key=clear_key, use_container_width=True):
            clear_callback()