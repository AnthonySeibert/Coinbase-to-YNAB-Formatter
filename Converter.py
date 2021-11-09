#must install pandas
#must delete info at bottom of starting csv file

import pandas as pd

#user input
filename=input("Enter Starting csv Filename: ")
filename2 = input("Finished csv Filename: ")

#read starting file
starting=pd.read_csv(filename, dtype="str", index_col=None, usecols=[2, 1, 0, 3])

#drop all cells with blank values
starting= starting.dropna()

#select only records with a Type value of purchase
starting = starting[starting.Type == 'Purchase']

#Format Date/Time to only show Date in a new column called Date
starting['Date/Time'] = pd.to_datetime(starting['Date/Time'])
starting["Date"] = starting["Date/Time"].dt.strftime("%m/%d/%y")

#Delete original Date/Time column
starting = starting.drop(columns=["Date/Time"])

#Rename column labels
starting = starting.rename(columns={"Type": "Memo", "Description": "Payee", "Purchase Amount": "Amount"})

#rearrange columns in a new dataframe
output = starting[["Date", "Payee", "Memo", "Amount"]]

#Write dataframe to new csv file and print in console
output.to_csv(filename2, index=False)
print(output)
