# SQLServer-Visualization-Project

## Project Overview
This project aims to create an interactive web application that allows users to explore and visualize data stored in a SQL Server database. The application is designed to list tables, execute specific queries, and display both data and corresponding graphs in a visually appealing and intuitive manner using modern data visualization libraries.

## Features
- **Table Listing:** Users can view and select tables available in the SQL Server database from a dropdown menu.
- **Data Retrieval:** Execute SQL queries to retrieve and display the first records from the selected table.
- **Data Visualization:** Generate interactive and modern graphs based on the retrieved data.
- **User Interface:** A responsive and visually appealing UI built using Tailwind CSS.
- **Backend:** A Python-based backend using Flask to manage database connections and serve the web interface.

## Requirements
- SQL Server (with the AdventureWorks database installed)
- Python 3.x
- Required Python packages: `pandas`, `matplotlib`, `pyodbc`, `Flask`, `Tailwind CSS`

## Getting Started
1. Clone the repository:
    ```bash
    git clone git@github.com:beloureiro/SQLServer-Visualization-Project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd SQLServer-Visualization-Project
    ```
3. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # On Windows
    # or
    source venv/bin/activate  # On macOS/Linux
    pip install -r requirements.txt
    ```

## Usage
1. **Run the Web Application:**
    ```bash
    cd project_root
    python app.py
    ```
    Open your browser and navigate to `http://127.0.0.1:5000` to access the application.

2. **Select a Schema and Table:**
    - Use the dropdown menus to select a schema and a table.
    - Click "Ver" to display the data and corresponding graph.

## Project Structure
- **`app.py`**: Manages the web application, handles routes, and integrates the frontend with the backend.
- **`data_queries.py`**: Contains functions for querying the SQL Server database.
- **`visualize_data.py`**: Handles the creation of data visualizations using Matplotlib.
- **`static/`**: Contains static files like the generated plots.
- **`templates/`**: Contains HTML templates for rendering the web pages.

## Technologies Used
- **SQL Server**: For data storage and management.
- **Python**: For backend logic, database interaction, and data manipulation.
- **Flask**: As the web framework for serving the application.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.
- **Tailwind CSS**: For the responsive and modern user interface design.
- **HTML/CSS/JavaScript**: For creating the user interface and improving interactivity.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
