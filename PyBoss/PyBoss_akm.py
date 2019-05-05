#Import the classes
import os
import csv

# Create a dict to lookup state code for state name
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open("employee_data.csv", newline="") as csvfileIn, open("Output_File.csv", 'w', newline="") as csvfileOut:
    csvreader = csv.reader(csvfileIn, delimiter=",")
    csvwriter = csv.writer(csvfileOut, delimiter=",")
    
    next(csvreader)
    csvwriter.writerow (["Emp ID","First Name","Last Name","DOB","SSN","State"])

    for row in csvreader:
        emp_id = row[0]
        emp_f_name, emp_l_name = row[1].split(" ")
        dob_year, dob_month, dob_date = row[2].split("-")
        new_dob = dob_month + "/" + dob_date + "/" + dob_year
        old_ssn = row[3].split("-")
        new_ssn = "***-**-" + old_ssn[2]
        old_state = row[4]
        new_state = us_state_abbrev[old_state]

        csvwriter.writerow([emp_id, emp_f_name, emp_l_name, new_dob, new_ssn, new_state])

print ("Output file created")
