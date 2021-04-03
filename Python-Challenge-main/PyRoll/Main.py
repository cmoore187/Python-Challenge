#import os and csv
import os 
import csv

# create a path to csv file
csvpath = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyPoll_Resources_election_data (1).csv")

#set all variables in this section to zero
totalVotes = 0
kahn = 0
correy = 0
li = 0
otooley =0

#Read CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    row = next(csvreader)

     # Read each row of data after the header
    for row in csvreader:
        
        #calculate total votes
        totalVotes += 1

        #calculate total votes for each person using ifs and else ifs
        if(row[2] == "Li"):
            li += 1
        elif(row[2] == "Khan"):
            kahn += 1
        elif(row[2] == "Correy"):
            correy += 1
        else:
            otooley += 1

        #now calculate percentages
        kahnPer = kahn/totalVotes
        liPer = li/totalVotes
        otooleyPer = otooley/totalVotes
        correyPer = correy/totalVotes

        #calculte the winner
        winner = max(kahn,li,otooley,correy)
        #use ifs and elseifs to name the winner
        if winner == correy:
            name = "Correy"
        elif winner == li:
            name = "Li"
        elif winner == kahn:
            name = "Kahn"
        else:
            name  = "O'Tooley"
    

        

        

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {totalVotes}")
print(f"---------------------------")
print(f"Kahn: {kahnPer:.0%}({ kahn})")
print(f"Correy: {correyPer:.0%}({ correy})")
print(f"Li: {liPer:.0%}({ li})")
print(f"O'Tooley: {otooleyPer:.0%}({ otooley})")
print(f"---------------------------")
print(f"Winner: {name}")
print(f"---------------------------")

#send a text file of the analysis to the analysis folder
outputFile = os.path.join("Analysis", "Analysis.text")
with open(outputFile, 'w',) as txtfile:

        # Print Analysis
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {totalVotes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {kahnPer:.0%}({kahn})\n")
    txtfile.write(f"Correy: {correyPer:.0%}({correy})\n")
    txtfile.write(f"Li: {liPer:.0%}({li})\n")
    txtfile.write(f"O'Tooley: {otooleyPer:.0%}({otooley})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {name}\n")
    txtfile.write(f"---------------------------\n")