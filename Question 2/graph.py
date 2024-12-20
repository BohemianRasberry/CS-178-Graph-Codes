import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file into a pandas DataFrame
# Replace 'your_file.csv' with your actual file path
df = pd.read_csv('bquxjob_75bf7c25_193e1bb4c43.csv')

# Step 2: Sort the data based on population_decline in descending order
df_sorted = df.sort_values('population_decline', ascending=False)

# Step 3: Create a horizontal bar plot for population decline
plt.figure(figsize=(10, 6))  # Adjust the size if needed
plt.barh(df_sorted['province'], df_sorted['population_decline'], color='lightcoral')

# Step 4: Customize the plot
plt.xlabel('Population Decline')
plt.ylabel('Provinces')
plt.title('Bird Population Decline by Province')
plt.tight_layout()  # Adjust layout for better spacing

# Step 5: Show the plot
plt.show()
