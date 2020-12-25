# How to start HomeSite on Raspberry Pi

## Setup Virtual environment and clone code from GitHub
#### In console/terminal (first time only: setup environment)...

pi@raspberrypi:~ $  ``` sudo apt install python3-pip nginx```

pi@raspberrypi:~ $  ``` sudo pip3 install virtualenv```

pi@raspberrypi:~ $  ``` cd ~; git clone https://github.com/nighthawkcoders/flask-idea-homesite```

pi@raspberrypi:~ $  ``` cd ~/flask-idea-homesite; virtualenv -p `which python3` homesite; source homesite/bin/activate```

#### In console/terminal with virtualenv activitate (first time only: test for python3)...

(homesite) pi@raspberrypi:~ $  ``` python -V```

(homesite) pi@raspberrypi:~ $  ``` deactivate```

(homesite) pi@raspberrypi:~ $  ``` cd```



## Pull code from Github and update packages
#### In console/terminal (every time: pull and check package dependencies)...

pi@raspberrypi:~ $  ``` sudo apt update; sudo apt upgrade```

pi@raspberrypi:~ $  ``` cd ~/flask-idea-homesite```

pi@raspberrypi:~/flask-idea-homesite $ ```  git pull```

pi@raspberrypi:~/flask-idea-homesite $ ```  source homesite/bin/activate```

#### In console/terminal with virtualenv activitate (every time: check and update packages)...

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```  sudo pip install -r requirements.txt```



## Start Flask test Server and verify
#### Start test server

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` python wsgi.py ``` 

in your browser ...
http://localhost:8080/ 

#### Stop test server by type control-c in terminal where you started test Server

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` ^c ``` 



## Prepare Gunicorn for production Sever and verify
#### In console/terminal with nano, vi, or other editor (first time only: setup Gunicorn configuration file)...

pi@raspberrypi:~ $  ``` sudo nano /etc/systemd/system/flask-idea-homesite.service```

[Unit]
Description=Gunicorn instance to serve homesite web project
After=network.target

[Service]
User=pi
Group=www-data
WorkingDirectory=/home/pi/flask-idea-homesite
Environment="PATH=/home/pi/flask-idea-homesite/homesite/bin"
ExecStart=/home/pi/flask-idea-homesite/homesite/bin/gunicorn --workers 3 --bind unix:flask-idea-homesite.soc
k -m 007 wsgi:app

[Install]
WantedBy=multi-user.target


