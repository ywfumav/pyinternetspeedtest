import speedtest

test = speedtest.Speedtest(secure=True)

test.get_servers()
print("Choosing best servers...")
best = test.get_best_server()
print("Best Server is:")
print("Hostname: {}\nLocation: {} \n".format(best['host'], best['country']))

print("Performing Download Test...")
download_result = test.download()
print("Download Speed: {:.2f} Mbps".format(download_result/1024/1024))

print("Performing Upload Test...")
upload_result = test.upload()
print("Upload Speed: {:.2f} Mbps".format(upload_result/1024/1024))

print("Performing Ping Test...")
ping_result = test.results.ping
print("Ping Latency: {:.2f} ms".format(ping_result))