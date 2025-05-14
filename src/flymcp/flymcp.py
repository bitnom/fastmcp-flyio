import logging
from fastmcp import FastMCP
import logging
import uvicorn

# Create FastMCP server instance
mcp = FastMCP("YouTube Transcript & Metadata Server")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@mcp.tool()
def test_tool() -> str:
    """
    A test tool that returns a string.

    Returns:
        A test string
    """
    return "This is the test result string."


def main():
    http_app = mcp.http_app(transport="streamable-http", path="/mcp")
    uvicorn.run(http_app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()