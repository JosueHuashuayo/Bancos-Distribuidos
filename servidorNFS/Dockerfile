FROM ubuntu:latest

# Instalar el servidor NFS
RUN apt-get update && apt-get install -y nfs-kernel-server

# Crear un sistema de archivos para compartir
RUN mkdir /shared_folder

RUN chmod -R 777 /shared_folder

# Configurar el servidor NFS
RUN echo "/shared_folder *(rw,sync,no_subtree_check,insecure)" >> /etc/exports

# Iniciar el servidor NFS
CMD ["sh", "-c", "echo 'Starting NFS Server...'; service nfs-kernel-server start; tail -f /dev/null"]
