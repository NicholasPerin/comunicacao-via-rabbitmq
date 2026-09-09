"""Produtor de mensagens do RabbitMQ."""

from conexao_rabbitmq import conectar_rabbitmq
import time
import pika

# Chama a conexão com o RabbitMQ
connection = conectar_rabbitmq()
channel = connection.channel()

# Declara a queue de mensagens caso não exita
channel.queue_declare(queue="queue_de_mensagens")

# Enquanto producer estiver ativo, ficar enviando mensagens para a queue a cada 10 segundos
while True:
    try:
        time.sleep(10)

        # Mensagem a ser enviada
        channel.basic_publish(
            exchange="",
            routing_key="queue_de_mensagens",
            body="Esta é uma mensagem enviada pelo queue.",
        )
        print("Enviado!")

    except pika.exceptions.ConnectionClosed as e:
        print(f"""
              Erro:
              Código: {e.reply_code}
              Texto: {e.reply_text}
              """)
