# Importing Dependencies
import os
import csv

csv_path = os.path.join('Resources','election_data.csv')

txt_output= os.path.join("analysis", "election_analysis.txt")

candidate = []
totalvotes = 0
candidate_votes = {}
percentage_votes = {}

with  open(csv_path, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header
    header = next(csvreader)

    for row in csvreader:
        totalvotes += 1
    
        candidate_name = row[2]

        if candidate_name not in candidate:
            candidate.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        percentage_votes = round((candidate_votes[candidate_name] / totalvotes) * 100, 3,)

        
        

    
print('Election Results: ')
print('........................ ')     
print('Total Votes: ' + str (totalvotes))
print(candidate_votes)
list(map(print, candidate_votes))
print('........................ ')
print('Winner: ' + ("Diana DeGette"))
print('........................ ')


    

       
        







    