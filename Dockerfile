# Pega a image pré-montada de Python
FROM python:3.12-slim

# Diretório em uso
WORKDIR /app

# Instala as dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante para a imagem
COPY . .

# Garante que os métodos print() são exibidos corretamente no terminal,
# visto que normalmente são mantidos no buffer
ENV PYTHONUNBUFFERED=1
