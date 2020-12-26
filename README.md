# How to deploy this web site on Raspberry Pi

### [Digital Ocean reference article](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04)

## An application is typically written using a developer-friendly framework, this project is using Flask. The application code does not care about anything except being able to process single requests.  Thus, when we scale up to the Web we add small services to handle problems that are the same acroos most web applications.  A Python Web Server Gateway Interface (WSGI) is a way to make sure that web servers and python web applications can talk to each other. So somewhere inside your application (usually a wsgi.py file) an object is defined which can be invoked by Gunicorn (app).

## Gunicorn takes care of everything which happens in-between the web server and a the Flask web application. This way, when coding up a Flask application we don’t need to find your own solutions for:
<ol>
  <li>Communicating with multiple web servers</li>
  <li>Reacting to lots of web requests at once and distributing the load</li>
  <li>Keepiung multiple processes of the web application running</li>
</ol>

## Nginx is the web server:  it accepts requests, takes care of general domain logic and takes care of handling https connections. Only requests which are meant to arrive at the application are passed on toward the application server (Gunicorn) and the application itself (Flask). 

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


### Build Gunicorn configuration file.  Interesting bits...
<ol>
<li> 'ExecStart' start statement looks into wsgi:app (wsgi.py) and starts localhost:8080 as defined in file. </li>
<li> 'ExecStart' -workers 3 starts thread processes that are listening for connections, this ties into load balancing. </li>
</ol>
#### In console/terminal with nano, vi, or other text editor (first time only: setup Gunicorn configuration file)...

pi@raspberrypi:~ $  ``` sudo nano /etc/systemd/system/homesite.service```

    [Unit]
    Description=Gunicorn instance to serve homesite web project
    After=network.target

    [Service]
    User=pi
    Group=www-data
    WorkingDirectory=/home/pi/flask-idea-homesite
    Environment="PATH=/home/pi/flask-idea-homesite/homesite/bin"
    ExecStart=/home/pi/flask-idea-homesite/homesite/bin/gunicorn --workers 3 --bind unix:homesite.sock -m 007 wsgi:app

    [Install]
    WantedBy=multi-user.target

### Build Nginx configuration file.  Requirements and interesting bits...
<ol>
  <li> Obtain your own 'server_name' Internet Domain, Host IP address, Internet IP address.  These values will not work in you environment </li>
  <li> 'listen' is the port for nginx, this port will be used when you port forward </li>
  <li> 'proxy_pass' is passing connect along to gunicorn server </li>
</ol>
#### In console/terminal with nano, vi, or other text editor (first time only: setup Nginx configuration file)...

pi@raspberrypi:~ $  ``` sudo nano /etc/nginx/sites-available/homesite```

    server {
        listen 80;
        server_name nighthawkcoders.cf 192.168.1.245 70.95.179.231;

        location / {
            include proxy_params;
            proxy_pass http://unix:/home/pi/flask-idea-homesite/homesite.sock;
        }
    }


## Pull code from Github and update packages
#### In console/terminal (every update: pull code and check package dependencies)...

pi@raspberrypi:~ $  ``` sudo apt update; sudo apt upgrade```

pi@raspberrypi:~ $  ``` cd ~/flask-idea-homesite```

pi@raspberrypi:~/flask-idea-homesite $ ```  git pull```

pi@raspberrypi:~/flask-idea-homesite $ ```  source homesite/bin/activate```

#### In console/terminal with virtualenv activitate (every time: check and update packages)...

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```  sudo pip install -r requirements.txt```


## Start Flask test Server and verify
#### Start an application test server, same as we do on development machine

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` python wsgi.py ``` 

in your browser ...

http://localhost:8080/ 

stop test server by typing control-c in terminal

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` ^c ``` 


## Prepare for Gunicorn usage and verify
#### In console/terminal test Gunicorn test Server and virify (first time only: gunicor exectuion)...

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```homesite/bin/gunicorn --bind 0.0.0.0:8080 wsgi:app```

in your browser ...

http://localhost:8080/ 

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` ^c ``` 


## Validate Gunicorn configuration file and enable service permanently
#### In console/terminal start Gunicorn

pi@raspberrypi:~ $ ```sudo systemctl start homesite.service```

pi@raspberrypi:~ $ ```sudo systemctl enable homesite.service```
 
check the status...

pi@raspberrypi:~ $ ```sudo systemctl status homesite.service```

stop status by typing q in terminal


## Validate Nginx configuration file and enable service permanently
#### In console/terminal start Nginx

link file...

pi@raspberrypi:~ $ ```sudo ln -s /etc/nginx/sites-available/homesite /etc/nginx/sites-enabled```

test for errors...

pi@raspberrypi:~ $ ```sudo nginx -t```

start the web server...

pi@raspberrypi:~ $ ``sudo systemctl restart nginx```

check nginx status...

pi@raspberrypi:~ $ ``sudo systemctl status nginx```

stop status by typing q in terminal

in address bar of browser on another device in LAN type ip address of this Nginx server ...

http://192.168.1.245/

reboot to verify Nginx server config is permanent ...

next task is port forward Nginx server via public IP address on the internet ...
