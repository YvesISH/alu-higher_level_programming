#!/bin/bash
# script that sends request and return the size of the body response
curl s-I $1 | grep "content-Length" | cut -d " " -f2
