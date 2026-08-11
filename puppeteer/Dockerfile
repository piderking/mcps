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

WORKDIR /app
COPY proxy.js .

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Proxy wraps supergateway and normalizes Accept headers for Google Spark compatibility
CMD ["node", "proxy.js", "mcp-server-puppeteer"]
