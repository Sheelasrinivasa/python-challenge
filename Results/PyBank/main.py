import os
import csv
import operator

# Path to rawdata csv files
#BudgetData1 = os.path.join("..","PyBank","raw_data","budget_data_1.csv")
BudgetData2 = os.path.join("..","PyBank","raw_data","budget_data_2.csv")

#Open files with csv reader and split columns with defined delimiter
#with open(BudgetData1,newline="") as csvfile:
with open(BudgetData2,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)    

# Declaring variable to capture csv values to tables
    Date = []
    Revenue =[]
    Difference = []
    previous = 0

# Read each row of csv and capture data to lists and capture diff of each revenue in Difference table
    for row in csvreader:
        Date.append (row[0])
        Revenue.append (int(row[1]))
        Difference.append (previous - Revenue[-1])
        previous = Revenue[-1]
    #print (Difference)

# Find index of max and min differences in revenue
    x = Difference.index(max(Difference))
    y = Difference.index(min(Difference))

# Calculate Total revenue by summing Revenue list   
    TotalRevenue = sum(Revenue)

# Get the date and difference based on the indexes got from line 29 & print
    GreatestIncrease= Date[x],Difference[x]
    GreatestDecrease= Date[y],Difference[y]
    print (GreatestIncrease)
    print (GreatestDecrease)

# Calculate Average revenue, total revenue / number of instances
    AverageRevenue = round(TotalRevenue / (len(Revenue)),2)

# To print in required format
    PrintMaterial = "Financial Analysis\n-----------------------\nTotal Months: " + str(len(Date)) + "\nTotal Revenue: $" + str(TotalRevenue) +"\nAverage Revenue Change: " + str(AverageRevenue) + "\nGreatest Increase in Revenue: " + str(Date[x]) + "(" + str(Difference[x]) + ")" + "\nGreatest Decrease in Revenue: " + str(Date[y]) + "(" + str(Difference[y]) + ")"        
    print(PrintMaterial)
    
#Create a text file to store data
    #filename = 'Results1.txt'
    filename = 'Results2.txt'
    with open(filename, 'w') as file_object:
        file_object.writelines(PrintMaterial)
