# Build from a slim python base
FROM python:3.9-slim-bullseye

# define working directory
WORKDIR /app

# set environment variable
ENV FLASK_APP=market
ENV FLASK_DEBUG=0
ENV VIRTUAL_ENV=/venv

# create a virtual environment and activate it by adding its bin to the PATH variable
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# intall app dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Export the port the application will listen on
EXPOSE 5000

# Copy application code
COPY . .

# Run our Python script
CMD ["python3", "run.py"]