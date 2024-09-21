FROM python:3.10-slim

RUN mkdir /project

COPY requirements.txt /project

RUN pip3 install -r/project/requirements.txt --no-cache-dir

RUN pip3 install aerich

COPY ./app/ /project/app
COPY ./.env/ /project

WORKDIR /project

#CMD ["uvicorn", "app.main:app", "--reload"]
#CMD["gunicorn", "project.wsgi:application", "--bind", "0:8000"]