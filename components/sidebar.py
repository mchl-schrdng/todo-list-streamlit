import streamlit as st
from utils.database import add_task, get_tasks, update_task_status, update_task_details, delete_task, reset_database
from utils.theme_manager import apply_theme

def render_sidebar():
    st.sidebar.write("### Navigation")
    col1, col2 = st.sidebar.columns(2)

    if col1.button("Task Manager"):
        st.session_state.menu = "Task Manager"
    if col2.button("Analytics"):
        st.session_state.menu = "Analytics"

    st.sidebar.markdown("---")

    st.sidebar.subheader("Add a New Task")
    with st.sidebar.form("task_form"):
        title = st.text_input("Task Title", placeholder="Enter your task title")
        tag = st.text_input("Tag", placeholder="One word (e.g., 'work', 'home')")
        urgency = st.slider("Urgency", 1, 5, 3)
        importance = st.slider("Importance", 1, 5, 3)
        submitted = st.form_submit_button("Add Task")
        if submitted and title:
            add_task(title, tag, urgency, importance)
            st.sidebar.success("Task added successfully!")
            st.rerun()

    st.sidebar.markdown("---")
    tasks = get_tasks()

    if tasks:
        st.sidebar.subheader("Update Existing Task")
        with st.sidebar.form("update_task_form"):
            task_id = st.selectbox(
                "Select Task ID to Update",
                [t["id"] for t in tasks],
                format_func=lambda x: f"Task {x}: {next(t['title'] for t in tasks if t['id'] == x)}",
            )
            selected_task = next(t for t in tasks if t["id"] == task_id)
            status = st.radio(
                "Status",
                options=["to do", "doing", "done"],
                index=["to do", "doing", "done"].index(selected_task["status"]),
                horizontal=True,
            )
            title = st.text_input("Title", value=selected_task["title"])
            tag = st.text_input("Tag", value=selected_task.get("tag", ""))
            urgency = st.slider("Urgency", 1, 5, selected_task["urgency"])
            importance = st.slider("Importance", 1, 5, selected_task["importance"])
            update_submitted = st.form_submit_button("Update Task")
            if update_submitted:
                update_task_status(task_id, status)
                update_task_details(task_id, title, tag, urgency, importance)
                st.sidebar.success(f"Task {task_id} updated successfully!")
                st.rerun()

        st.sidebar.markdown("---")

        st.sidebar.subheader("Delete a Task")
        task_id_to_delete = st.sidebar.selectbox(
            "Select Task ID to Delete",
            [t["id"] for t in tasks],
            format_func=lambda x: f"Task {x}: {next(t['title'] for t in tasks if t['id'] == x)}",
        )
        if st.sidebar.button("Delete Task"):
            delete_task(task_id_to_delete)
            st.sidebar.success(f"Task {task_id_to_delete} deleted successfully!")
            st.rerun()
    else:
        st.sidebar.write("No tasks available to manage.")

    st.sidebar.markdown("---")

    if st.sidebar.button("Reset Database"):
        reset_database()
        st.sidebar.success("Database has been reset!")
        st.rerun()

    st.sidebar.markdown("---")

    st.sidebar.subheader("Appearance")
    is_dark_mode = st.sidebar.toggle("Enable Dark Mode", value=False)

    apply_theme(is_dark_mode)