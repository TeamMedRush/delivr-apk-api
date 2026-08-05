set -a
. .env
set +a

alembic "$@"
cutypy migrations

