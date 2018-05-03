import os
import csv
import operator
import itertools
from tabulate import tabulate

# Path to rawdata csv files
PollData1 = os.path.join("..","PyPoll","raw_data","election_data_1.csv")

#PollData2 = os.path.join("..","PyPoll","raw_data","election_data_2.csv")

#Open files with csv reader and split columns with defined delimiter
with open(PollData1,newline="") as csvfile:
#with open(PollData2,newline="") as csvfile:

# To split the CSV file to columns
    csvreader = csv.reader(csvfile,delimiter=",")

# To skip header
    next(csvreader)

# Declaring variable 
# Candidate is to get column from csv
# UniqueCandidate is to store unique candidate names
# VoterCounter is to get votes per candidate
# Percentage to calculate percentage of candidate votes 
    Candidates = []
    UniqueCandidate = []
    VoteCounter = []
    Percentage = []


# Capture Candidate column from csv to Candidate list
    for row in csvreader:
        Candidates.append (row[2])

# Calculate total votes by length of Candidates list    
    TotalCounter = len(Candidates)

# Capture unique candidate names from Candidate list
    for i in Candidates:
        if i not in UniqueCandidate:
            UniqueCandidate.append (i)

# Calculate counts per unique candidates from Candidates list   
    for x in UniqueCandidate:
        VoteCounter.append (Candidates.count(x))

# Calculate % of Votes per candidate, calling TotalCounters calculated earlier
    for y in VoteCounter:
        Percentage.append (y / TotalCounter * 100)

# Find max of Votecounter index and get candidate name from UniqueCandidates
    WinnerInd = VoteCounter.index(max(VoteCounter))
    Winner = UniqueCandidate[WinnerInd]

# Creating variables to print (just split for easy maintenance)    
 
# Part 1
    PrintMaterial = "Election Results\n---------------------------------------\nTotal Votes: " + str(TotalCounter) + "\n---------------------------------------\n" 
    print(PrintMaterial)

# Part 2
    Trial = []
    for UniqueCandidate,VoteCounter,Percentage in zip(UniqueCandidate,VoteCounter,Percentage):
        Test = (UniqueCandidate,VoteCounter,Percentage)
        Trial.append(Test)
    print(tabulate(Trial, headers=['Candidate','Votes','Percentage(%)']))

# Part 3   
    PrintMaterial1 = "\n---------------------------------------\n Winner: " + str(Winner) +"\n---------------------------------------\n"
    print(PrintMaterial1)
  
    
#Create a text file to store data
    filename = 'Results1.txt'
    #filename = 'Results2.txt'

# Create/Open text file and append
    with open(filename, 'a') as file_object:
        file_object.writelines(PrintMaterial)
        file_object.writelines (str(tabulate(Trial, headers=['Candidate','Votes','Percentage(%)'])))
        file_object.writelines(PrintMaterial1)

    


 