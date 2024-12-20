import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file into a pandas DataFrame
# Make sure to replace 'your_file.csv' with the actual CSV file path
df = pd.read_csv('bquxjob_1c529f12_193e1a10e3d.csv')

# Step 2: Get unique species from the 'species' column
species_list = df['species'].unique()

for species in species_list:
    print(species)

'''

# Step 3: Loop through each species and generate a bar graph
for species in species_list:
    # Filter the data for the current species
    species_data = df[df['species'] == species]
    
    # Create a bar plot for the species
    plt.figure(figsize=(10, 6))  # Adjust size if needed
    plt.bar(species_data['province'], species_data['occurrences_in_province_2023'], color='skyblue')
    
    # Customize the plot
    plt.xlabel('Provinces')
    plt.ylabel('Occurrences in 2023')
    plt.title(f'Ocurrences of {species} by Province in 2023')
    plt.xticks(rotation=90)  # Rotate the x-axis labels for readability
    plt.tight_layout()  # Adjust the layout for better spacing
    
    # Step 4: Show the plot for the current species
    plt.show()
'''