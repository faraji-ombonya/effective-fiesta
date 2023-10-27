#!/usr/bin/env python
import pika
import sys
import json
import email.em as e
import sms.sm as s
import whatsapp.wh as w
import telegram.tg as t


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost',
                              port='5672'))
channel = connection.channel()

channel.exchange_declare(exchange='miniature_umbrella', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

outbound_channels = sys.argv[1:]
if not outbound_channels:
    sys.stderr.write("Usage: %s [sms] [whatsapp] [email]\n" % sys.argv[0])
    sys.exit(1)

for outbound_channel in outbound_channels:
    channel.queue_bind(
        exchange='miniature_umbrella', queue=queue_name, routing_key=outbound_channel)

print(' [*] Waiting for messages. To exit press CTRL+C')


handlers = {
    "email":e.email_handler,
    "sms":s.sms_handler,
    "whatsapp": w.whatsapp_handler,
    "telegram":t.telegram_handler,
}

def callback(ch, method, properties, body):
    notification = json.loads(body)
    handlers[method.routing_key](notification)
    # print(f" [x] {method.routing_key}:{body}")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()