import yfinance as yf
from colorama import Fore

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("trading_server")




@mcp.tool()
def trading_server(ticker: str) -> str:
    """This tool returns the last known price for a given stock ticker.
    Args:
        ticker: a alphanumeric stock ticker 
        Example payload: "NVDA"

    Returns:
        str:"ticker: Last Price" 
        Example Respnse "NVDA: $100.21" 
    """
    dat = yf.Ticker(ticker)
    historical_prices = dat.history(period = '1mo')
    close_data = historical_prices['Close']

    print(f"{Fore.YELLOW}{close_data}")
    return str(f"Stock price over the last month for {ticker}: {close_data}")


if __name__ == "__main__":
    mcp.run(transport="stdio")