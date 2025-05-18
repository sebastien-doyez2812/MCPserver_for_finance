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

@mcp.tool()
def stock_info(ticker: str) -> str:
    """This tool returns information about a given stock given it's ticker.
    Args:
        stock_ticker: a alphanumeric stock ticker
        Example payload: "IBM"

    Returns:
        str:information about the company
        Example Respnse "Background information for IBM: {'address1': 'One New Orchard Road', 'city': 'Armonk', 'state': 'NY', 'zip': '10504', 'country': 'United States', 'phone': '914 499 1900', 'website': 
            'https://www.ibm.com', 'industry': 'Information Technology Services',... }" 
    """
    dat = yf.Ticker(ticker)
    return f"Background information for {ticker}: {dat.info}"

@mcp.tool()
def income_statement(ticker:str) -> str:
    """This tool returns the quarterly income statement for a given stock ticker.
    Args:
        stock_ticker: a alphanumeric stock ticker
        Example payload: "BOA"

    Returns:
        str:quarterly income statement for the company
        Example Respnse "Income statement for BOA: 
        Tax Effect Of Unusual Items                           76923472.474289  ...          NaN
        Tax Rate For Calcs                                            0.11464  ...          NaN
        Normalized EBITDA                                        4172000000.0  ...          NaN
    """
    
    dat = yf.ticker(ticker)

    return f"Background info for {ticker}: {dat.quarterly_income_stmt}"


@mcp.prompt()
def stock_summary(ticker: str) -> str:
    """ This prompt returns a summary of a given stock ticker.
    Args:
        ticker: a alphanumeric stock ticker
        Example payload: "NVDA"

    Returns:
        str:summary of the stock ticker
    """
    return """
    You are a financial analyst.
    You are given a stock ticker.
    You need to return the last known price for the stock ticker.
    """
if __name__ == "__main__":
    mcp.run(transport="stdio")