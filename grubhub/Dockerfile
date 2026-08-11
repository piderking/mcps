FROM python:3.12-slim

# Install Node.js for supergateway
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install supergateway globally
RUN npm install -g supergateway

# Install mcp (1.x branch for mcp.server.fastmcp compatibility) and grubhub-mcp
RUN pip install --no-cache-dir "mcp>=1.2.0,<2.0.0" "fastmcp>=0.1.0" grubhub-mcp

WORKDIR /app
COPY proxy.js .

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Proxy wraps supergateway and normalizes Accept headers for Google Spark compatibility
CMD ["node", "proxy.js", "grubhub"]
