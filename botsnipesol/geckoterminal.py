import asyncio
from geckoterminal_api import AsyncGeckoTerminalAPI

# Initialize the async GeckoTerminal API
gt_async = AsyncGeckoTerminalAPI()

# Define an asynchronous function to fetch trending pools
async def fetch_trending_pools():
    try:
        # Fetch trending pools for the base network
        trending_pools = await gt_async.network_trending_pools(network="eth")
        
        # Print the structure of the first trending pool data
        if trending_pools.get('data', []):
            first_pool = trending_pools['data'][0]
            print("First pool data structure:")
            print(first_pool)
        else:
            print("No trending pools available.")
    
    except Exception as e:
        print(f"Error fetching data: {e}")

# Define the main entry point for the asyncio event loop
async def main():
    await fetch_trending_pools()

# Run the asynchronous loop
if __name__ == "__main__":
    asyncio.run(main())
