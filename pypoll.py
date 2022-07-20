import csv
import os
file_to_load=os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("analysis","election_analysis.txt")

#initialize a total vote counter
total_votes=0

#Candidate options
candidate_options=[]

#Declare empty dictionary
candidate_votes={}

winning_candidate=""
winning_count=0
winning_percentage=0

#open election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
  
    #print each row in CSV file
    for row in file_reader:
        #Add to total vote count
        total_votes+=1

        #Print the candidate name from each row
        candidate_name=row[2]

        if candidate_name not in candidate_options:

        #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
        #Begin tracking candidate vote count
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
        
with open(file_to_save,"w")as txt_file:
    election_results=(
        f"\nElection Results\n"
        f"_______________________\n"
        f"Total Votes:{total_votes,}\n"
        f"_______________________\n")
    print(election_results,end="")

    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)*100
        candidate_results=(
            f"{candidate_name}:{vote_percentage:.1f}%({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
            
        if(votes>winning_count)and(vote_percentage>winning_percentage):
            winning_count=votes
            winning_candidate=candidate_name
            winning_percentage=vote_percentage

    winning_candidate_summary=(
        f"---------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count:{winning_count:,}\n"
        f"Winning Percentage:{winning_percentage:.1f}%\n"
        f"____________________________\n")
            
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)