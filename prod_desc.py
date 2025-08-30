import streamlit as st
from components.text_box import editable_text_box

def render_prod_desc():
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