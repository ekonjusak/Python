# Python

1) ANN is folder with Artificial Neural Network that contains:


ANN1 - simple code that find our local database (nedded vehicles database: https://www.gti.ssr.upm.es/data/Vehicle_database.html ) and shows us how this pictures look in numbers. 

    - pictures converted in grayscale 
    
    -  reshaped for NN (neural network) and saved as pickle 
    


ANN2 - NN with 2 Conv layers 


ANN3 - training model + testing on pictures that are not from database 


needed : Python 3.6 

         pip install tensorflow, keras, pickle, numpy, os, cv2, matplotlib.pyplot


2) temperature 

emit_log.py - sending logs to rabbit mq ( https://www.rabbitmq.com/) 
recive_logs.py - create query on database and save time and temperature (that emit_log sends)

needed:  SQL database, Python 2.7, rabbit mq, tomcat 
          pip install pika, sqlite3, sys, time, json, request, tomcatmanager 


3) image processing basics 

some playing with images, nothing serious 
