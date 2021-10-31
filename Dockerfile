FROM python:3.9-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY server/requirements.txt .
RUN pip install -r requirements.txt

# # Run the application:
COPY server/app.py .
CMD ["python3", "server/app.py"]


# Advice from Python society
# start with only dockerfile
# use both commands for running app (so node js + python app.py)
# & (for running multiple commands)
# fg (foreground)
# web client - run with node js
# use docker
# docker compose
