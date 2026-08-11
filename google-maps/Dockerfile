FROM node:22-slim

# Install supergateway and Google Maps MCP server globally
RUN npm install -g supergateway @modelcontextprotocol/server-google-maps

WORKDIR /app
COPY proxy.js .

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Proxy wraps supergateway and normalizes Accept headers for Google Spark compatibility
CMD ["node", "proxy.js", "mcp-server-google-maps"]
