FROM node:22-slim

# Install supergateway and Google Maps MCP server globally
RUN npm install -g supergateway @modelcontextprotocol/server-google-maps

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway wraps stdio MCP with CORS over SSE transport at /sse
CMD supergateway --port ${PORT} --cors --stdio "mcp-server-google-maps"
