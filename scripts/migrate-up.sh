#!/bin/sh

if [ -z "$1" ]; then
  echo "Usage: ./migrate <message>"
  exit 1
fi

set -a
. .env
set +a

alembic revision --autogenerate -m "$1"
cutypy migrations
alembic upgrade head

