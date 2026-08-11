FROM node:22-slim

# Install Chromium and system dependencies for Puppeteer
RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    fonts-liberation \
    libnss3 \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# Configure Puppeteer to use installed Chromium
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

# Install supergateway and the Puppeteer MCP server globally
RUN npm install -g supergateway @modelcontextprotocol/server-puppeteer

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway exposes Streamable HTTP with CORS at /mcp for Google Spark
CMD supergateway --port ${PORT} --cors --outputTransport streamableHttp --stdio "mcp-server-puppeteer"
