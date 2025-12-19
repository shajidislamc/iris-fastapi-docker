from fastapi import FastAPI
import asyncio
import time


app = FastAPI(title="Async vs Sync Demo")

@app.get("/sync")
def sync_endpoint():
    """
    Simulates a CPU-bound blocking task by doing heavy computation.
    This will block the event loop when called concurrently.
    """
    count = 0
    for _ in range(10**8): # heavy computation
        count += 1
    return {"message": "Synchronous task completed", "count": count}

@app.get("/async")
async def async_endpoint():
    """
    Simulates an I/O-bound non-blocking task using asyncio.sleep.
    This will not block the event loop and can handle concurrent requests efficiently.
    """
    await asyncio.sleep(5)  # Simulate a non-blocking I/O operation
    return {"message": "Asynchronous task completed"}