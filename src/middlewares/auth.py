from fastapi import Request
from fastapi.responses import JSONResponse

from src.utils.jwt_helper import JWTHelper

public_endpoints = []

with open("public_endpoints.txt", "r") as f:
  public_endpoints = [
    line.strip() for line in f.readlines()
  ]

async def auth_middleware(request: Request, call_next):
  if request.method == "OPTIONS":
    return await call_next(request)

  if request.url.path in public_endpoints:
    return await call_next(request)

  token = request.headers.get("Authorization")

  if token is None or token.lower() == "bearer unauthorized":
    return JSONResponse(
      status_code=401,
      content={
        "detail": "Unauthorized",
      },
    )

  token = token.replace("Bearer ", "")

  if not JWTHelper.verify(token):
    return JSONResponse(
      status_code=401,
      content={
        "detail": "Unauthorized",
        "force_logout": True,
      },
    )

  token_data = JWTHelper.decode(token)
  user = token_data.get("user", {})

  if any([
    "user_id" not in user,
    "username" not in user,
    "phone_number" not in user,
  ]):
    return JSONResponse(
      status_code=401,
      content={
        "detail": "Unauthorized",
        "force_logout": True,
      },
    )

  request.state.user = user
  request.state.token = token
  request.state.token_data = token_data

  return await call_next(request)

