FROM python:3.12-slim

# Install Node.js for supergateway
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install supergateway globally
RUN npm install -g supergateway

# Install grubhub-mcp from PyPI
RUN pip install --no-cache-dir grubhub-mcp

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway wraps the stdio-based grubhub MCP and exposes Streamable HTTP at /mcp
CMD supergateway --port ${PORT} --outputTransport streamableHttp --stdio "grubhub"
