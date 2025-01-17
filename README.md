# Todooolist

**Todooolist** is a Streamlit-based task management application that helps you prioritize and manage your tasks effectively. It features a simple interface for managing tasks, tracking analytics, and visualizing trends in urgency and importance.

---

## Features

- **Task Management**: Add, update, delete, and manage tasks with custom fields like urgency and importance.
- **Analytics Dashboard**: Gain insights into your task distribution, trends in urgency/importance, and task creation over time.
- **Prioritization**: View tasks based on the Eisenhower matrix using urgency and importance ratings.
- **Customizable Appearance**: Toggle between light and dark modes for a personalized look.

---

## Directory Structure

```plaintext
└── mchl-schrdng-todo-list-streamlit/
    ├── app.py
    ├── requirements.txt
    ├── components/
    │   ├── analytics.py
    │   ├── sidebar.py
    │   └── task_display.py
    └── utils/
        ├── database.py
        ├── plotly_utils.py
        └── theme_manager.py
```

## Key Files
- app.py: Main application file that initializes the app, manages routing, and sets up the layout.
- requirements.txt: Contains the dependencies required to run the application.
- components/: Modular components for analytics, sidebar, and task display.
- utils/: Utility scripts for database operations, plot customization, and theme management.

## Installation

Clone the repository:
```bash
git clone https://github.com/mchl-schrdng/mchl-schrdng-todo-list-streamlit.git
cd mchl-schrdng-todo-list-streamlit
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
streamlit run app.py
```

## Usage

Navigation
- Task Manager: Manage your tasks by adding, updating, or deleting them via the sidebar.
- Analytics: Visualize your task data using pie charts, line graphs, and bar charts.

Adding Tasks
- Fill in the task title, tag, urgency, and importance from the sidebar.
- Submit the form to add a new task.

Updating Tasks
- Select a task from the dropdown in the sidebar to update its details.

Deleting Tasks
- Use the delete option in the sidebar to remove unwanted tasks.

## Visualization

The analytics dashboard includes:
- Pie Chart: Task distribution by status.
- Line Graphs: Trends in urgency and importance over time.
- Bar Chart: Task distribution by status over time.

## Dependencies
- Streamlit: Web application framework.
- Plotly: For interactive visualizations.

Install all dependencies via the provided requirements.txt file.

## Customization

Appearance
Toggle between light and dark modes using the Appearance section in the sidebar.

Database Reset
Reset the task database via the Reset Database button in the sidebar.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork the repository and create a pull request for any features or bug fixes. All contributions are welcome!
