# -*- coding: utf-8 -*-
"""Agile_task.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lJZBIEcKnwqHIQojCOs3XP7IxhK7z96s
"""

import pandas as pd

# Read the two tables from CSV files
table1_path = "table1.csv"
table2_path = "table2.csv"
table1 = pd.read_csv(table1_path)
table2 = pd.read_csv(table2_path)

# Merge the two tables on the "User ID" column
merged_table = pd.merge(table1, table2, on="User ID")

# Group the merged table by team and calculate the average statements and reasons for each team
team_stats = merged_table.groupby("Team Name").agg({
    "total_statements": "mean",
    "total_reasons": "mean"
})

# Calculate the sum of average statements and reasons for each team
team_stats["sum_avg"] = team_stats["total_statements"] + team_stats["total_reasons"]
# Round the average values to 2 decimal places
team_stats = team_stats.round(2)

# Sort the team stats by the sum of average statements and reasons in descending order
team_stats = team_stats.sort_values(by="sum_avg", ascending=False)

# Reset the index of the team stats table
team_stats = team_stats.reset_index()

# Add a column for team rank
team_stats["Team Rank"] = team_stats.index + 1

# Format the table for display
team_stats = team_stats[["Team Rank", "Team Name", "total_statements", "total_reasons"]]
team_stats.columns = ["Team Rank", "Thinking Teams Leaderboard", "Average Statements", "Average Reasons"]

# Print the table
print("Here's the leaderboard (team-wise). The rank is decided on the basis of sum of average statements and reasons.")
print()
print(team_stats.to_string(index=False))

import pandas as pd

# Read the input tables from csv files
table1 = pd.read_csv('table1.csv')
table2 = pd.read_csv('table2.csv')

# Merge the two tables based on 'uid' column
merged_table = pd.merge(table1, table2, on='User ID')

# Sort the merged table by 'total_statements' and 'total_reasons' in descending order
sorted_table = merged_table.sort_values(['total_statements', 'total_reasons'], ascending=[False, False])

# Add a new column for ranking based on the sorted table
sorted_table['Rank'] = sorted_table['total_statements'].rank(method='min', ascending=False)

# Display the output table with required columns and format
output_table = sorted_table[['Rank', 'name', 'User ID', 'total_statements', 'total_reasons']]

print(output_table.to_string(index=False))