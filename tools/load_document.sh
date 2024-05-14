#!/bin/bash

# Check if the file path is provided as an argument
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <text-file-path>"
	exit 1
fi

# Check if the file exists
FILE_PATH=$1
if [ ! -f "$FILE_PATH" ]; then
	echo "File not found: $FILE_PATH"
	exit 1
fi

# Read the content of the file and escape necessary characters for JSON
DOCUMENT_TEXT=$(awk '{ gsub(/"/, "\\\""); gsub(/\n/, "\\n"); printf "%s", $0 }' "$FILE_PATH")

# Create JSON payload
JSON_PAYLOAD="{\"text\": \"$DOCUMENT_TEXT\"}"

# Send the request to the /document endpoint using --data-binary to handle the payload properly
RESPONSE=$(curl -s -X POST http://localhost:8001/api/document \
	-H "Content-Type: application/json" \
	--data-binary "$JSON_PAYLOAD")

# Print the response
echo "Response from ingestion API:"
echo "$RESPONSE"
