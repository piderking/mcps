FROM python:3.12-slim

# Install system dependencies for Playwright / Chromium
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/* || true

# Install Node.js for supergateway
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install supergateway globally
RUN npm install -g supergateway

# Install crawl4ai, mcp, and playwright
RUN pip install --no-cache-dir crawl4ai mcp playwright && \
    playwright install --with-deps chromium || playwright install chromium

WORKDIR /app
COPY server.py .

ENV PORT=8080
EXPOSE ${PORT}

# Supergateway wraps stdio MCP server with CORS and exposes Streamable HTTP endpoint at /mcp
CMD supergateway --port ${PORT} --cors --outputTransport streamableHttp --stdio "python3 server.py"
