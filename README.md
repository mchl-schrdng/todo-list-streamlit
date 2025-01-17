# Todooolist

**Todooolist** is a Streamlit-based task management application that helps you prioritize and manage your tasks effectively. It features a simple interface for managing tasks, tracking analytics, and visualizing trends in urgency and importance.

<img src="https://github.com/user-attachments/assets/b10bcc81-f439-45c1-bbc6-26e56e6005b8" alt="First Image" width="900">
<img src="https://github.com/user-attachments/assets/b99f4830-72c2-4fac-a071-4ce02beb74c6" alt="Second Image" width="900">


---

## Features
- **Task Management**: Add, update, delete, and manage tasks with custom fields like urgency and importance.
- **Analytics Dashboard**: Gain insights into your task distribution, trends in urgency/importance, and task creation over time.
- **Prioritization**: View tasks based on the Eisenhower matrix using urgency and importance ratings.
- **Customizable Appearance**: Toggle between light and dark modes for a personalized look.

---

### Key Files
- **`app.py`**: Main application file for initializing and running the app.
- **`requirements.txt`**: List of required Python packages.
- **`components/`**: Modular components for analytics, sidebar, and task display.
- **`utils/`**: Scripts for database operations, plot customization, and theme management.

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mchl-schrdng/mchl-schrdng-todo-list-streamlit.git
    cd mchl-schrdng-todo-list-streamlit
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

---

## Usage

### Navigation
- **Task Manager**: Add, update, or delete tasks using the sidebar.
- **Analytics**: Visualize task data through charts and graphs.

### Adding Tasks
- Use the form in the sidebar to enter task details like title, tag, urgency, and importance.
- Submit the form to create a new task.

### Updating Tasks
- Select a task from the dropdown menu in the sidebar to edit its details.

### Deleting Tasks
- Choose a task from the sidebar and delete it with one click.

---

## Visualization

The analytics dashboard includes:
- **Pie Chart**: Displays task distribution by status.
- **Line Graphs**: Tracks trends in urgency and importance over time.
- **Bar Chart**: Shows task distribution by status over time.

---

## Dependencies

- **Streamlit**: Web application framework.
- **Plotly**: For creating interactive visualizations.

Install dependencies using the provided `requirements.txt` file.

---

## Customization

- **Appearance**: Toggle light or dark mode in the sidebar.
- **Database Reset**: Reset all tasks using the "Reset Database" button.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions are welcome! Fork the repository and create a pull request for any features or fixes.

