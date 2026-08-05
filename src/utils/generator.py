from uuid import uuid4

class IdGenerator:
  @staticmethod
  def uuid() -> str:
    return str(uuid4())

