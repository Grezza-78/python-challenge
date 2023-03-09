import os
import csv

budget_data_csv = os.path.join(".", "Resources", "budget_data.csv")

#  List of store data
dates = []
profit_loss = []

# Establishing a sum variable to calculate Total Profit/Loss from the csv file
sum = 0
max_value = 0
max_index = 0
min_value = 0
min_index = 0

# with open(work_csv, encoding='utf-8') as csvfile:
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Skip the header of the csv file   
    next(csvreader)

    for row in csvreader:
        # Adds the dates
        dates.append(row[0])
        
        # Adds the Profit/Loss values
        profit_loss.append(row[1])
        
        # Calculates the Profit/Loss total through each loop
        sum = sum + (int(float(row[1])))

        if int(float(profit_loss(row[1]))) > max_value:
            max_value = int(float(row[1])) 
            max_index = row[1]
            print(max_value)
            print(max_index)

"""# Confirms the total number of months
count = (len(dates))

# Uses the Profit/Loss Open and Closing Value for the period from the set 
# and then devides by the number of months to calcualte the average change 
# for the period
open_PL_value = profit_loss[0]
close_PL_value = profit_loss[-1]
PL_year = ((int(close_PL_value) - (int(open_PL_value))) / int(count))
average_PL = (round(float(PL_year), 2))

# Using the max function to identify the biggest value in the PL list
max_value = (max(profit_loss))

# Identifies the position of the max value within the PL list
max_index = profit_loss.index(max_value)

# Using max_value position identified to identify the position with in the Dates list
date_max = dates[max_index]

# Using the min function to identify the biggest value in the PL list
min_value = (min(profit_loss))

# Identifies the position of the min value within the PL list
min_index = profit_loss.index(min_value)

# Using min value position identified to identify the position with in the Dates list
date_min = dates[min_index]



print("\n")
print("Financial Analysis\n")
print("------------------------------------------\n")
print (f"Total Months: {count}\n")
print(f"Total: ${sum}\n")
print(f"Average Change: ${average_PL}\n")
print(f"Greatest Increase in Profits: {date_max} ${max_value} \n")
print(f"Greatest Decrease in Profits: {date_min} (${min_value}) \n")


output_file = os.path.join(".", "analysis","analysis.txt")

with open(output_file, "w") as datafile:
    datafile.writelines("\n")
    datafile.writelines("Financial Analysis\n")
    datafile.writelines("\n")
    datafile.writelines("------------------------------------------\n")
    datafile.writelines("\n")
    datafile.writelines(f"Total Months: {count}\n")
    datafile.writelines("\n")
    datafile.writelines(f"Total: ${sum}\n")
    datafile.writelines("\n")
    datafile.writelines(f"Average Change: ${average_PL}\n")
    datafile.writelines("\n")
    datafile.writelines(f"Greatest Increase in Profits: {date_max} ${max_value} \n")
    datafile.writelines("\n")
    datafile.writelines(f"Greatest Decrease in Profits: {date_min} (${min_value}) \n")"""