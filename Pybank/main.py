import os
import csv

# Set path for file
budget_data_csv = os.path.join(".", "Resources", "budget_data.csv")


#  List of stored data
Current_dates = []
Current_month_PL = []
PL_movement = []
PL_Max_amount = []
PL_Min_amount = []
PL_Max_date = []
PL_Min_date = []


# Establishing variables to help calculate Total Profit/Loss from the csv file
Total_PL = 0
Open_PL = 0
PL_month_movement = 0
OpenMaxValue = 0
OpenMinValue = 0
Total_PL_movement = 0

# with open(budget_data_csv, encoding='utf-8') as csvfile:
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # Skips the Header row
    next(csvreader)
 
    for row in csvreader:
        # Adds the dates
        Current_dates.append(row[0])
        
        # Adds the Profit/Loss values
        Current_month_PL.append(row[1])

        # Calculates the Profit/Loss total through each loop
        Total_PL = Total_PL + int(float(row[1]))


# Uses a 'for loop' to calcaulates the PL movements between the various months and then saves it to a list 
for i in Current_month_PL:
    PL_month_movement = int(i) - Open_PL
    PL_movement.append(int(PL_month_movement))
    Open_PL = int(i)
    Total_PL_movement = Total_PL_movement + PL_month_movement


#Confirms the total number of months
count_of_dates = (len(Current_dates))


#Confirms the total number of months for Profit movements
Average_PL_dates = (len(Current_dates)) - 1


#Identifies the Biggest Profit in the Profit/Loss movement
max_value = max(PL_movement)


#Identifies the position of the Biggest Profit in the list
max_index = PL_movement.index(max_value)


#Identifies the position of the date relative for Biggest Profit value
PL_Max_date = Current_dates[max_index]


#Identifies the biggest Loss in the Profit/Loss movement
min_value = min(PL_movement)


#Identifies the position of the Biggest Loss in the list 
min_index = PL_movement.index(min_value)


#Identifies the position of the date relative for Biggest Loss value
PL_Min_date = Current_dates[min_index]


#Calulates the average Profit Loss over the period
Total_PL_movement_Average = round((Total_PL_movement - int(Current_month_PL[0])) /Average_PL_dates, 2)


# Prints the outputs from script to the screen
print("\n")
print("Financial Analysis\n")
print("------------------------------------------\n")
print (f"Total Months: {count_of_dates}\n")
print(f"Total: ${Total_PL}\n")
print(f"Average Change: ${Total_PL_movement_Average}\n")
print(f"Greatest Increase in Profits: {PL_Max_date} ${max_value} \n")
print(f"Greatest Decrease in Profits: {PL_Min_date} (${min_value}) \n")


# Sets the output file path
output_file = os.path.join(".", "analysis","analysis.txt")


# Writes the outputs from script to a txt file
with open(output_file, "w") as datafile:
    datafile.writelines("\n")
    datafile.writelines("Financial Analysis\n")
    datafile.writelines("\n")
    datafile.writelines("------------------------------------------\n")
    datafile.writelines("\n")
    datafile.writelines(f"Total Months: {count_of_dates}\n")
    datafile.writelines("\n")
    datafile.writelines(f"Total: ${Total_PL}\n")
    datafile.writelines("\n")
    datafile.writelines(f"Average Change: ${Total_PL_movement_Average}\n")
    datafile.writelines("\n")
    datafile.writelines(f"Greatest Increase in Profits: {PL_Max_date} ${max_value} \n")
    datafile.writelines("\n")
    datafile.writelines(f"Greatest Decrease in Profits: {PL_Min_date} (${min_value}) \n")