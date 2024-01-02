FROM python:3.8

RUN apt-get update && apt-get install -y nfs-common

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Crea el directorio /mnt/nfs
RUN mkdir -p /mnt/nfs/cuentas_banco1
# RUN chmod 777 /mnt/nfs/cuentas_banco1
RUN mkdir -p /mnt/nfs/cuentas_banco2
# RUN chmod 777 /mnt/nfs/cuentas_banco2
RUN mkdir -p /mnt/nfs/cuentas_banco3
# RUN chmod 777 /mnt/nfs/cuentas_banco3

# Monta el sistema de archivos NFS durante el CMD
# CMD ["sh", "-c", "echo $NFS_SERVER_IP:$NFS_SHARED_FOLDER && mount -v -t nfs -o vers=4,port=2049 $NFS_SERVER_IP:$NFS_SHARED_FOLDER /mnt/nfs/ && python manage.py runserver 0.0.0.0:8000"]
# Monta el sistema de archivos NFS durante el CMD
CMD ["sh", "-c", "echo NFS Client && \
                    echo IPs: $NFS_SERVER_IP_1 $NFS_SERVER_IP_2 $NFS_SERVER_IP_3 && \
                    echo dirs: $DIRECTORIO_NFS1 $DIRECTORIO_NFS2 $DIRECTORIO_NFS3 && \
                  mount -v -t nfs -o vers=4,port=2049,rw $NFS_SERVER_IP_1:/ $DIRECTORIO_NFS1 && \
                  mount -v -t nfs -o vers=4,port=2049,rw $NFS_SERVER_IP_2:/ $DIRECTORIO_NFS2 && \
                  mount -v -t nfs -o vers=4,port=2049,rw $NFS_SERVER_IP_3:/ $DIRECTORIO_NFS3 && \
                  python manage.py runserver 0.0.0.0:8000"]
