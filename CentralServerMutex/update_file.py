import Pyro4

@Pyro4.expose
class CentralServer:
    def __init__(self):
        self.mutexes = {}

    def request_cs(self, key):
        if key not in self.mutexes:
            self.mutexes[key] = []
        self.mutexes[key].append(True)
        return True

    def release_cs(self, key):
        if key in self.mutexes and self.mutexes[key]:
            self.mutexes[key].pop(0)
            return True
        return False

    def can_enter_cs(self, key):
        return key in self.mutexes and self.mutexes[key] and self.mutexes[key][0]

def main():
    central_server = CentralServer()
    daemon = Pyro4.Daemon(host="0.0.0.0", port=50000)
    uri = daemon.register(central_server, objectId="central_server")
    print("Central Server URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
