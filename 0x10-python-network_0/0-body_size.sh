#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL
#and displays the size of the body

curl -sI "$1"| grep 'Content-Length' | gerp -o '[0-9]\+'
