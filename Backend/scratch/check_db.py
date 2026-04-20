import sys
import os
import asyncio

# Add parent directory to path to import core
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

async def run():
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    db = client[settings.DATABASE_NAME]
    n = await db['content'].count_documents({})
    u = await db['users'].count_documents({})
    print(f'Content: {n}, Users: {u}')
    
    # Check if there are any graph nodes
    gn = await db['graph_nodes'].count_documents({})
    print(f'Graph Nodes: {gn}')
    
    await client.close()

if __name__ == "__main__":
    asyncio.run(run())
