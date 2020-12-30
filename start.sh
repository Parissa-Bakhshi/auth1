#!/bin/bash
echo "Running application tests"
for _ in {1..10}; do
    flask app test >> /dev/null
    rc=$?
    if [ $rc -eq 0 ]; then
        break
    fi 
    sleep 10
done

if [ $rc -ne 0 ]; then
    echo "Application tests failed!"
    exit 1
fi

flask db upgrade

echo "Starting application"

if [ -z "$AUTH1_DEBUG" ]; then # if it is in debug mode log-level=debug
    gunicorn -b 0.0.0.0:$APP_PORT \  #define env in docker file
        -w $APP_WORKERS \
        --access-logfile - \
        --error-logfile - "auth1:create_app()"
else   
   gunicorn -b 0.0.0.0:$APP_PORT \
        -w $APP_WORKERS \
        --access-logfile - \
        --log-level debug \
        --error-logfile - "auth1:create_app()" 
fi
