FROM ubuntu:22.04

# install dependencies

COPY . /app

WORKDIR /app

# install python
RUN apt-get update && apt-get install -y python3 python3-pip 

# install python dependencies
RUN pip3 install -r requirements.txt

# i think this is useless
EXPOSE 8000

# run the application (fastapi with uvicorn file server.py)
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]