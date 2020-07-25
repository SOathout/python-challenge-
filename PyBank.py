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
    avg_change = 0
    great_incease = 0
    great_decrease = 0
    date = []
    profits =[]

def print_percentages(first_row):

    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])