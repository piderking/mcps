FROM node:22-slim

# Install supergateway and the Brave Search MCP server globally
RUN npm install -g supergateway @modelcontextprotocol/server-brave-search

WORKDIR /app
COPY proxy.js .

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Proxy wraps supergateway and normalizes Accept headers for Google Spark compatibility
CMD ["node", "proxy.js", "npx @modelcontextprotocol/server-brave-search"]
