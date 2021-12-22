import csv
import haversine as hs
from haversine import Unit
station = []
people = []
dis = []
pop = []
output = []

with open('people.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    for row in spamreader:
        people.append(row)
        people = [list(map(float, x)) for x in people]

with open('station.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    for row in spamreader:
        station.append(row)
        station = [list(map(float, x)) for x in station]


Spoint = []
for i in range(len(station)):
    Spoint.append([station[i][1], station[i][2]])

Ppoint = []
for i in range(len(people)):
    Ppoint.append([people[i][0], people[i][1]])

for cntS in range(len(station)):
    print(str(cntS)+"번쨰 거치대 확인")
    short_distance = 10000000000000
    dis.append(0)
    pop.append(0)
    for cntP in range(len(people)):
        result = hs.haversine(Spoint[cntS], Ppoint[cntP], unit=Unit.METERS)
        if result < short_distance:
            print("최단 거리 갱신")
            short_distance = result
            dis[cntS] = short_distance
            pop[cntS] = people[cntP][2]

for i in range(len(station)):
    output.append([station[i][0], station[i][3], pop[i], dis[i]])

csvfile = open("station_pop.csv", "w", newline="")

csvwriter = csv.writer(csvfile)
for row in output:
    csvwriter.writerow(row)
csvfile.close()
