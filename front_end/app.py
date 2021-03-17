from flask import Flask, render_template, request, redirect, url_for
import json
import pika
import time
app = Flask(__name__)

#main index landing page
@app.route('/')
def index():
    return render_template('index.html')

#login submit route
@app.route('/login', methods = ['POST', 'GET'])
def login():
    

    print("beginning of def login")

    #pulls username and password from form
    user = request.form['user']
    passwd = request.form['pass']

    #creates data dict for user and pass
    data = {}
    data['user'] = user
    data['passwd'] = passwd

    #creates the json object to be sent
    #json_data = json.dumps(data)

    #Opening Login Send Queue
    connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
    channel = connection.channel()
    channel.queue_declare(queue='login')

    channel.basic_publish(exchange='',
                  routing_key='login',
                  body=json.dumps(data),
                  properties=pika.BasicProperties(
                  delivery_mode = 2, # make message persistent
                  ))
    print(" [x] Sent 'Login Validation Request'")
    #Closing Login Send Queue
    connection.close()
    #return redirect(url_for('landing'))
    return

   
@app.route('/landing')
def landing():
    return render_template('login.html')