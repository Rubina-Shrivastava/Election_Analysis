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

candidate_options = []

candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0
candidate_resultstotal = ""
countyreult_total = ""
winning_countycount =0
winning_countypercentage = 0
winning_county =""
# 1: Create a county list and county votes dictionary.

county_list = []
county_votes ={}

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
        # 3: Extract the county name from each row.
        county_name = row[1]
        

    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
                # Add it to the list of candidates.
                candidate_options.append(candidate_name)
                # 2. Begin tracking that candidate's vote count.
                candidate_votes[candidate_name] = 0

     # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # county does not match any existing county in the county list.

        if county_name not in county_list:
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.

        county_votes[county_name] += 1        

print(county_list)
print(county_votes)
# 3. Print the total votes.
print(total_votes)
# Print the candidate list. 
print(candidate_options)  
# Print the candidate vote dictionary.
print(candidate_votes)   
print (county_votes) 
# Determine the percentage of votes for each candidate by looping through the counts.
 # 6a: Write a for loop to get the county from the county dictionary.
for county_name  in county_votes:
        # 6b: Retrieve the county vote count.
    countyvote = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
    countyvote_percentage = float(countyvote) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
    county_result = (f"{county_name}: {countyvote_percentage:.1f}% ({countyvote:,})\n") 

    countyreult_total = countyreult_total + '#' +  county_result
    print(county_result)

         # 6f: Write an if statement to determine the winning county and get its vote count.
    if(countyvote > winning_countycount) and (countyvote_percentage > winning_countypercentage) :
        winning_countycount = countyvote
        winning_countypercentage = countyvote_percentage
        winning_county = county_name

    # 7: Print the county with the largest turnout to the terminal.


winning_county_summary = (
    f"-------------------------\n"
    f"county Votes: \n{countyreult_total} \n"
    f"-------------------------\n"
    f"Winner county Details: \n"
    f"Largest  county turnout : {winning_county}\n"
    f"Winning County votes: {winning_countycount:,}\n"
    f"Winning  county Percentage: {winning_countypercentage:.1f}%\n"
    f"-------------------------\n")
print(winning_county_summary)


for candidate_name in candidate_votes:
    #  vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
     
    # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")  
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
    
    candidate_resultstotal = candidate_resultstotal + "#"+ candidate_results 
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
    f"Candidate Results: \n{candidate_resultstotal} \n"
    f"-------------------------\n"
    f"Winner Details: \n"
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
    txt_file.write(winning_county_summary)
    txt_file.write(election_results)
    #txt_file.write(candidate_results)
    txt_file.write(winning_candidate_summary)
        

