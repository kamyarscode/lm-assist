#FROM continuumio/miniconda3:24.7.1-0
FROM nvidia/cuda:12.6.0-cudnn-devel-ubuntu22.04

# Allow install to continue without interaction.
ENV DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get update && apt-get install -y nano curl net-tools pciutils wget plocate

# Update image:
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb \
    && dpkg -i cuda-keyring_1.1-1_all.deb \
    && apt-get update && apt-get install -y nano curl net-tools pciutils linux-headers-generic gnupg gnupg2 software-properties-common

# Update image for Nvidia drivers. 
RUN curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
    && chmod 644 /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    #&& apt purge nvidia-* \
    #&& apt-add-repository ppa:graphics-drivers/ppa \
    && apt-get update && apt-get autoremove && apt search nvidia-driver-550 && apt-get install -y nvidia-container-toolkit nvidia-driver-550

    #&& apt-get install -y ubuntu-drivers-common nvidia-container-toolkit nvidia-driver-560


# Copy language model server install script.
COPY lmserver_install.sh /home
RUN /home/lmserver_install_install.sh

# Ollama API runs on 11434. Must use these 2 lines, otherwise it won't work when making API calls. 
EXPOSE 11434
ENV OLLAMA_HOST=0.0.0.0


#CMD tail -f /dev/nullCMD # use for debugging container when crashing.

# CMD to install llama3.1 and 3.1 instruct.
CMD ["/bin/sh", "-c", "/usr/local/bin/ollama serve & sleep 5 && /usr/local/bin/ollama pull llama3.1:8b-instruct-q8_0 && /usr/local/bin/ollama pull llama3.1:8b & wait"]
