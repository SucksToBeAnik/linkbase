FROM python:latest AS build

WORKDIR /app

# Install build dependencies for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Dev stage
FROM python:slim AS dev

# Install PostgreSQL client libraries
RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

# Copy the dependencies and app from the build stage
COPY --from=build /usr/local /usr/local
COPY --from=build /app .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# Prod stage
FROM python:slim AS prod

# Install PostgreSQL client libraries
RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

# Copy the dependencies and app from the build stage
COPY --from=build /usr/local /usr/local
COPY --from=build /app .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
