import csv

with open('election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    total=0
    canidates=[]
    votes=[]
    votes_by_candiate=[]
    total_votes=0
    winner=''
    for row in csv_reader:
        if line_count> 0:
             if row[2] not in canidates: 
                canidates.append(row[2]) 
             votes.append(row[2])       
        line_count += 1
    over_total=line_count-1
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(over_total))
    print('-------------------------')
    for canidate in canidates:
           previou_votes=total_votes
           total_votes= votes.count(canidate)
           precent=(total_votes/over_total)*100
           print(canidate +":"+str(precent)+"% " +"("+str(total_votes)+")")
           if total_votes>previou_votes:
               winner=canidate
    print("-------------------------")
    print("Winner:"+winner)
