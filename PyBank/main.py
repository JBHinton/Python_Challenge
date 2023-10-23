import csv
data = csv.DictReader(open('C:/Users/jackb/OneDrive/Data Analyst/Projects/Python_Challenge/PyBank/Resources/budget_data.csv'))


# Initialize variables
months = 0
total = 0
total_ch = 0
pre_rev = 0
greatest_increase = 0
greatest_decrease = 0
increase_month = ""
decrease_month = ""

    # Loop through the data
for row in data:
        months += 1
        rev = int(row['Profit/Losses'])
        total += rev

        ch = rev - pre_rev
        total_ch += ch

        if ch > greatest_increase:
            greatest_increase = ch
            increase_month = row['Date']
        if ch < greatest_decrease:
            greatest_decrease = ch
            decrease_month = row['Date']

        pre_rev = rev

# Calculate the average change
average_change = total_ch / (months - 1)

# Create the output
output = f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total:,}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {increase_month} (${greatest_increase:,})
Greatest Decrease in Profits: {decrease_month} (${greatest_decrease:,})
'''

print(output)





