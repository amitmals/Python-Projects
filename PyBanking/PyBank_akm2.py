#Import the classes
#Keep the input file named "budget_data.csv" in the same folder as the python script
#Output file name: "Output_File.csv"
#Open the input file
#   Cycle through all the rows (remove header)
#Print to terminal and output file

import os
import csv

#open the file budget_data.csv as read only(default) and read it with csv reader
csvpath = os.path.join("..", "Resources", "budget_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #initialize my variables    
    total_months=0
    net_profit_loss=0
    total_profit_loss=0
    last_mon_profit_loss = 0
    next_mon_profit_loss = 0
    average_change = 0  
    great_increase_mon=""
    great_decrease_mon=""
    great_increase_amt=0
    great_decrease_amt=0
    
    #remove the header
    next(csvreader)
    
    #cycle thru the rest of the rows
    for row in csvreader:
        #increase the counter to count total_months
        total_months+=1
        #for the 1st time the change is 0. so set this_mon_profit_loss and last_mon_profit_loss as the same
        if total_months == 1:
            last_mon_profit_loss = int(row[1])
        #aggregate the net_profit_loss using += the current month profit loss in row[1]
        net_profit_loss+=int(row[1])
        this_mon_profit_loss = int(row[1])
        #aggregate the total_profit_loss using += the current month profit loss in row[1]
        total_profit_loss +=(this_mon_profit_loss - last_mon_profit_loss)
        #check if this is the greatest gain
        if (this_mon_profit_loss-last_mon_profit_loss) > great_increase_amt:
                great_increase_amt = this_mon_profit_loss-last_mon_profit_loss
                great_increase_mon = row[0]
        #check if this is the grestest loss
        if (this_mon_profit_loss-last_mon_profit_loss) < great_decrease_amt:
            great_decrease_amt = this_mon_profit_loss-last_mon_profit_loss
            great_decrease_mon = row[0]
        #set the value in profit loss as last_mon_profit_loss for the next iteration
        last_mon_profit_loss=int(row[1])

#average change is the total_profit_loss divided by the intervals (which is total_months-1)
average_change = total_profit_loss/(total_months-1)

#print out the output to the terminal screen
print ("-------------------------------------------------------------")
print ("Financial Analysis")
print ("-------------------------------------------------------------")
print (f'Total Months: {total_months}')
print (f'Total: ${net_profit_loss}')
print (f'Average Change: ${average_change:.2f}')
print (f'Greatest Increase in Profits: {great_increase_mon} (${great_increase_amt})')
print (f'Greatest Decrease in Profits: {great_decrease_mon} (${great_decrease_amt})')
print ("-------------------------------------------------------------")

#Now lets open a file and write out the data to it
with open("Output_File.csv", 'w', newline='') as csvfile2:
        csvwriter = csv.writer(csvfile2, delimiter=',')
        csvwriter.writerow (['Financial Analysis'])
        csvwriter.writerow (['Total Months', total_months])
        csvwriter.writerow (['Total',"$"+str(net_profit_loss)])
        csvwriter.writerow (['Average Change', "$"+str(round(average_change,2))])
        csvwriter.writerow (['Greatest Increase in Profits',great_increase_mon,"$"+str(great_increase_amt)])
        csvwriter.writerow (['Greatest Decrease in Profits',great_decrease_mon,"$"+str(great_decrease_amt)])