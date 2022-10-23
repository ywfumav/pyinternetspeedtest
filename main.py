import time
import speedtest
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'pi',
    password = 'pi',
    database = 'wan',
)

mycursor = mydb.cursor()

epoch_time = int(time.time()*1000)
print("Epoch time is {}".format(epoch_time))

test = speedtest.Speedtest(secure=True)

test.get_servers()
print("Choosing best servers...")
best = test.get_best_server()
print("Best Server is:")
print("Hostname: {}\nLocation: {} \n".format(best['host'], best['country']))

print("Performing Download Test...")
download_result = test.download()/1024/1024
print("Download Speed: {:.2f} Mbps".format(download_result))

print("Performing Upload Test...")
upload_result = test.upload()/1024/1024
print("Upload Speed: {:.2f} Mbps".format(upload_result))

print("Performing Ping Test...")
ping_result = test.results.ping
print("Ping Latency: {:.2f} ms \n ".format(ping_result))

sql = ("INSERT INTO internet (epoch, download, upload, ping) VALUES ({},{},{},{})".format(epoch_time, download_result, upload_result, ping_result))


mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "details inserted")

mydb.close()
