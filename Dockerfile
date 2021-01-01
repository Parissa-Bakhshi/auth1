FROM shared:latest


# we should do the installation of packages 1st, so each
# time the image is built, there is no need to rebuild this
# section again, only the code section will be rebuilt

COPY requirements.txt . 

RUN pip install -r requirements.txt

ARG APP_PORT=8000

ENV APP_PORT $APP_PORT
ENV APP_WORKERS 4

EXPOSE $APP_PORT

COPY . .

CMD ./start.sh