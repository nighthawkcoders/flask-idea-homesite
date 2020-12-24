# How to start HomeSite on Raspberry Pi

## Setup Virtual environment and clone code from GitHub
#### In console/terminal (first time: setup environment)...

pi@raspberrypi:~ $  ``` sudo pip install virtualenv```

pi@raspberrypi:~ $  ``` git clone https://github.com/nighthawkcoders/flask-idea-homesite```

pi@raspberrypi:~ $  ``` cd flask-idea-homesite```

pi@raspberrypi:~ $  ``` virtualenv flaskenv```


## Pull code from Github and update packages
#### In console/terminal (every time: pull and check package dependencies)...

pi@raspberrypi:~ $  ``` cd ~/flask-idea-homesite```

pi@raspberrypi:~/flask-idea-homesite $ ```  git pull```

pi@raspberrypi:~/flask-idea-homesite $ ```  source flaskenv/bin/activiate```

(flaskenv) pi@raspberrypi:~/flask-idea-homesite $ ```  sudo pip3 install -r requirements.txt```



## Verify Server runs successfully
#### Start test server

(flaskenv) pi@raspberrypi:~/flask-idea-homesite $ ``` python3 wsgi.py ``` 

in your browser ...
http://localhost:8080/ 
