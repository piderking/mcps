FROM node:22-slim

# Install supergateway and Google Maps MCP server globally
RUN npm install -g supergateway @modelcontextprotocol/server-google-maps

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway wraps stdio MCP server with CORS and exposes Streamable HTTP endpoint at /mcp
CMD supergateway --port ${PORT} --cors --outputTransport streamableHttp --stdio "mcp-server-google-maps"
