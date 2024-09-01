from flask import Flask, render_template, request, jsonify
from data_queries import get_schemas_and_tables, get_data
from visualize_data import plot_data  # Importa a função plot_data
import os

app = Flask(__name__)

# Variável global para armazenar schemas_and_tables
schemas_and_tables = get_schemas_and_tables()

@app.route('/')
def index():
    global schemas_and_tables
    schemas = schemas_and_tables['TABLE_SCHEMA'].unique().tolist()
    return render_template('index.html', schemas=schemas)

@app.route('/get_tables', methods=['POST'])
def get_tables():
    schema_name = request.form['schema_name']
    tables = schemas_and_tables[schemas_and_tables['TABLE_SCHEMA'] == schema_name]['TABLE_NAME'].tolist()
    return jsonify(tables)

@app.route('/view', methods=['POST'])
def view_data():
    global schemas_and_tables
    schemas = schemas_and_tables['TABLE_SCHEMA'].unique().tolist()
    schema_name = request.form['schema_name']
    table_name = request.form['table_name']
    
    data = get_data(schema_name, table_name)
    
    # Verifique se os dados não estão vazios
    if data.empty:
        return render_template('index.html', schemas=schemas, data=None, error="No data available for the selected table.")
    
    # Gera o gráfico usando a função plot_data
    image_path = os.path.join('static', 'plot.png')
    plot_data(data, image_path)

    return render_template('index.html', schemas=schemas, data=data, image_file=image_path)

if __name__ == '__main__':
    app.run(debug=True)
