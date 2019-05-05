#Import the classes
#Keep the input file named "budget_data.csv" in the same folder as the python script
#Output file name: "Output_File.csv"
#Open the input file
#   Cycle through all the rows (remove header)
#   For each cylce increase the counter for total_months and add the net_profit_loss variable
#   Check to see if the entry in the row is the great_increase_amt/great_decrease_amt. If so save the month in great_increase_mon/great_decrease_mon
#   Cal Average profit/loss as avg_profit_loss
#Print to terminal and output file

import os
import csv

#open the file budget_data.csv as read only(default) and read it with csv reader
with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #initialize my variables    
    total_months=0
    net_profit_loss=0
    avg_profit_loss=0
    great_increase_mon=""
    great_decrease_mon=""
    great_increase_amt=0
    great_decrease_amt=0
    
    #remove the header
    next(csvreader)
    
    #cycle thru the rest of the rows
    #increase the counter to count total_months and check if the data in the row has the largest increase or decrease
    #save the corresponding month
    for row in csvreader:
        total_months+=1
        net_profit_loss+=int(row[1])
        if int(row[1])>great_increase_amt:
            great_increase_amt= int(row[1])
            great_increase_mon=row[0]
        elif int(row[1])<great_decrease_amt:
                great_decrease_amt=int(row[1])
                great_decrease_mon=row[0]
    
    avg_profit_loss=net_profit_loss/total_months
    
    #print out the output to the terminal screen
    print ("-------------------------------------------------------------")
    print ("Financial Analysis")
    print ("-------------------------------------------------------------")
    print (f'Total Months: {total_months}')
    print (f'Total: ${net_profit_loss}')
    print (f'Average Change: ${avg_profit_loss:.2f}')
    print (f'Greatest Increase in Profits: {great_increase_mon} (${great_increase_amt})')
    print (f'Greatest Decrease in Profits: {great_decrease_mon} (${great_decrease_amt})')
    print ("-------------------------------------------------------------")

    #Now lets open a file and write out the data to it
    with open("Output_File.csv", 'w', newline='') as csvfile2:
         csvwriter = csv.writer(csvfile2, delimiter=',')
         csvwriter.writerow (['Financial Analysis'])
         csvwriter.writerow (['Total Months', total_months])
         csvwriter.writerow (['Total',"$"+str(net_profit_loss)])
         csvwriter.writerow (['Average Change', "$"+str(round(avg_profit_loss,2))])
         csvwriter.writerow (['Greatest Increase in Profits',great_increase_mon,"$"+str(great_increase_amt)])
         csvwriter.writerow (['Greatest Decrease in Profits',great_decrease_mon,"$"+str(great_decrease_amt)])