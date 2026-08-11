import asyncio
from mcp.server.fastmcp import FastMCP
from crawl4ai import AsyncWebCrawler

mcp = FastMCP("Crawl4AI")

@mcp.tool()
async def crawl_url(url: str) -> str:
    """Crawl a webpage using Crawl4AI and return clean, LLM-optimized Markdown.

    Args:
        url: The web URL to crawl and convert to markdown.
    """
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url)
            if result.success:
                return result.markdown
            else:
                return f"Error crawling {url}: {result.error_message}"
    except Exception as e:
        return f"Exception while crawling {url}: {str(e)}"

@mcp.tool()
async def extract_content(url: str, css_selector: str = None) -> str:
    """Scrape a page or extract specific DOM elements using CSS selectors.

    Args:
        url: The webpage URL to scrape.
        css_selector: Optional CSS selector to target specific DOM elements.
    """
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url, css_selector=css_selector)
            if result.success:
                return result.markdown
            else:
                return f"Error extracting content from {url}: {result.error_message}"
    except Exception as e:
        return f"Exception while extracting content from {url}: {str(e)}"

if __name__ == "__main__":
    mcp.run()
