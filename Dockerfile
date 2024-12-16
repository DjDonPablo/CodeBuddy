# Base image with Node.js
FROM node:22

# Install required dependencies
RUN apt-get update && apt-get install -y curl

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Set the working directory
WORKDIR /extension

# Copy your extension's source code into the container
COPY codebuddy-0.0.1.vsix ./codebuddy-0.0.1.vsix

# Install the extension locally (from the source)
RUN code-server --install-extension ./codebuddy-0.0.1.vsix --force

# Set the Python server URL as an environment variable
ENV PYTHON_SERVER_URL=http://host.docker.internal:8000

# Expose the code-server port
EXPOSE 8080

# Start code-server
CMD ["code-server", "--bind-addr", "0.0.0.0:8080", "--auth", "none"]
