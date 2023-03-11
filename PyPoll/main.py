import os
import csv

# Set path for file
election_data_csv = os.path.join(".", "Resources", "election_data.csv")

#  List of stored data
Vote_Count = []
Can1_Votes = []
Can2_Votes = []
Can3_Votes = []

# Establishing variables so this can be updated with user input in the future
Candidate1 = "Charles Casper Stockham"
Candidate2 = "Diana DeGette"
Candidate3 = "Raymon Anthony Doane"

# Establishing a variable to help calculate votes from the csv file
Total_votes = 0


# with open(budget_data_csv, encoding='utf-8') as csvfile:

with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # Skips the Header row
    next(csvreader)
    
    for row in csvreader:
        # Adds the vote count for each row
        Vote_Count.append(row[0])

        # if conditional check to allocate votes for each candidate based on the row
        if row[2] == Candidate1:
            Can1_Votes.append(row[0]) 

        elif row[2] == Candidate2:
            Can2_Votes.append(row[0])
        
        elif row[2] == Candidate3:
            Can3_Votes.append(row[0])


# Counts the number of values in each list
Total_vote = (len(Vote_Count))
Can1_count = (len(Can1_Votes))
Can2_count = (len(Can2_Votes))
Can3_count = (len(Can3_Votes))


# Calcualtes the percentage of vote each candidate received
Can1_Percent = Can1_count/Total_vote
Can2_Percent = Can2_count/Total_vote
Can3_Percent = Can3_count/Total_vote


# Prints the outputs from module to the screen
print("\n")
print("Election Results\n")
print("------------------------------------------\n")
print(f"Total Votes: {Total_vote}\n")
print("------------------------------------------\n")
print(f"{Candidate1}: {Can1_Percent:.3%} ({Can1_count})\n")
print(f"{Candidate2}: {Can2_Percent:.3%} ({Can2_count})\n")
print(f"{Candidate3}: {Can3_Percent:.3%} ({Can3_count})\n")
print("------------------------------------------\n")

# Applies 'if and' conditional to identify the winner and print it to the screen
if Can1_Percent > Can2_Percent and Can1_Percent > Can3_Percent:
    print(f"Winner: {Candidate1}\n")

elif Can2_Percent > Can1_Percent and Can2_Percent > Can3_Percent:
    print(f"Winner: {Candidate2}\n")

elif Can3_Percent > Can1_Percent and Can3_Percent > Can2_Percent:
    print(f"Winner: {Candidate3}\n")
print("------------------------------------------\n")


# Sets the output file path
output_file = os.path.join(".", "analysis","analysis.txt")


# Writes the outputs from script to a txt file
with open(output_file, "w") as datafile:
    datafile.writelines("\n")
    datafile.writelines("Election Results\n")
    datafile.writelines("\n")
    datafile.writelines("------------------------------------------\n")
    datafile.writelines("\n")
    datafile.writelines(f"Total Votes: {Total_vote}\n")
    datafile.writelines("\n")
    datafile.writelines("------------------------------------------\n")
    datafile.writelines("\n")
    datafile.writelines(f"{Candidate1}: {Can1_Percent:.3%} ({Can1_count})\n")
    datafile.writelines("\n")
    datafile.writelines(f"{Candidate2}: {Can2_Percent:.3%} ({Can2_count})\n")
    datafile.writelines("\n")
    datafile.writelines(f"{Candidate3}: {Can3_Percent:.3%} ({Can3_count})\n")
    datafile.writelines("\n")
    datafile.writelines("------------------------------------------\n")
    datafile.writelines("\n")

    # Applies 'if and' conditional to identify the winner and writes it to the txt file
    if Can1_Percent > Can2_Percent and Can1_Percent > Can3_Percent:
        datafile.writelines(f"Winner: {Candidate1}\n")

    elif Can2_Percent > Can1_Percent and Can2_Percent > Can3_Percent:
        datafile.writelines(f"Winner: {Candidate2}\n")

    elif Can3_Percent > Can1_Percent and Can3_Percent > Can2_Percent:
        datafile.writelines(f"Winner: {Candidate3}\n")
    datafile.writelines("\n")
    datafile.writelines("------------------------------------------\n")
    datafile.writelines("\n")
    
    
