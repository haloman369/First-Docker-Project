import pika
import time

print ("Hello sleeping.....")
time.sleep(60)

connection = pika.BlockingConnection(pika.ConnectionParameters('messaging'))
channel = connection.channel()
channel.queue_declare(queue='hello')

while(True):
	time.sleep(60)
	channel.basic_publish(exchange='',
                      	routing_key='hello',
                      	body='Hello World!')
	print(" [x] Sent 'Hello World!'")


connection.close()

