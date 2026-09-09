# Serviço de mensageria Cliente-Servidor via RabbitMQ

Teste de uso de Docker com Python.

Necessário usar [Docker Desktop](https://www.docker.com/products/docker-desktop/) para rodar o RabbitMQ. Caso esteja usando o Windows como sistema operacional, verifique os [requisitos operacionais](https://docs.docker.com/desktop/setup/install/windows-install/).

Em um terminal dentro do projeto, use:

```bash
docker compose up --build
```

Para acessar o RabbitMQ na web, digite na barra de endereço: `localhost:15672`

```text
Username: guest
Password: guest
```

A cada 10 segundos, o `producer` envia uma mensagem ao queue, do qual o `consumer` irá receber e confirmar pelo terminal.
Se `consumer` estiver inativo enquanto `producer` está ativo, as mensagens se acumulam na queue até `consumer` ficar ativo novamente.

Para parar todo o processo:

```bash
docker compose down
```

> Feito para o curso de Bacharelado em Engenharia da Computação do [Centro Universitário Fundação Santo André](https://www2.fsa.br/home/).
