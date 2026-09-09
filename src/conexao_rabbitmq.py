"""Lida com a conexão ao RabbitMQ dentro do Docker."""

import os
import time
import pika


def conectar_rabbitmq():
    """Método para conectar ao RabbitMQ."""

    # Define a variável de ambiente
    host = os.environ.get("RABBITMQ_HOST", "localhost")

    # Realiza as tentativas de conexão ao RabbitMQ, visto que ela nem sempre inicializa antes
    # de producer e consumer. Após 10 tentaivas, joga um erro
    for tentativa in range(10):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host))
            return connection
        except pika.exceptions.AMQPConnectionError:
            print(f"RabbitMQ não está pronto, tentando novamente... ({tentativa+1}/10)")
            time.sleep(3)
    else:
        raise Exception("Não foi possível conectar ao RabbitMQ.")
