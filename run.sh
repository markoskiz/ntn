#!/bin/bash

# Get the absolute directory path of the script
project_dir=$(dirname "$(readlink -f "$0")")

# Define the container name
container_name="feit-ai"

# Check if the container is running
if podman inspect -t container "$container_name" &>/dev/null; then
    # Container is running, stop and remove it
    echo "Stopping and removing existing container..."
    podman stop "$container_name"
    podman rm "$container_name"
fi

# Pull the latest image
echo "Pulling the latest image..."
podman pull registry.gitlab.com/feeit-freecourseware/ai

# Spin a new container
echo "Spinning a new container..."
podman run -it --rm -p 8888:8888 -v "$project_dir:/app:Z" --name "$container_name" registry.gitlab.com/feeit-freecourseware/ai

