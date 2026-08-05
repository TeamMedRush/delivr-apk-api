set -a
[ -f .env ] && source .env
set +a

python3 -m $DEV_APP $@

