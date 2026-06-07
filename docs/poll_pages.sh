#!/usr/bin/env bash
# Poll the GitHub Pages site until it returns HTTP 200 or attempts exhausted
URL="https://howarddalerapp.github.io/ARGUS/"
TRIES=10
SLEEP=30
echo "Polling $URL up to $TRIES times (every $SLEEP seconds)..."
for i in $(seq 1 $TRIES); do
  status=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
  echo "[$i/$TRIES] HTTP $status"
  if [ "$status" = "200" ]; then
    echo "Pages site is live: $URL"
    exit 0
  fi
  sleep $SLEEP
done
echo "Pages did not return 200 after $TRIES attempts. Check GitHub Pages settings or wait a few more minutes."
exit 1
