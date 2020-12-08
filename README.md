# homesite

## How to Run on Raspberry Pi

in console/terminal...

pi@raspberrypi:~ $  ``` git clone https://github.com/nighthawkcoders/flask-idea-homesite```
pi@raspberrypi:~ $  ``` cd flask-idea-homesite```


establish virtual environment...

pi@raspberrypi:~/flask-idea-homesite $ ```  source homesitenv/bin/activate ```


in virtual environment...

(homesitenv) pi@raspberrypi:~/flask-idea-homesite $ ```
``` pip install -r requirements.txt ``` (install dependencies)

(homesitenv) pi@raspberrypi:~/flask-idea-homesite $ ```
``` python3 wsgi.py ``` (runs from entry point)

in your browser ...
http://localhost:8080/ 
