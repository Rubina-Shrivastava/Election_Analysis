# Data we need to Retrieve
# 1 Total number of votes cast
# 2 A complete list of candidates who received votes
# 3 Total number of votes each candidate received
# 4 Percentage of votes each candidate won
# 5 The winner of the election based on popular vote

import csv
import os
from re import T
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'      #For window user
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.

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
with open(file_to_save, "w") as txt_file:
       
     txt_file.write("countits in Election")
     txt_file.write("\n---------------")
     txt_file.write("\nArapahoe\nDenver\nJefferson")
     # Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)