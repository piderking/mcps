from mcp.server.fastmcp import FastMCP
from crawl4ai import AsyncWebCrawler

mcp = FastMCP("Crawl4AI")

@mcp.tool()
async def crawl_url(url: str) -> str:
    """Crawl a webpage using Crawl4AI and return clean, LLM-optimized Markdown."""
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        if result.success:
            return result.markdown
        return f"Error crawling {url}: {result.error_message}"

@mcp.tool()
async def extract_content(url: str, css_selector: str | None = None) -> str:
    """Scrape a page or extract specific DOM elements using CSS selectors."""
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, css_selector=css_selector)
        if result.success:
            return result.markdown
        return f"Error extracting content from {url}: {result.error_message}"

if __name__ == "__main__":
    mcp.run()
