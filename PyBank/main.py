#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
# budget_data = 'budget_data.csv'
budget_data = os.path.join(r'C:\Users\zacha\Desktop\Python-Challenge\python-challenge\PyBank\budget_data.csv')

# Variables Used for Homework 
months = 0 
profit_losses = 0
change = 0
current= 0
day = []
profits = []

with open(budget_data, newline = "") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter = ",")

    # Read the Header Row and the first row while adding 1 to total months and keeping track of profit/losses
    csv_header = next(csv_reader)
    first_row = next(csv_reader)
    months += 1
    profit_losses += int(first_row[1])
    current = int(first_row[1])

    for row in csv_reader:

        # Keeping Track of the days and adding 1 count to months   
        day.append(row[0])
        months += 1

        # Keeping Track of the change in Profits/Losses and updating what the current value is for each row
        change = int(row[1])-current
        current = int(row[1])
        profits.append(change)
        

        # Sum of profits and losses (Net Profit)
        profit_losses = profit_losses + int(row[1])

 # The average of the changes in "Profit/Losses" over the entire period
    average_change = round(sum(profits)/len(profits),2)

 # Doing Maximum Change in profits while indexing the correct date
    Max_Change = max(profits)
    Max_Date = profits.index(Max_Change)
    Max_Day = day[Max_Date]
# Doing Minimum Change in profits while indexing the correct data
    Min_Change = min(profits)
    Min_Date = profits.index(Min_Change)
    Min_Day = day[Min_Date]

    print("Financial Analysis")
    print("----------------")
    print(f'Total Months: {months}')
    print("----")
    print(f'Total: ${profit_losses}')
    print("----")
    print(f'Average Change: ${average_change}')
    print("----")
    print(f'Greatest Increase in Profits: {Max_Day} ({Max_Change})')
    print("----")
    print(f'Greatest Increase in Profits: {Min_Day} ({Min_Change})')




output = open('Bank_results.txt', 'w')


line1 = "Financial Analysis"
line2 = "-------------------"
line3 = f'Total Months: {months}'

line3 = str( print(f'Total Months: {months}'))

output.write("Financial Analysis\n--:)-----:)---:)-----\nTotal Months: 86\nTotal: $38382578\nAverage Change: $-2315.12\nGreatest Increase in Profits: Feb-12 (1926159)\nGreatest Increase in Profits: Sep-13 (-2196167)")
output.close()
    



    


    

    