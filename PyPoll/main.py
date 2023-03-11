import os
import csv

# Set path for file
election_data_csv = os.path.join(".", "Resources", "election_data.csv")

#  List of stored data
Vote_Count = []
CCS_Votes = []
DG_Votes = []
RAD_Votes = []

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
        if row[2] == "Charles Casper Stockham":
            CCS_Votes.append(row[0]) 

        elif row[2] == "Diana DeGette":
            DG_Votes.append(row[0])
        
        elif row[2] == "Raymon Anthony Doane":
            RAD_Votes.append(row[0])


# Counts the number of values in each list
Total_vote = (len(Vote_Count))
CCS_count = (len(CCS_Votes))
DG_count = (len(DG_Votes))
RAD_count = (len(RAD_Votes))


# Calcualtes the percentage of vote each candidate received
CCS_Percent = CCS_count/Total_vote
DG_Percent = DG_count/Total_vote
RAD_Percent = RAD_count/Total_vote


# Prints the outputs from module to the screen
print("\n")
print("Election Results\n")
print("------------------------------------------\n")
print(f"Total Votes: {Total_vote}\n")
print("------------------------------------------\n")
print(f"Charles Casper Stockham: {CCS_Percent:.3%} ({CCS_count})\n")
print(f"Diana Degette: {DG_Percent:.3%} ({DG_count})\n")
print(f"Raymon Anthony Doane {RAD_Percent:.3%} ({RAD_count})\n")
print("------------------------------------------\n")

# Applies 'if and' conditional to identify the winner and print it to the screen
if CCS_Percent > DG_Percent and CCS_Percent > RAD_Percent:
    print("Winner: Charles Casper Stockham\n")

elif DG_Percent > CCS_Percent and DG_Percent > RAD_Percent:
    print("Winner: Diana Degette\n")

elif RAD_Percent > CCS_Percent and RAD_Percent > DG_Percent:
    print("Winner: Raymon Anthony Doane\n")
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
    datafile.writelines(f"Charles Casper Stockham: {CCS_Percent:.3%} ({CCS_count})\n")
    datafile.writelines("\n")
    datafile.writelines(f"Diana DeGette: {DG_Percent:.3%} ({DG_count})\n")
    datafile.writelines("\n")
    datafile.writelines(f"Raymon Anthony Doane: {RAD_Percent:.3%} ({RAD_count})\n")
    datafile.writelines("\n")
    datafile.writelines("------------------------------------------\n")
    datafile.writelines("\n")

    # Applies 'if and' conditional to identify the winner and writes it to the txt file
    if CCS_Percent > DG_Percent and CCS_Percent > RAD_Percent:
        datafile.writelines("Winner: Charles Casper Stockham\n")

    elif DG_Percent > CCS_Percent and DG_Percent > RAD_Percent:
        datafile.writelines("Winner: Diana Degette\n")

    elif RAD_Percent > CCS_Percent and RAD_Percent > DG_Percent:
        datafile.writelines("Winner: Raymon Anthony Doane\n")
    datafile.writelines("\n")
    datafile.writelines("------------------------------------------\n")
    datafile.writelines("\n")
    
    