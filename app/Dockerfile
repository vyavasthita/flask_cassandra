FROM diliplakshya/python-3.11.1-poetry-slim-bullseye as requirements-stage

WORKDIR /tmp

COPY pyproject.toml /tmp
COPY poetry.lock /tmp

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM diliplakshya/python-3.11.1-poetry-slim-bullseye

WORKDIR /app

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# Expose the port 5001 in which our application runs
EXPOSE 5001

# Copy requirements from host, to docker container in /app 
# COPY ./requirements.txt .
# Install the dependencies
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy everything from ./src directory to /app in the container
COPY main.py /app/main.py
COPY pyproject.toml .
COPY poetry.lock .

CMD ["python", "main.py"]
