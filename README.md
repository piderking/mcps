# MCP Servers on Railway

A monorepo hosting multiple [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) servers on [Railway](https://railway.app), each exposed over **Streamable HTTP** via [Supergateway](https://github.com/nichochar/supergateway).

## Services

| Service | Source | Description | Endpoint |
|---------|--------|-------------|----------|
| **brave-search** | [@modelcontextprotocol/server-brave-search](https://www.npmjs.com/package/@modelcontextprotocol/server-brave-search) | Web search via Brave Search API | `https://<service>.railway.app/mcp` |
| **crawl4ai** | [crawl4ai](https://pypi.org/project/crawl4ai/) | Open-source LLM-optimized web crawler & Playwright scraper | `https://<service>.railway.app/mcp` |
| **google-maps** | [@modelcontextprotocol/server-google-maps](https://www.npmjs.com/package/@modelcontextprotocol/server-google-maps) | Location search, directions, and place details via Google Maps API | `https://<service>.railway.app/mcp` |
| **grubhub** | [aserper/grubhub-mcp](https://github.com/aserper/grubhub-mcp) | Search restaurants, browse menus, manage cart, place orders | `https://<service>.railway.app/mcp` |
| **puppeteer** | [@modelcontextprotocol/server-puppeteer](https://www.npmjs.com/package/@modelcontextprotocol/server-puppeteer) | Browser automation using headless Chromium | `https://<service>.railway.app/mcp` |

## Architecture

Each service is a Docker container that:
1. Installs the underlying MCP server (npm package or pip package)
2. Runs [Supergateway](https://github.com/nichochar/supergateway) to bridge stdio → Streamable HTTP
3. Exposes a `/mcp` endpoint on Railway's assigned port

```
┌─────────────────────────────────────────────┐
│  Railway Service                            │
│                                             │
│  Supergateway (HTTP :$PORT)                 │
│       │                                     │
│       └── stdio ──▶ MCP Server              │
│                     (brave-search/crawl4ai/ │
│                      google-maps/grubhub/   │
│                      puppeteer)             │
│                                             │
│  Endpoint: https://svc.railway.app/mcp      │
└─────────────────────────────────────────────┘
```

## Setup

### 1. Clone & configure

```bash
git clone https://github.com/<your-username>/mcps.git
cd mcps
cp .env.example .env
# Edit .env with your API keys
```

### 2. Environment Variables

| Service | Variable | Required | Description |
|---------|----------|----------|-------------|
| brave-search | `BRAVE_API_KEY` | ✅ | Get from [brave.com/developers](https://search.brave.com/developers) |
| crawl4ai | *(none)* | — | Open-source, runs Playwright locally out-of-the-box |
| google-maps | `GOOGLE_MAPS_API_KEY` | ✅ | Get from [console.cloud.google.com](https://console.cloud.google.com) |
| grubhub | `GRUBHUB_EMAIL` | ⚠️ | Required for account access, cart & ordering |
| grubhub | `GRUBHUB_PASSWORD` | ⚠️ | Required for account access, cart & ordering |
| puppeteer | *(none)* | — | Runs headless Chromium out-of-the-box |

### 3. Deploy to Railway

1. Create a new project on [Railway](https://railway.app)
2. Connect this GitHub repo
3. Add services pointing to their subdirectories:
   - `brave-search/` → service name: `brave-search`
   - `crawl4ai/` → service name: `crawl4ai`
   - `google-maps/` → service name: `google-maps`
   - `grubhub/` → service name: `grubhub`
   - `puppeteer/` → service name: `puppeteer`
4. Set environment variables on each service
5. Railway auto-detects the Dockerfile and deploys

### 4. Connect to your MCP client

Use the Railway-assigned URLs in your MCP client config:

```json
{
  "mcpServers": {
    "brave-search": {
      "url": "https://brave-search-production-e850.up.railway.app/sse"
    },
    "crawl4ai": {
      "url": "https://crawl4ai-production-64f5.up.railway.app/sse"
    },
    "google-maps": {
      "url": "https://google-maps-production-4cff.up.railway.app/sse"
    },
    "grubhub": {
      "url": "https://grubhub-production.up.railway.app/sse"
    },
    "puppeteer": {
      "url": "https://puppeteer-production-88ab.up.railway.app/sse"
    }
  }
}
```

## Adding More MCP Servers

1. Create a new directory (e.g., `my-new-mcp/`)
2. Add a `Dockerfile` following the same pattern (install MCP + supergateway, wrap with `CMD`)
3. Add a new service in Railway pointing to the directory
4. Deploy

## License

MIT
