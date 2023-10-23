import csv

# Define the file path
file_path = 'C:/Users/jackb/OneDrive/Data Analyst/Projects/Python_Challenge/PyPoll/Resources/election_data.csv'

# variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read CSV file
with open(file_path, 'r') as csvfile:
    data = csv.reader(csvfile)
    
    # Skip the header row
    header = next(data)
    
    # for loop through the data
    for row in data:
        total_votes += 1
        candidate_name = row[2]
        
        # Check if the candidate is in the dictionary
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Determine the winner
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Calculate and print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")









