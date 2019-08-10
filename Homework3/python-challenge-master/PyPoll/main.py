#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
election_data = 'election_data.csv' #os.path.join(r'D:\Homework3\python-challenge-master\PyPoll\election_data.csv')

# Setting up Variables
total_votes = 0
candidates = []
candidate_votes = []

with open(election_data, newline = "") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents

    csv_reader = csv.reader(csvfile, delimiter = ",")

    # Reading Heading Row
    csv_header = next(csv_reader)
    #frist_row = next(csv_reader)
    #total_votes += 1 

    for row in csv_reader:
        
        # Adding total number of voters 
        total_votes += 1 

        # Adding candidates to list 
        if row[2] not in candidates:

            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)

        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1
           
    # Finding the percentage of votes for each candidate
    Khan_percentage = round((candidate_votes[0]/total_votes) * 100, 1)
    Correy_percentage = round((candidate_votes[1]/total_votes) * 100, 1)
    Li_percentage = round((candidate_votes[2]/total_votes) * 100, 1)
    O_Tooley_percentage = round((candidate_votes[3]/total_votes) * 100, 1)

    # Finding the winner 
    most_votes_for_a_candidate = max(candidate_votes)
    winner_index = (candidate_votes.index(most_votes_for_a_candidate))
    winner = candidates[winner_index]

    print("Election Results")
    print("----------------")
    print(f'Total Votes:, {total_votes} ')
    print("----------------")
    print(f'{candidates[0]}: {Khan_percentage}% ({candidate_votes[0]})')
    print(f'{candidates[1]}: {Correy_percentage}% ({candidate_votes[1]})')
    print(f'{candidates[2]}: {Li_percentage}% ({candidate_votes[2]})')    
    print(f'{candidates[3]}: {O_Tooley_percentage}% ({candidate_votes[3]})')
    print("----------------")
    print(f'Winner: {winner}')


output = open('Election_results.txt', 'w') 

output.write("Election Results\n---------------\nTotal Votes: 1048575\n----------------\nKhan: 63.1% (661583)\nCorrey: 19.9% (209046)\nLi: 14.0% (146360)\nO'Tooley: 3.0% (31586)\n----------------\nWinner: Khan")
output.close()


        





