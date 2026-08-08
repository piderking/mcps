FROM node:22-slim

# Install supergateway and the Brave Search MCP server globally
RUN npm install -g supergateway @modelcontextprotocol/server-brave-search

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway wraps the stdio-based MCP server and exposes it over Streamable HTTP
CMD supergateway --port ${PORT} --stdio "npx @modelcontextprotocol/server-brave-search"
