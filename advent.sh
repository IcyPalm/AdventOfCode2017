#!/bin/sh
docker run -it --rm --name adventofcode -v "$PWD":/usr/src/advent -w /usr/src/advent python:3 python $1