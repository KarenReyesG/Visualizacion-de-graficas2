import pandas as pd
import matplotlib.pyplot as plt

# Define the dataset (replace with your actual data source if needed)
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje',
                'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje',
                'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Apply a visual style (optional)
plt.style.use('fivethirtyeight')

# --- Boxplot for Distribution of Notes ---

# Fix the warning: use 'tick_labels' instead of 'labels'
plt.boxplot(
    [df[df['materia'] == materia]['nota'] for materia in df['materia'].unique()],
    tick_labels=df['materia'].unique(),  # Use 'tick_labels' for Matplotlib >= 3.9
    medianprops={'color': 'orange'}
)
plt.title('Distribución de Notas')
plt.ylabel('Nota')
plt.grid(True)

# Save the boxplot figure
plt.savefig('distribucion_notas_boxplot.png', bbox_inches='tight')  # Save with proper bounding box

# Clear the plot (optional)
plt.clf()  # Clear the plot to avoid overlapping plots

# --- Pie Chart for Distribution of Aprobados ---

# Calculate student counts
aprobados = df[df['aprobado'] == 'Sí'].shape[0]
no_aprobados = df[df['aprobado'] == 'No'].shape[0]

# Prepare pie chart data
sizes = [aprobados, no_aprobados]
labels = ['Aprobados', 'No Aprobados']
colors = ['blue', 'orange']  # Colors for segments

# Create the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Aprobados')

# Save the pie chart figure
plt.savefig('distribucionaprobados_piechart.png', bbox_inches='tight')  # Save with proper bounding box

# Show the pie chart
plt.show()