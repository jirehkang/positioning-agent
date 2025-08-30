import streamlit as st
from components.text_box import editable_text_box

def render_prod_desc():
    st.subheader("Step 1. Describe your product")
    st.markdown("For best results, include your product name, key features, and problems you're solving.")
    editable_text_box(
        saved_content="",
        placeholder="Slack is where teams talk, share files, and connect their tools...", 
        session_text_key="saved_text",
        session_edit_key="editing",
        session_status_confirmed="product_desc_confirmed",
        area_label="product_desc",
        default_edit_mode=True,
        label_visibility="collapsed",
        success_message="Changes saved. You can now generate product insight!"
    )