FROM node:22-slim

# Install supergateway and Google Maps MCP server globally
RUN npm install -g supergateway @modelcontextprotocol/server-google-maps

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway exposes Streamable HTTP with CORS at /mcp for Google Spark
CMD supergateway --port ${PORT} --cors --outputTransport streamableHttp --stdio "mcp-server-google-maps"
