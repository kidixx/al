#!/bin/bash

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided by the user
url="$1"

# Use curl to fetch the URL and store the response in a variable
response=$(curl -s "$url")

# Get the size of the response body in bytes
size=$(echo -n "$response" | wc -c)

# Display the size of the response body
echo "Size of the response body: $size bytes"
