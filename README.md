# MCP Servers on Railway

A monorepo hosting multiple [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) servers on [Railway](https://railway.app), each exposed over **Streamable HTTP** via [Supergateway](https://github.com/nichochar/supergateway).

## Services

| Service | Source | Description | Endpoint |
|---------|--------|-------------|----------|
| **brave-search** | [@modelcontextprotocol/server-brave-search](https://www.npmjs.com/package/@modelcontextprotocol/server-brave-search) | Web search via Brave Search API | `https://<service>.railway.app/mcp` |
| **grubhub** | [aserper/grubhub-mcp](https://github.com/aserper/grubhub-mcp) | Search restaurants, browse menus, manage cart, place orders | `https://<service>.railway.app/mcp` |

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
│                     (brave-search / grubhub) │
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
| grubhub | *(none)* | — | Search/browse works without auth |

### 3. Deploy to Railway

1. Create a new project on [Railway](https://railway.app)
2. Connect this GitHub repo
3. Add **two services**, each pointing to its subdirectory:
   - `brave-search/` → service name: `brave-search`
   - `grubhub/` → service name: `grubhub`
4. Set environment variables on each service
5. Railway auto-detects the Dockerfile and deploys

### 4. Connect to your MCP client

Use the Railway-assigned URLs in your MCP client config:

```json
{
  "mcpServers": {
    "brave-search": {
      "url": "https://brave-search-production-XXXX.up.railway.app/mcp"
    },
    "grubhub": {
      "url": "https://grubhub-production-XXXX.up.railway.app/mcp"
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
