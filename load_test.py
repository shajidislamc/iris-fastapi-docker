import asyncio
import time
import httpx

URL = "http://127.0.0.1:7860"

async def call_sync():
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.get(f"{URL}/sync")
        return response.json()
async def call_async():
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.get(f"{URL}/async")
        return response.json()
    
async def run_many_calls(endpoint_func, name, n = 5):
    print(f"Starting {n} calls to {name} endpoint")
    start = time.time()
    results = await asyncio.gather(*[endpoint_func() for _ in range(n)])
    total_time = time.time() - start
    print(f"Completed {n} calls to {name} endpoint in {total_time:.2f} seconds")
    for i, result in enumerate(results):
        print(f"Result {i+1} from {name} endpoint: {result}")
        
async def main():
    await run_many_calls(call_sync, "SYNC", n=5)
    await run_many_calls(call_async, "ASYNC", n=5)

if __name__ == "__main__":
    asyncio.run(main())