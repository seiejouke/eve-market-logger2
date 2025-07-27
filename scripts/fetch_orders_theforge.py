import aiohttp
import asyncio
import pandas as pd
from datetime import datetime, timezone

region_id = 10000002
output_dir = 'output'
delay = 1.2
url = f"https://esi.evetech.net/latest/markets/{region_id}/orders/"

async def fetch_dummy_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={"order_type": "all", "page": 1}) as resp:
            resp.raise_for_status()
            data = await resp.json()
            print(f"Fetched {len(data)} orders on page 1")

            for order in data[:3]:
                print(order)

            df = pd.DataFrame(data)
            df.to_csv("forge_orders_dummy_data.csv", index=False)
            print("Saved sample page to forge orders_page1.csv")
    
if __name__ == "__main__":
    asyncio.run(fetch_dummy_data())