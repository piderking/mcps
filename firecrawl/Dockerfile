FROM node:22-slim

# Install supergateway and firecrawl-mcp globally
RUN npm install -g supergateway firecrawl-mcp

# Railway injects PORT automatically
ENV PORT=8080

EXPOSE ${PORT}

# Supergateway wraps stdio MCP server and exposes Streamable HTTP endpoint at /mcp
CMD supergateway --port ${PORT} --outputTransport streamableHttp --stdio "firecrawl-mcp"
