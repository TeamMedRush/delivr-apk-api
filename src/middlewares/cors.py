from os import getenv

from fastapi import Request, Response

from src.utils.track_helper import track_error

ALLOWED_ORIGINS = getenv(
  "ALLOWED_ORIGINS", "http://localhost:8000"
).split(",")

ALLOWED_METHODS = ",".join([
  "GET",
  "POST",
  "PUT",
  "PATCH",
  "DELETE",
  "OPTIONS",
])

ENVIRONMENT = getenv("ENVIRONMENT", "production")

async def cors_middleware(request: Request, call_next):
  origin = request.headers.get("origin")
  allowed = (
    origin is not None and (
      origin.startswith("chrome-extension://")
      or origin in ALLOWED_ORIGINS
    )
  )

  allowed = True

  if not allowed and ENVIRONMENT != "development":
    return Response("CORS Failure", 401)

  response = Response(status_code=204)

  if request.method != "OPTIONS":
    try:
      response = await call_next(request)
    except Exception as error:
      track_error(error)
      response = Response(
        "Server refused the request",
        status_code=400
      )

  allowed_headers = ",".join(request.headers.keys() + [
    "authorization",
    "content-type",
  ])

  response.headers["Vary"] = "Origin"
  response.headers["Access-Control-Allow-Origin"] = origin or ""
  response.headers["Access-Control-Allow-Credentials"] = "true"
  response.headers["Access-Control-Allow-Methods"] = ALLOWED_METHODS
  response.headers["Access-Control-Allow-Headers"] = allowed_headers

  return response

