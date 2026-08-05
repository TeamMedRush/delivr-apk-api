from functools import wraps

from inspect import signature

from os import getenv

from time import perf_counter

from traceback import format_tb

from src.core.analytics import Analytics

SYSTEM_USER_ID = getenv("SYSTEM_USER_ID", "system")
ENVIRONMENT = getenv("ENVIRONMENT", "production")

def track_perf(func):
  @wraps(func)
  async def wrapper(*args, **kwargs):
    start = perf_counter()

    try:
      return await func(*args, **kwargs)
    finally:
      duration = perf_counter() - start
      Analytics.track_event(
        SYSTEM_USER_ID,
        "endpoint_duration",
        {
          "endpoint": func.__name__,
          "duration": duration,
        },
      )

  wrapper.__signature__ = signature(func)

  return wrapper

def track_error(error: Exception):
  if ENVIRONMENT == "development":
    print(f"Error: {error}")

  Analytics._track(
    SYSTEM_USER_ID,
    event_name="unhandled_error",
    properties={
      "error_type": str(type(error).__name__),
      "error_message": str(error),
      "stack_trace": "".join(format_tb(error.__traceback__)),
    }
  )

