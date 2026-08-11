FROM python:3.12-slim

# Install Node.js for supergateway
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install supergateway globally
RUN npm install -g supergateway

# Install mcp, fastmcp, and grubhub-mcp from PyPI
RUN pip install --no-cache-dir "mcp>=1.2.0" "fastmcp>=0.1.0" grubhub-mcp

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway exposes Streamable HTTP with CORS at /mcp for Google Spark
CMD supergateway --port ${PORT} --cors --outputTransport streamableHttp --stdio "grubhub"
