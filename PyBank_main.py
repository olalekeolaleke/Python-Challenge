from audioop import minmax
import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

txt_output= os.path.join("analysis", "budget_analysis.txt")

dates = []
total_months = 0
total_profit = 0
monthly_change = []
grtst_incr = 0
grtst_incr_month = 0
grtst_dcr = 0
grtst_dcr_month = 0
ini_profit = []


with open(csv_path, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header
    header = next(csvreader)
    row = next(csvreader)

    total_months += 1
    total_profit += int(row[1])
    ini_profit = int(row[1])

# Calculate the value of the total months and the total profit

    for row in csvreader:
        total_months += 1
        total_profit += int(row[1])

# Calculate the value of the average change

        profit_change = int(row[1]) - ini_profit
        monthly_change.append(profit_change)
        ini_profit = int(row[1])

        average_change = round((sum(monthly_change)/len(monthly_change)), 2)
        dates.append(row[0])


        if int(row[1]) > grtst_incr:
            grtst_incr = int(row[1])
            grtst_incr_month = (row[0])

            




print('Financial Analysis: ')
print('...................')
print('Total Month: ' + str(total_months))
print('Total: ' '$' + str(total_profit))
print('Average Change: ' '$' + str(average_change))
print('Greatest Increase: ' '$' + str(grtst_incr))




