from granian import Granian

def main():
  server = Granian(
    target="src.core.app:app",
    address="0.0.0.0",
    port=8000,
    interface="asgi"
  )

  server.serve()

