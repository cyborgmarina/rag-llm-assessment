# Network name
NETWORK_NAME="hotmart_challenge"

# Check if the network exists
if ! docker network ls | grep -q $NETWORK_NAME; then
	echo "Network $NETWORK_NAME does not exist. Creating it..."
	docker network create $NETWORK_NAME
else
	echo "Network $NETWORK_NAME already exists."
fi

# Run Docker Compose
docker-compose up
