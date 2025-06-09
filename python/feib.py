from itertools import combinations
import numpy as np

# Input list of 15 CGPAs
cgpas = [6.7, 7.56, 7.88,
         9.86, 9.62, 9.34, 9.17,
         8.1, 8.37, 8, 7.99,
         9, 8.88, 8.61, 8.57]

# Desired group sizes (must sum to 15)
group_sizes = [3, 4, 4, 4]

# Function to generate all valid groupings given size constraints
def generate_groupings(elements, sizes):
    if not sizes:
        return [[]] if not elements else []
    results = []
    for group in combinations(elements, sizes[0]):
        remaining = list(elements)
        for g in group:
            remaining.remove(g)
        for rest in generate_groupings(remaining, sizes[1:]):
            results.append([list(group)] + rest)
    return results

# Generate all valid groupings
print("Generating groupings... (this may take a few minutes)")
groupings = generate_groupings(cgpas, group_sizes)

# Find the best grouping: minimal spread between group averages
best_spread = float('inf')
best_avg = 0
best_grouping = None

for groups in groupings:
    avgs = [np.mean(g) for g in groups]
    spread = max(avgs) - min(avgs)
    overall_avg = np.mean(avgs)
    if spread < best_spread or (spread == best_spread and overall_avg > best_avg):
        best_spread = spread
        best_avg = overall_avg
        best_grouping = groups

# Print the best grouping and their averages
print("\nBest Grouping (spread minimized, averages close):")
for i, group in enumerate(best_grouping, 1):
    print(f"Group {i}: {group} → Average: {round(np.mean(group), 4)}")

print(f"\nSpread: {round(best_spread, 4)}")
print(f"Average of Group Averages: {round(best_avg, 4)}")
