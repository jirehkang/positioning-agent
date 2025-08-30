import streamlit as st

def editable_text_box(
    saved_content,
    session_text_key: str,
    session_edit_key: str,
    session_status_confirmed: str,
    area_label: str,
    success_message: str,
    default_edit_mode=False,
    height: int=120,
    placeholder: str=""
):

    if session_edit_key not in st.session_state:
        st.session_state[session_edit_key] = default_edit_mode
    if session_text_key not in st.session_state:
        st.session_state[session_text_key] = saved_content

    if st.session_state[session_edit_key]:
        # Editable mode
        edited_text = st.text_area(area_label, value=st.session_state[session_text_key], key=f"{session_text_key}_input", placeholder=placeholder, height=height)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save", use_container_width=True, key=f"save_{session_text_key}"):
                if edited_text.strip() == "":
                    st.error("Enter some text before saving.")
                else:
                    st.session_state[session_status_confirmed] = True
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
            st.success(success_message)
            del st.session_state[f"{session_text_key}_show_success"]
