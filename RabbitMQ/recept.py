import numpy as np
import pandas as pd
import pika

def binary_to_pandas_and_receive(queue_name, num_rows=10):
    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue=queue_name)

    # Callback function to handle received messages
    def callback(ch, method, properties, body):
        data = np.fromstring(body.decode('utf-8'), dtype=np.int32, sep=',')
        df = pd.DataFrame(data.reshape(-1, 3), columns=['userId', 'movieId', 'rating'])
        print("Received data:")
        print(df.head(num_rows))

    # Set up the consumer
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    # Start consuming messages
    print(f"Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

# Example usage
binary_to_pandas_and_receive('movie_ratings_queue', num_rows=10)
