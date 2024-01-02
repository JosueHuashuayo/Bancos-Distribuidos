import Pyro4
import threading
import time


def atomic(func):
    def wrapper(*args, **kwargs):
        if "cuenta_id" not in kwargs:
            raise ValueError("El parámetro 'cuenta_id' es necesario para el decorador synchronized.")
        mutex_key = kwargs["cuenta_id"]

        with Pyro4.Proxy("PYRO:central_server@192.168.1.18:50000") as central_server:
            central_server.request_cs(mutex_key)
            while not central_server.can_enter_cs(mutex_key):
                time.sleep(1)
            central_server.request_cs(mutex_key)

            try:
                result = func(*args, **kwargs)
            finally:
                central_server.release_cs(mutex_key)

            return result
    return wrapper