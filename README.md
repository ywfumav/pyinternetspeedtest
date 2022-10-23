# pyinternetspeedtest
An internet speed test monitor.

**pyinternetspeedtest** will conduct a internet speed test using **speedtest-cli**. Then it will save test values into a **sql database**. User can monitor internet performance from a local webpage hosted on **node red**.

## Hardware Information
Hardware: **Raspberry Pi 4 Model B** <br>
OS: **Raspbian Buster Lite**

## Code Flowchart
```mermaid
graph TD;
A[<font size = 3>main.py]-->B[<font size = 3>speedtest-cli<br><font size = 2>conduct internet speed test every minute] 
B-->A
A-->C[<font size = 3>database<br><font size = 2>store speed test results<br>datetime<br>download speed<br>upload speed<br>ping]
C-->D[<font size = 3>Web GUI<br><font size = 2>Local Web interface to monitor <br> speed test results ]
```

## Installation
### Update Raspberry Pi
```
sudo apt update 
sudo apt upgrade
```

### Install Git
```
sudo apt install git
```

### Install speedtest-cli
```
sudo pip3 install speedtest-cli
```

### Install MariadB
```
sudo apt install mariadb-server
sudo pip3 install mysql-connector-python==8.0.29
```


### speedtest-cli

