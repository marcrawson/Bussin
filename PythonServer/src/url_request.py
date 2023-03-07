import http.client
import json
from json_to_csv import *

# Set the URL endpoint to request
url = "/data/train_set"

# Set up the HTTP connection to localhost
conn = http.client.HTTPConnection("localhost")

# Send the HTTP GET request to the specified endpoint
conn.request("GET", url)

# Get the response from the server
response = conn.getresponse()

# Read the response data as JSON
data = json.loads(response.read())

# Close the connection to the server
conn.close()

# Save the JSON data to a file
with open("example.json", "w") as outfile:
    json.dump(data, outfile)

print("JSON data saved to file 'example.json'")

# convert 'example.json' to 'example.csv'
compute_csv()

print("JSON converted to csv file 'example.csv'")