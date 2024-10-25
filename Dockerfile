# Base install conda but use mamba for package install. Faster with mamba.
FROM continuumio/miniconda3:24.7.1-0

# Set root container for now
USER root

# Update image info. Specifically need nano to edit/troubleshoot/debug and need httpie for api requests.
RUN apt=get update && apt-get install -y nano httpie

# Change working directory
WORKDIR /home/assist/app/lm-assist

# Verify conda and use proper channels for package install.
RUN conda --version
RUN conda config --remove channels defaults
RUN conda config --set channel_priority flexible

# Get env file and create env from it.
COPY ./env.yml ./
RUN mamba env create -n assist_env --file ./env.yml

# Copy code over.
COPY . .

# Activate env
SHELL ["conda", "run", "-n", "assist_env", "/bin/bash", "-c"]
ENV PATH /opt/conda/envs/assist_env/bin:$PATH

# Use ports for communication and api calls.
#EXPOSE 11434
EXPOSE 7777

# Needs to be changed dynamically. Do later but for now get from docker network's gateway.
ENV OLLAMA_HOST http://xxx.xx.x.x:11434

# Start server with 2 workers for now.
CMD ["gunicorn", "-b", "0.0.0.0:7777", "--access-logfile", "-", "--workers=2", "--timeout=24000", "app:app"]