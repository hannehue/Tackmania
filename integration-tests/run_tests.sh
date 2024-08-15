#! /bin/bash
docker compose -f ./docker-compose.yml --project-directory . up --build --exit-code-from test