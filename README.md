# RaspberryPi

<h3>라즈베리 파이 초기 설정</h3>
<br>
  
    sudo apt update
    sudo apt upgrade

<h4>한글깨짐</h4>
    
    sudo apt-get install fonts-unfonts-core -y
    sudo apt-get install ibus ibus-hangul -y
    sudo reboot

<h4>아두이노 설치</h4>

    sudo apt-get install arduino -y

<h3>InfluxDB2 설치</h3>

    wget -q https://repos.influxdata.com/influxdata-archive_compat.key
    echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
    echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list


* Packages are up to date && install influxdb2

      sudo apt-get update && sudo apt-get install influxdb2 -y

* InfluxDB as a background service on startup

      sudo service influxdb start
  
* InfluxDB is status (service)

      sudo service influxdb status

<h3>InfluxDB2 web setting </h3>

* localhost:8086 접속

* GET STARTED
  ![image](https://github.com/ikk5515/RaspberryPi/assets/22267184/6fbe50d0-a6c9-433f-9e37-1a5027b314b2)

* Setup Initial User
* (pi , raspberry)
* Organization Name (study)
* Bucket Name (DatabaseName)
* test
  * test
![image](https://github.com/ikk5515/RaspberryPi/assets/22267184/6c0f0f75-35f7-4611-bd0c-c5eac3139b65)

