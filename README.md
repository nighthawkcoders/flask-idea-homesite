# How to start HomeSite on Raspberry Pi

## Setup Virtual environment and clone code from GitHub
#### In console/terminal (first time only: setup environment)...

pi@raspberrypi:~ $  ``` sudo apt install python3-pip nginx```

pi@raspberrypi:~ $  ``` sudo pip3 install virtualenv```

pi@raspberrypi:~ $  ``` cd ~; git clone https://github.com/nighthawkcoders/flask-idea-homesite```

pi@raspberrypi:~ $  ``` cd ~/flask-idea-homesite; virtualenv -p `which python3` homesite; source homesite/bin/activate```

#### In console/terminal (first time only: test for python3 version in virtual env)...

(homesite) pi@raspberrypi:~ $  ``` python -V```

(homesite) pi@raspberrypi:~ $  ``` deactivate```



## Pull code from Github and update packages
#### In console/terminal (every time: pull and check package dependencies)...

pi@raspberrypi:~ $  ``` sudo apt update; sudo apt upgrade```

pi@raspberrypi:~ $  ``` cd ~/flask-idea-homesite```

pi@raspberrypi:~/flask-idea-homesite $ ```  git pull```

pi@raspberrypi:~/flask-idea-homesite $ ```  source homesite/bin/activiate```

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ```  sudo pip install -r requirements.txt```



## Start Flask development Server and verify
#### Start test server

(homesite) pi@raspberrypi:~/flask-idea-homesite $ ``` python wsgi.py ``` 

in your browser ...
http://localhost:8080/ 
