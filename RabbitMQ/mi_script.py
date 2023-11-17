import pika

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# Declaración de la cola
channel.queue_declare(queue='mi_cola')

# Enviar mensajes a la cola
for i in range(1, 6):
    mensaje = f'Mensaje {i}'
    channel.basic_publish(exchange='', routing_key='mi_cola', body=mensaje)
    print(f'Se ha enviado: {mensaje}')

# Cerrar la conexión
connection.close()
