import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_months = 0
    net_total = 0
    avgerage_change = 0
    greatest_incease = 0
    greatest_decrease = 0
    date = []
    profits =[]

 for row in csvreader:
    date.append(row[0])
    total_months = total_months + 1
    profits.append(row[1])
    net_total = net_total + (int(row[1]))

    average_change = sum(profits)/len(profits)
    
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = date[greatest_index]

    greatest_decrease = min(profits)
    decrease_index = profits.index(greatest_decrease)
    decrease_date = date[worst_index]

    print(f"Financial Analysis")
    print(f"-------------------")

    

    