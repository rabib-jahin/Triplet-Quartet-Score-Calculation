# Function to extract the triplet scores from a given line
def extract_triplet_score(line):
    prefix = "Triplet score:"
    if prefix in line:
        return int(line.split(prefix)[1])

# File path
file_path = "out2.txt"

# List to store the triplet scores
triplet_scores = []

# Read the file line by line and extract triplet scores
with open(file_path, "r") as file:
    for line in file:
        score = extract_triplet_score(line.strip())
        if score is not None:
            triplet_scores.append(score)

# Find the minimum and maximum triplet scores
if triplet_scores:
    min_triplet_score = min(triplet_scores)
    max_triplet_score = max(triplet_scores)
    print("Triplet Scores:", triplet_scores)
    print("Minimum Triplet Score:", min_triplet_score)
    print("Maximum Triplet Score:", max_triplet_score)
else:
    print("No triplet scores found in the file.")

