"""Consumidor de mensagens do RabbitMQ."""

from conexao_rabbitmq import conectar_rabbitmq

# Chama a conexão com o RabbitMQ
connection = conectar_rabbitmq()
channel = connection.channel()

# Declara a queue de mensagens caso não exita
channel.queue_declare(queue="queue_de_mensagens")


def callback(ch, method, properties, body):
    """
    Executado automaticamente pela bilbioteca "pika" a cada mensagem recebida na fila.
    ch: canal usado para enviar ack/nack.
    method: contém o delivery_tag, necessário para confirmar a mensagem.
    body: conteúdo da mensagem recebida.
    """

    try:
        print(f"Mensagem recebida: {body}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print(f"Falha: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


# Aguarda o recebimento de mensagens na queue. Após cada uma, rodar a função callback()
channel.basic_consume(queue="queue_de_mensagens", on_message_callback=callback)
print("Aguardando mensagens...")
channel.start_consuming()
