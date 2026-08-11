FROM node:22-slim

# Install supergateway and the Brave Search MCP server globally
RUN npm install -g supergateway @modelcontextprotocol/server-brave-search

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway wraps stdio MCP with CORS over SSE transport at /sse
CMD supergateway --port ${PORT} --cors --stdio "npx @modelcontextprotocol/server-brave-search"
