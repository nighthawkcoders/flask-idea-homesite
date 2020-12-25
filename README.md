# How to start HomeSite on Raspberry Pi

## Setup Virtual environment and clone code from GitHub
#### In console/terminal (first time only: setup environment)...

pi@raspberrypi:~ $  ``` sudo apt install python3-pip nginx```

pi@raspberrypi:~ $  ``` sudo pip install virtualenv```

pi@raspberrypi:~ $  ``` cd ~; git clone https://github.com/nighthawkcoders/flask-idea-homesite```

pi@raspberrypi:~ $  ``` cd ~/flask-idea-homesite; virtualenv -p `which python3` homenv; source homenv/bin/activate```

pi@raspberrypi:~ $  ``` python -V```

pi@raspberrypi:~ $  ``` deactivate```



## Pull code from Github and update packages
#### In console/terminal (every time: pull and check package dependencies)...

pi@raspberrypi:~ $  ``` sudo apt update``

pi@raspberrypi:~ $  ``` sudo apt upgrade``

pi@raspberrypi:~ $  ``` cd ~/flask-idea-homesite```

pi@raspberrypi:~/flask-idea-homesite $ ```  git pull```

pi@raspberrypi:~/flask-idea-homesite $ ```  source flaskenv/bin/activiate```

(flaskenv) pi@raspberrypi:~/flask-idea-homesite $ ```  sudo pip3 install -r requirements.txt```



## Start Web Server and verify
#### Start test server

(flaskenv) pi@raspberrypi:~/flask-idea-homesite $ ``` python3 wsgi.py ``` 

in your browser ...
http://localhost:8080/ 
