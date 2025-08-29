import streamlit as st

def text_box_start_unsaved(
    saved_content,
    placeholder,
    session_text_key: str,
    session_edit_key: str,
    area_label: str,
):

    if session_edit_key not in st.session_state:
        st.session_state[session_edit_key] = True
    if session_text_key not in st.session_state:
        st.session_state[session_text_key] = saved_content

    if st.session_state[session_edit_key]:
        # Editable mode
        edited_text = st.text_area(area_label, value=st.session_state[session_text_key], key=f"{session_text_key}_input", placeholder=placeholder, height=130)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save", use_container_width=True, key=f"save_{session_text_key}"):
                st.session_state[session_text_key] = edited_text
                st.session_state[session_edit_key] = False
                st.session_state[f"{session_text_key}_show_success"] = True
                st.rerun()
            
        with col2:
            if st.button("Cancel", use_container_width=True, key=f"cancel_{session_text_key}"):
                st.session_state[session_edit_key] = False
                input_key = f"{session_text_key}_input"
                if input_key in st.session_state:
                    del st.session_state[input_key]
                st.rerun()
        

    else:
        # Read-only mode

        st.markdown(f"{st.session_state[session_text_key]}")
        if st.button("Edit", use_container_width=True, key=f"edit_{session_text_key}"):
            st.session_state[session_edit_key] = True
            st.rerun()

        if st.session_state.get(f"{session_text_key}_show_success"):
            st.success("Description saved! Now click Generate Product Insight.")
            del st.session_state[f"{session_text_key}_show_success"]


def text_box_start_saved(
    saved_content,
    session_text_key: str,
    session_edit_key: str,
    area_label: str,
):
    
    if session_edit_key not in st.session_state:
        st.session_state[session_edit_key] = False
    if session_text_key not in st.session_state:
        st.session_state[session_text_key] = saved_content

    if st.session_state[session_edit_key]:
        # Editable mode
        edited_text = st.text_area(area_label, value=st.session_state[session_text_key], key=f"{session_text_key}_input", height=200)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save", use_container_width=True, key=f"save_{session_text_key}"):
                st.session_state[session_text_key] = edited_text
                st.session_state[session_edit_key] = False
                st.success("Changes saved.")
                st.rerun()
        with col2:
            if st.button("Cancel", use_container_width=True, key=f"cancel_{session_text_key}"):
                st.session_state[session_edit_key] = False
                input_key = f"{session_text_key}_input"
                if input_key in st.session_state:
                    del st.session_state[input_key]
                st.rerun()
    else:
        # Read-only mode
        st.text_area(
            area_label,
            value=st.session_state[session_text_key],
            key=f"{session_text_key}_readonly",
            height=200,
            disabled=True
        )
        if st.button("Edit", use_container_width=True, key=f"edit_{session_text_key}"):
            st.session_state[session_edit_key] = True
            st.rerun()