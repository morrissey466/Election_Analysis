# The data we need to retrieve 
# The total number of votes cast 
# the complete list of candidates won 
# the total number of bvotes each candidate won 
# the winner of the election based on popular vote 

import csv
import os

file_to_load = os.path.join("resources", "election_results.csv")
election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    
# To do: read and analyze the data here

    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)