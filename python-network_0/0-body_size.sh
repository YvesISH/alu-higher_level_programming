#!/bin/bash
# script that sends request and return the size of body response
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
