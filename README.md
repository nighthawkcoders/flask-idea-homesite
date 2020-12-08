# How to start HomeSite on Raspberry Pi

## Pull code from GitHub
#### In console/terminal (first time: clone)...

pi@raspberrypi:~ $  ``` git clone https://github.com/nighthawkcoders/flask-idea-homesite```

pi@raspberrypi:~ $  ``` cd flask-idea-homesite```



#### In console/terminal (after clone: pull)...

pi@raspberrypi:~ $  ``` cd flask-idea-homesite```

pi@raspberrypi:~/flask-idea-homesite $ ```  git pull



## Establish virtual environment
#### Set virtual environment...
pi@raspberrypi:~/flask-idea-homesite $ ```  source homesitenv/bin/activate ```


## Make sure dependencies are up to date
#### In virtual environment...

(homesitenv) pi@raspberrypi:~/flask-idea-homesite $ ```
``` pip install -r requirements.txt ``` (install dependencies)



## Verify Server runs successfully
#### Start test server

(homesitenv) pi@raspberrypi:~/flask-idea-homesite $ ```
``` python3 wsgi.py ``` 

in your browser ...
http://localhost:8080/ 
