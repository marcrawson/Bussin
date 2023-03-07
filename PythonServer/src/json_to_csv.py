import json
import csv

def compute_csv():
    with open('example.json', 'r') as input: # open input json file
        data = json.load(input) # load json data into python object

    with open('example.csv', 'w', newline='') as outfile: # open output csv file
        writer = csv.writer(outfile) # create csv writer object
        writer.writerow(['id', 'trip_id', 'route_id', 'stop_sequence', 'arrival_time', 'stop_id', 'scheduled']) # write headers to csv file

        for bus in data: # write each rowto csv file
            writer.writerow([bus['id'], bus['trip_id'], bus['route_id'], bus['stop_sequence'], bus['arrival_time'], bus['stop_id'], bus['scheduled']])