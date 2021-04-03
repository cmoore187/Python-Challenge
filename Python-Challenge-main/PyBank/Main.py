#import os and csv
import os 
import csv

# create a path to csv file
csvpath = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

#set all variables in this section to zero or empty
totalMonths = 0
net = 0
change = []
monthCount = []
increase = 0
increaseMonth = 0
decrease = 0
decreaseMonth = 0

#Read CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    row = next(csvreader)

    #add to total months and the net 
    totalMonths += 1
    net += int(row[1])

    #set current row as previous row and set the greatest increase as well as month
    increase = int(row[1])
    increaseMonth = row[0]
    previousRow = int(row[1])

     # Read each row of data after the header
    for row in csvreader:
        
        #calculate total months as well as net
        totalMonths += 1
        net += int(row[1])

        #calculate the change from the current month to the previous month
        netChange = int(row[1]) - previousRow
        change.append(netChange)

        #set previous row to current row and count month
        previousRow = int(row[1])
        monthCount.append(row[0])

        #Calculate greatest increase using if
        if int(row[1]) > increase:
            #set increase to current number and month to current month
            increase = int(row[1])
            increaseMonth = row[0]

        #do the same for greatest decrese
        if int(row[1]) < decrease:
            #set decrese to current number and month to current month
            decrease = int(row[1])
            decreaseMonth = row[0]

        # now we calculate the average as well as the date for ouput
        average = sum(change)/ len(change)

        #set the highest and lowest
        high = max(change)
        low = min(change)

#Print the Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${net}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits:, {increaseMonth}, (${high})")
print(f"Greatest Decrease in Profits:, {decreaseMonth}, (${low})")

#send a text file of the analysis to the analysis folder
outputFile = os.path.join("Analysis", "Analysis.text")
with open(outputFile, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {totalMonths}\n")
    txtfile.write(f"Total: ${net}\n")
    txtfile.write(f"Average Change: ${average:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits:, {increaseMonth}, (${high})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {decreaseMonth}, (${low})\n")






