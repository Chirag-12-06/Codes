import pandas as pd
import random

# Load the original Excel file
input_file = "fool_data_d.xlsx"
df = pd.read_excel(input_file)

# Initialize an empty DataFrame to store the updated rows
updated_df = df.copy()

# Loop to add the new activities 4 times
for i in range(4):
    new_activities = [
        {"Activity": "Fig", "Value": round(random.uniform(100,500), 1), "Value_gen": round(random.uniform(5, 50), 1),"Value_op": round(random.uniform(1, 20), 1), "Type": "fat_gain"},
        {"Activity": "Fig", "Value": round(random.uniform(100,500), 1), "Value_gen": round(random.uniform(5, 50), 1),"Value_op": round(random.uniform(1, 20), 1), "Type": "muscle_gain"},
        {"Activity": "Fig", "Value": round(random.uniform(100,500), 1), "Value_gen": round(random.uniform(5, 50), 1),"Value_op": round(random.uniform(1, 20), 1), "Type": "fat_loss"},
    ]

    # Convert to DataFrame
    new_rows = pd.DataFrame(new_activities)

    # Append new rows to the existing dataset
    updated_df = pd.concat([updated_df, new_rows], ignore_index=True)

# Save to a new Excel file
output_file = "fool_data_f.xlsx"
updated_df.to_excel(output_file, index=False)

print(f"Updated dataset saved as: {output_file}")
