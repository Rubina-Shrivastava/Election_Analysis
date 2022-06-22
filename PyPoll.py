# Data we need to Retrieve
# 1 Total number of votes cast
# 2 A complete list of candidates who received votes
# 3 Total number of votes each candidate received
# 4 Percentage of votes each candidate won
# 5 The winner of the election based on popular vote

from asyncore import write
import csv
import os

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'      #For window user
file_to_load = os.path.join("Resources", "election_results.csv")

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
#  Declare the empty dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
candidate_resultstotal = ""

with open(file_to_load) as election_data:
# To do: perform analysis.
     print(election_data)
# Close the file.
#election_data.close()  #If we not use 'with' with open function
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Create a filename variable  to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#with open(file_to_save, "w") as txt_file:
       
   #  txt_file.write("countits in Election")
    # txt_file.write("\n---------------")
     #txt_file.write("\nArapahoe\nDenver\nJefferson")
     # Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
 # Print each row in the CSV file.
    for row in file_reader:
 # 2. Add to the total vote count.
        total_votes += 1


# Print the candidate name from each row.
        candidate_name = row[2]
        

    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
                # Add it to the list of candidates.
                candidate_options.append(candidate_name)
                # 2. Begin tracking that candidate's vote count.
                candidate_votes[candidate_name] = 0

     # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


# 3. Print the total votes.
print(total_votes)
# Print the candidate list. 
print(candidate_options)  
# Print the candidate vote dictionary.
print(candidate_votes)    
# Determine the percentage of votes for each candidate by looping through the counts.
for candidate_name in candidate_votes:
    #  vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
     
    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
    
    candidate_resultstotal = candidate_resultstotal + "....."+ candidate_results 
    print(candidate_results)
 
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name


winning_candidate_summary = (
    f"-------------------------\n"
    f"Candidate Results: {candidate_resultstotal} \n"
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

with open(file_to_save, "w") as txt_file:
       
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print(election_results, end = "none")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    #txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary)
        

