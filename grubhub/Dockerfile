FROM python:3.12-slim

# Install Node.js for supergateway
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install supergateway globally
RUN npm install -g supergateway

# Install mcp and grubhub-mcp from PyPI
RUN pip install --no-cache-dir "mcp[cli]" grubhub-mcp

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway wraps stdio MCP with CORS over SSE transport at /sse
CMD supergateway --port ${PORT} --cors --stdio "grubhub"
