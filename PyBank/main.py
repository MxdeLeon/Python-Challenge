#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import csv
import statistics as st

num_months = 0
total = 0
change = []
date_tracker = []
avg_change = 0
greatest_increase = 0
increase_date = ""
greatest_decrease = 0
decrease_date = ""
prev_val = 0
headers = []

csv_path = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csv_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    
    headers = next(csv_reader)
    
    counter = 0
    
    #calculates total entries, appends the changes between entries and associated dates
    for row in csv_reader:
        total += int(row[1])
        num_months += 1
        if counter > 0:
            change.append(int(row[1]) - prev_val)
            date_tracker.append(row[0])
            
        prev_val = int(row[1])
        counter += 1
    
    #calculates the average change, greatest increase, and greatest decrease
    avg_change = st.mean(change[:])
    greatest_increase = max(change[:])
    greatest_decrease = min(change[:])
    
    #retrieves the dates of greatest increase and decrease
    increase_date = date_tracker[change.index(greatest_increase)]
    decrease_date = date_tracker[change.index(greatest_decrease)]
    
    #prints results to terminal
    print(f"Financial Analysis\n"
          f"----------------------------\n"
          f"Total Months: {num_months}\n"
          f"Total: {total}\n"
          f"Average Change: {round(avg_change, 2)}\n"
          f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
          f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")
    
    #writes results to .txt file
    txt_path = os.path.join('.', 'analysis', 'budget_data_analysis.txt')
    with open(txt_path, 'w') as file:
        file.write(f"Financial Analysis\r")
        file.write(f"----------------------------\n")
        file.write(f"Total Months: {num_months}\r")
        file.write(f"Total: {total}\r") 
        file.write(f"Average Change: {round(avg_change, 2)}\r")
        file.write(f"Greatest Increase in Profits: {increase_date} ({greatest_increase})\r")
        file.write(f"Greatest Decrease in Profits: {decrease_date} ({greatest_decrease})\r")
        
    file.close()


# In[3]:


print(headers)


# In[ ]:




