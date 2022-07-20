# Election-Analysis
## Overview of Election-Audit
Colorado Board of Election has requested for the assistance to submit election data to Election Commission in recent local congressional election. In addition to information such as total number of votes cast, votes received by each candidate, percentage of votes of each candidate, and winning candidate, the Election board has also requested following additional data to submit to Election commision;
1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

In this project, we'll use Python3.7.6 and Visual Studio Code to analyze and generate the election-audit result.

## Election-Audit Results
1. Number of votes in congressional election= 369,711
2. Number of votes and the percentage of total votes for each county in the precinct
    ![image](https://user-images.githubusercontent.com/107566776/179990336-a4734526-e1c3-4a17-810d-fd4cc7d0605a.png)


4. County with largest number of votes= Denver
5. Number of votes and the percentage of total votes each candidate received
   ![image](https://user-images.githubusercontent.com/107566776/179990816-ed4153cf-4e95-45c4-b04f-ace47a0f29af.png)

7.  Winner Details
    Winning Candidate- Diana Degette
    Total Vote Count- 272,892
    Percentage of their total votes- 73.8%
    
    ![image](https://user-images.githubusercontent.com/107566776/179988938-bfaa74cb-f5cc-46d3-97e1-33f3d80a02e1.png)
    
## Election-Audit Summary
The script for this Election-Audit can be used to analyze and generate result for any future election. 
file_to_load = os.path.join("Resources", "election_results.csv"), you can update the election_results that contains new election data
file_to_save = os.path.join("analysis", "election_analysis.txt"), save the output in new analysis_txt file.
