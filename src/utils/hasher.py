from bcrypt import checkpw, gensalt, hashpw

class SecretHasher:
  @staticmethod
  def hash_secret(data: str) -> str:
    return hashpw(
      data.encode(),
      gensalt()
    ).decode()

  @staticmethod
  def verify_hash(data: str, hashed_data: str) -> bool:
    return checkpw(
      data.encode(),
      hashed_data.encode()
    )

