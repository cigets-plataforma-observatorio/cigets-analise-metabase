FROM python:3.7.9

# Instalar Dependências
RUN apt-get update && apt-get install -y \
    gcc \
    locales
RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales
RUN apt-get install -y --reinstall build-essential
RUN apt-get update &&  \
    apt-get install -y \
    build-essential \
    python3-dev \
    gcc


# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED 1
ENV LC_TIME "pt_BR.UTF-8"
ENV LC_ALL "pt_BR.UTF-8"

# Copiar todos os arquivos para o container
COPY . ./

# Configurar diretório de trabalho
WORKDIR ./

# Instalar dependências
RUN pip --default-timeout=30 install -r requirements.txt


# Atualizar a estrutura do banco e iniciar a aplicação
CMD python -m uvicorn api:app --reload --port 5025 --host 0.0.0.0