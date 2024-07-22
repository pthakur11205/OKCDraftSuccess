import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
df = pd.read_csv('combined_draft_data_with_zScore.csv')

# Convert columns to appropriate data types if necessary
success_counts = df.groupby(['Team', 'Successful Pick']).size().unstack(fill_value=0)

# Calculate percentage of successful picks
success_counts['Success Rate %'] = success_counts[True] / (success_counts[True] + success_counts[False]) * 100

# Plot histogram
plt.figure(figsize=(14, 8))
success_counts['Success Rate %'].plot(kind='bar', stacked=False)
plt.xlabel('Teams (Abbreviations)')
plt.ylabel('Successful Pick Percentage (%)')
plt.title('Successful Pick Percentage by Teams since 1989 (Z-Score method)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the graph as a PNG file
plt.savefig('successful_pick_percentage_zScore.png')

# Show the plot
plt.show()
