from os import getenv

from time import time

from jwt import encode, decode

secret = getenv("JWT_SECRET_KEY")

class JWTHelper:
  def encode(
    payload: dict,
    expiry: float = 864000,
    algorithm: str = "HS256",
  ) -> str:
    data = payload.copy()
    data["exp"] = time() + expiry

    return encode(data, secret, algorithm=algorithm)

  def verify(
    token: str,
    algorithm: str = "HS256",
  ) -> bool:
    try:
      data = decode(
        token,
        secret,
        algorithms=[algorithm],
      )

      if not data.get("exp") or data.get("exp") < int(time()):
        return False
    except Exception:
      return False

    return True

  def decode(
    token: str,
    algorithm: str = "HS256",
  ) -> dict:
    return decode(
      token,
      secret,
      algorithms=[algorithm],
    )

