#!/usr/bin/env bash

# Build image and add a descriptive tag
docker build --tag=cmd-agent .

# List docker images
docker image ls

# Run flask app
docker run -p 9000:9000 predict
