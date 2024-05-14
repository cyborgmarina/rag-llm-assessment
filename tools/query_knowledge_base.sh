#!/bin/bash

# Check if jq is installed
if ! command -v jq &>/dev/null; then
	echo "jq is required but it's not installed. Please install jq and try again."
	exit 1
fi

# Check if the query string is provided as an argument
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <query-string>"
	exit 1
fi

# Get the query string and escape necessary characters for JSON
QUERY_STRING=$(echo "$1" | sed 's/"/\\"/g')

# Create JSON payload
JSON_PAYLOAD="{\"question\": \"$QUERY_STRING\"}"

# Send the request to the /retrieval endpoint and extract assistantResponse
RESPONSE=$(curl -s -X POST http://localhost:8002/api/retrieval \
	-H "Content-Type: application/json" \
	--data-binary "$JSON_PAYLOAD")

echo "#####"
echo "#####"
echo "Context from Knowledge Base:"
echo "$RESPONSE" | jq -r '.context'
echo "#####"
echo "#####"
echo "#####"
echo "#####"
echo "Assistant Response:"
echo "$RESPONSE" | jq -r '.assistantResponse'
echo "#####"
echo "#####"
