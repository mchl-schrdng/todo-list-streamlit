import streamlit as st
import plotly.express as px
from datetime import datetime
from collections import defaultdict
from utils.plotly_utils import apply_transparent_layout

def display_analytics(tasks):
    if not tasks:
        st.write("No tasks available for analytics.")
        return

    task_status_counts = defaultdict(int)
    time_series_data = defaultdict(int)
    urgency_trends = defaultdict(list)
    importance_trends = defaultdict(list)
    status_over_time = defaultdict(lambda: defaultdict(int))

    for task in tasks:
        created_date = datetime.strptime(task["created_at"], "%Y-%m-%d").date()
        task_status_counts[task["status"]] += 1
        time_series_data[created_date] += 1
        urgency_trends[created_date].append(task["urgency"])
        importance_trends[created_date].append(task["importance"])
        status_over_time[created_date][task["status"]] += 1

    urgency_avg = {date: sum(values) / len(values) for date, values in urgency_trends.items()}
    importance_avg = {date: sum(values) / len(values) for date, values in importance_trends.items()}

    sorted_time_series = sorted(time_series_data.items())
    sorted_urgency = sorted(urgency_avg.items())
    sorted_importance = sorted(importance_avg.items())

    status_data = []
    for date, statuses in status_over_time.items():
        for s, count in statuses.items():
            status_data.append({"Date": date, "Status": s, "Count": count})

    dates, task_counts = zip(*sorted_time_series) if sorted_time_series else ([], [])
    urgency_dates, urgency_values = zip(*sorted_urgency) if sorted_urgency else ([], [])
    importance_dates, importance_values = zip(*sorted_importance) if sorted_importance else ([], [])

    pie_chart = px.pie(
        names=list(task_status_counts.keys()),
        values=list(task_status_counts.values()),
        title="Task Distribution by Status",
        hole=0.4,
    )
    pie_chart = apply_transparent_layout(pie_chart)

    time_series_chart = px.line(
        x=dates,
        y=task_counts,
        labels={"x": "Date", "y": "Number of Tasks"},
        title="Tasks Created Over Time",
    )
    time_series_chart = apply_transparent_layout(time_series_chart)
    time_series_chart.update_xaxes(type="date", tickformat="%b %d, %Y")

    combined_x = list(urgency_dates) + list(importance_dates)
    combined_y = list(urgency_values) + list(importance_values)
    combined_color = ["Urgency"] * len(urgency_dates) + ["Importance"] * len(importance_dates)

    trend_chart = px.line(
        x=combined_x,
        y=combined_y,
        color=combined_color,
        labels={"x": "Date", "y": "Average Value", "color": "Metric"},
        title="Urgency and Importance Trends Over Time",
    )
    trend_chart = apply_transparent_layout(trend_chart)
    trend_chart.update_xaxes(type="date", tickformat="%b %d, %Y")

    status_chart = px.bar(
        status_data,
        x="Date",
        y="Count",
        color="Status",
        barmode="stack",
        labels={"Date": "Date", "Count": "Task Count", "Status": "Task Status"},
        title="Task Distribution by Status Over Time",
    )
    status_chart = apply_transparent_layout(status_chart)
    status_chart.update_xaxes(type="date", tickformat="%b %d, %Y")

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(pie_chart, use_container_width=True)
        st.plotly_chart(trend_chart, use_container_width=True)
    with col2:
        st.plotly_chart(time_series_chart, use_container_width=True)
        st.plotly_chart(status_chart, use_container_width=True)