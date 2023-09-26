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

<h3>InfluxDB2 설치 (2의경우)</h3>

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


<h3>InfluxDB 설치 (1의경우)</h3>

    wget -q https://repos.influxdata.com/influxdata-archive_compat.key
    echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null
    echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list


* Packages are up to date && install influxdb

      sudo apt-get update && sudo apt-get install influxdb -y

* InfluxDB as a background service on startup

      sudo service influxdb start
  
* InfluxDB is status (service)

      sudo service influxdb status


* Terminal
  * database 생성
  
        create database pir

  * database 조회
 
        show databases

  * influxdb import with python

        sudo pip3 install influxdb

  * python pir_influx.py 실행시 running influxdb OK라 표시되면 DB에 저장중인 상태


# Grafana Installation

<h4>1. Repository의 GPG key를 더하기</h4>

      wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -

<h4>2. Repository를 더하기</h4>

      echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

<h4>3. 프로그램 설치</h4>

      sudo apt update
      sudo apt install grafana

<h4>4. 프로그램 실행</h4>

      sudo service grafana-server start

<h4>influxdb import with python</h4>

      sudo pip3 install influxdb


# 라즈베리파이 카메라 이용

<h4>카메라 설정</h4>

* Interface Options

  * Legacy Camera -> Enable

<h4>카메라 이용 (기본 촬영)</h4>
  
    raspistill –o 파일명.jpg 

    libcamera-still –o 파일명.jpg 

<h4>카메라 이용 (계속 보기)</h4>

    libcamera-hello -t 0
