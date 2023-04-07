import csv 
with open('game_log.csv', 'w', newline='') as file:
     writer = csv.writer(file)

     writer.writerow(["Game #", "Winner", "Score"])