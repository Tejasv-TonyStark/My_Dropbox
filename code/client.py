from server import storageServer

server = storageServer()

print(server.save_file("Hello.txt","Hello World from Client!!"))

print("Downloaded content:",server.read_file("Hello.txt"))

