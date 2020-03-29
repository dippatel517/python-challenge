import csv

with open('budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    total=0
    average_change = 0
    great_increases =0
    great_decrease = 0
    Change = []
    current_month = 0
    for row in csv_reader:
        if line_count> 0:
            previous_month = current_month
            current_month = int(row[1])
            total = total + current_month
            if   previous_month !=0:
                 Change.append(current_month - previous_month)
        line_count += 1
    average_change= sum(Change)/len(Change)
    great_increases = max(Change)
    great_decrease = min(Change)
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:" + str(line_count-1))
    print('Total: $' + str(total))
    print("Average Change:"+ str(average_change)) 
    print("Greatest Increase in Profits:"+ str(great_increases))
    print("Greatest Decrease in Profits:"+ str(great_decrease))

    
    

 