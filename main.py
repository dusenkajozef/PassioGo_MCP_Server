from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv


load_dotenv()

mcp = FastMCP("passiogo-mcp-server")

USER_AGENT = "passiogo-agent/1.0"

def main():
    print("Hello from passiogo-mcp-server!")


if __name__ == "__main__":
    main()
