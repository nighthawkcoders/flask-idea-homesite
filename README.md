# How to start HomeSite on Raspberry Pi
## An application is typically written using a developer-friendly framework, this project is using Flask. The application code does not care about anything except being able to process single requests.  Thus, when we scale up to the Web we add small services to handle problems that are the same acroos most web applications.  A Python Web Server Gateway Interface (WSGI) is a way to make sure that web servers and python web applications can talk to each other. So somewhere inside your application (usually a wsgi.py file) an object is defined which can be invoked by Gunicorn (app).

## Gunicorn takes care of everything which happens in-between the web server and a the Flask web application. This way, when coding up a Flask application we don’t need to find your own solutions for:
<ol>
  <li>Communicating with multiple web servers</li>
  <li>Reacting to lots of web requests at once and distributing the load</li>
  <li>Keepiung multiple processes of the web application running</li>
</ol>

## Nginx takes is the web server:  it accepts requests, takes care of general domain logic and takes care of handling https connections. Only requests which are meant to arrive at the application are passed on toward the application server (Gunicorn) and the application itself (Flask). 

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



## Prepare for a production Sever and verify
### [Digital Ocean reference article](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)
#### In console/terminal test Gunicorn test Server and virify (first time only: gunicor exectuion)...

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```homesite/bin/gunicorn --bind 0.0.0.0:8080 wsgi:app```

in your browser ...
http://localhost:8080/ 

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` ^c ``` 


#### In console/terminal with nano, vi, or other editor (first time only: setup Gunicorn configuration file)...

pi@raspberrypi:~ $  ``` sudo nano /etc/systemd/system/homesite.service```

[Unit]
Description=Gunicorn instance to serve homesite web project
After=network.target

[Service]
User=pi
Group=www-data
WorkingDirectory=/home/pi/flask-idea-homesite
Environment="PATH=/home/pi/flask-idea-homesite/homesite/bin"
ExecStart=/home/pi/flask-idea-homesite/homesite/bin/gunicorn --workers 3 --bind unix:homesite.soc
k -m 007 wsgi:app

[Install]
WantedBy=multi-user.target


