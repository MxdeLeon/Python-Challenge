#!/usr/bin/env python
# coding: utf-8

# In[42]:


import os
import csv

total_votes = 0
counter = 0
candidates = {}
c_names = []
winner_votes = 0
winner = ""
headers = []

csv_path = os.path.join('.', 'Resources', 'election_data.csv')

with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    
    headers = next(csv_reader)
    
    #adds candidate names as keys as well as adding up total votes per candidate and total overall votes
    for row in csv_reader:
        if row[2] not in candidates.keys():
            candidates[row[2]] = [1, 0]
        
        elif row[2] in candidates.keys():
            candidates[row[2]][0] += 1
            
        counter += 1
    
    #stores the candidates names in a list so that keys can be references later
    c_names = candidates.keys()
    
    total_votes = counter
    
    #determines which candidate has the highest number of votes
    for person in candidates:
        candidates[person][1] = candidates[person][0] / counter
        if candidates[person][0] > winner_votes:
            winner_votes = candidates[person][0]
    
    #retrieves the name of the winning candidate
    for key in candidates:
        if winner_votes in candidates[key]:
            winner = key

    #prints results to terminal
    print(f"Election Results\n"
          f"-------------------------")
    for name in c_names:
        print(f"{name}: {(candidates[name][1]):.2%} ({candidates[name][0]})")
    print(f"-------------------------\n"
         f"Winner: {winner}\n"
         f"-------------------------\n")

    #writes results to .txt file
    
txt_path = os.path.join('.', 'analysis', 'election_data_analysis.txt')
with open(txt_path, 'w') as file:
    file.write(f"Election Results\n"
               f"-------------------------\n")
    for name in c_names:
        file.write(f"{name}: {(candidates[name][1]):.2%} ({candidates[name][0]})\n")
    file.write(f"-------------------------\n"
               f"Winner: {winner}\n"
               f"-------------------------\n")
    
    file.close()


# In[38]:


print(headers)

