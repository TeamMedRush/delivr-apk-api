from datetime import datetime

from os import getenv

from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse

from src.core.analytics import Analytics
from src.middlewares.cors import cors_middleware

ALLOWED_ORIGINS = getenv(
  "ALLOWED_ORIGINS", "http://localhost:8000"
).split(",")

ENVIRONMENT = getenv("ENVIRONMENT", "production")
is_development = ENVIRONMENT == "development"
app = FastAPI(
  docs_url="/docs" if is_development else None,
  redoc_url="/redoc" if is_development else None,
  openapi_url="/openapi.json" if is_development else None,
)

app.middleware("http")(cors_middleware)

@app.get("/")
async def app_root():
  return "Hello, Delivr APK Server!"

@app.get("/ping")
async def ping():
  time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  return f"Active! Received: {time}"

@app.get("/favicon.ico")
async def favicon():
  with open("logo.png", "rb") as f:
    return Response(
      content=f.read(),
      media_type="image/png",
    )

@app.get("/robots.txt")
async def robots():
  with open("robots.txt", "r") as f:
    return Response(
      content=f.read(),
      media_type="text/plain",
    )

@app.get("/health")
async def health_check():
  Analytics.track_user_profile(
    getenv("SYSTEM_USER_ID", "system"),
    {
      "username": "system",
    },
  )

  return { "api": True }

@app.get("/latest")
async def download_latest():
  def stream_apk():
    with open("downloads/latest.apk", "rb") as file:
      while chunk := file.read(1024 * 1024):
        yield chunk

  return StreamingResponse(
    content=stream_apk(),
    media_type="application/vnd.android.package-archive",
    headers={
      "Content-Disposition": "attachment; filename=delivr.apk"
    },
  )

