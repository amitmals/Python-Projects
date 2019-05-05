#Import the classes
#Keep the input file named "election_data.csv" in the same folder as the python script
#Output file name: "Output_File.csv"
#Open the input file
#   Cycle through all the rows (remove header)
#   For each cylce increase the counter for total_votes(stores total votes in file)
#   Use var "found" to check if the entry on the row matches any entries in the election_candidates list
#      If candidate is found in election_candidates[] list: Increase vote count votes_for_candidate[] by 1 in  and label as found
#      If candidate is NOT found in election_candidates list: Add candidate name to election_candidates[] list and set no of votes as 1 in votes_for_candidate[]
#   Then, cycle thru election_candidates and votes_for_candidate to find winner and store values in winner_vote_count and winner_name
#   Use total_votes and votes_for_candidate[] to calc the % for each candidate
#Print to terminal and output file

import os
import csv
csvpath = os.path.join("..", "Resources", "election_data.csv")
#open the file budget_data.csv as read only(default) and read it with csv reader
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #initialize my variables    
    election_candidates = []
    votes_for_candidate = []
#   percentage_votes_for_candidates = []
    total_votes = 0
    winner_vote_count=0
    winner_name=""
    
    #remove the header
    next(csvreader)

    # cycle thru the 3rd col to find #votes/candidate
    # increase the total_votes count each time
    # var found is used to check if the candidate is found in the output file
    for row in csvreader:
        total_votes+=1
        found=0
        for idx, val in enumerate(election_candidates):
            if str(row[2])==val:
                votes_for_candidate[idx]+=1
                found = 1
        if found==0:
            election_candidates.append(row[2])
            votes_for_candidate.append(int(1))
    # Now lets find the winner and his vote count
    for idx, val in enumerate(election_candidates):
        if votes_for_candidate[idx]>winner_vote_count:
            winner_vote_count=votes_for_candidate[idx]
            winner_name = election_candidates[idx]

    #print out the output to the terminal screen
    print("|-----------------------------------")
    print("|     Election Results             ")
    print("|----------------------------------")
    print(f'|     Total Votes: {total_votes}')
    print("|----------------------------------")
    
    for idx, val in enumerate(election_candidates):
        print(f'|     {election_candidates[idx]}: {round(votes_for_candidate[idx]/total_votes*100,2)}% ({votes_for_candidate[idx]})')
    print("|----------------------------------")
    print(f'|     Winner: {winner_name}')
    print("|----------------------------------")

    #Now lets open a file and write out the data to it
    with open("Output_File.csv", 'w', newline='') as csvfile2:
         csvwriter = csv.writer(csvfile2, delimiter=',')
         csvwriter.writerow (['Election Results'])
         csvwriter.writerow (['Total Votes',str(total_votes)])
         for idx, val in enumerate(election_candidates):
             csvwriter.writerow([str(election_candidates[idx]), str(round(votes_for_candidate[idx]/total_votes*100,2))+'%',str(votes_for_candidate[idx])])
         csvwriter.writerow (['Winner', str(winner_name)])