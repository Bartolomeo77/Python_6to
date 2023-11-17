import pika

# Función para procesar mensajes
def procesar_mensaje(ch, method, properties, body):
    print(f'Se ha recibido y procesado el mensaje: {body}')

# Conexión a RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaración de la cola
channel.queue_declare(queue='mi_cola')

# Configuración del consumidor
channel.basic_consume(queue='mi_cola', on_message_callback=procesar_mensaje, auto_ack=True)

print('Esperando mensajes. Para salir, presiona CTRL+C')
# Iniciar la recepción de mensajes
channel.start_consuming()
