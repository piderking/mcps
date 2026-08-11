import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types
from crawl4ai import AsyncWebCrawler

server = Server("Crawl4AI")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="crawl_url",
            description="Crawl a webpage using Crawl4AI and return clean, LLM-optimized Markdown.",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "The web URL to crawl and convert to markdown."}
                },
                "required": ["url"]
            }
        ),
        types.Tool(
            name="extract_content",
            description="Scrape a page or extract specific DOM elements using CSS selectors.",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "The webpage URL to scrape."},
                    "css_selector": {"type": "string", "description": "Optional CSS selector to target specific DOM elements."}
                },
                "required": ["url"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    if not arguments:
        arguments = {}
    url = arguments.get("url", "")
    
    if name == "crawl_url":
        try:
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=url)
                if result.success:
                    return [types.TextContent(type="text", text=result.markdown)]
                else:
                    return [types.TextContent(type="text", text=f"Error crawling {url}: {result.error_message}")]
        except Exception as e:
            return [types.TextContent(type="text", text=f"Exception while crawling {url}: {str(e)}")]
            
    elif name == "extract_content":
        css_selector = arguments.get("css_selector")
        try:
            async with AsyncWebCrawler() as crawler:
                result = await crawler.arun(url=url, css_selector=css_selector)
                if result.success:
                    return [types.TextContent(type="text", text=result.markdown)]
                else:
                    return [types.TextContent(type="text", text=f"Error extracting content from {url}: {result.error_message}")]
        except Exception as e:
            return [types.TextContent(type="text", text=f"Exception while extracting content from {url}: {str(e)}")]

    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
