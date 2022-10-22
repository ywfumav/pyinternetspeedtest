# Generate test data for demonstration of the visualization
# Creates json file of mocked data
# including Download speed, Uplaod speed and ping latency
import json
import os
import pprint
import random
from datetime import datetime, timedelta

import speedtest

# Create folder to save all the generated test data
gen_data_dir = os.getcwd() + "/data/gen"
if not os.path.exists("data/gen"):
    os.mkdir("data/gen")

# Create file to save the test data
gen_data_path = os.getcwd() +  f"/data/gen/data_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.json"
print(gen_data_path)
if not os.path.exists(gen_data_path):
    f = open(gen_data_path, "w")
    f.write("")
    f.close()

# Calculate total number of data points to visualize N days worth of data
NUM_DAYS = 5
total_data_points = NUM_DAYS * 24 * (60//5)
print(f"Generating {total_data_points} datapoints to simulate {NUM_DAYS} days")

# Data generation start date
start = datetime.now()
now = start

# Get servers to receive a fixed result
test = speedtest.Speedtest(secure=True)
test.get_servers()
print("Choosing best servers...")
best = test.get_best_server()
host = best["host"]
country = best["country"]
download_result = test.download()/1024/1024
upload_result = test.upload()/1024/1024
ping_result = test.results.ping

# Set seed for replicability
random.seed(8888)

datas = []
for _ in range(total_data_points):

    # Increment timestamp by 5 minutes
    now = now + timedelta(minutes=5)

    # Create epsilon small values to add to values for variation
    epsilon_download = random.uniform(-150.5, 15.5)
    epsilon_upload = random.uniform(-100.5, 15.5)
    epsilon_ping = random.uniform(-1, 1)
    new_download_result = download_result + epsilon_download
    new_upload_result = upload_result + epsilon_upload
    new_ping_result = ping_result + epsilon_ping
    timestamp = now.strftime('%Y-%m-%dT%H:%M:%S.%f')

    # Debug print
    print(f"{timestamp} {host} {country} {download_result:,.2f} [{epsilon_download:,.2f}] {upload_result:,.2f} [{epsilon_upload:,.2f}] {ping_result:,.2f} [{epsilon_ping:,.2f}]")

    # Save to list
    datas.append({"host": host, "country": country, "download": new_download_result, "upload": new_upload_result, "ping": new_ping_result})

# Write to json file
with open(gen_data_path, "w") as f:
    json.dump(datas, f)
