import sqlite3
import pika



connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    conn=sqlite3.connect('temperatura.db')
    c=conn.cursor()
    c.execute("INSERT INTO temperatura(TEMPERATURE) VALUES(?)",(body,))
    conn.commit()
    c.close()
    conn.close()
    print(body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
