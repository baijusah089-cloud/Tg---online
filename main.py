import asyncio
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateStatusRequest

# यहाँ पार्ट 1 वाले अपने असली कोड डालें
API_ID =        36015449
API_HASH = 'b340520249bf9f388c11dc512cbd6ayf8'

async def main():
    client = TelegramClient('my_session', API_ID, API_HASH)
    await client.start()
    print("Script started! You are now always online.")
    
    while True:
        try:
            await client(UpdateStatusRequest(offline=False))
            await asyncio.sleep(30)
        except Exception as e:
            print(f"Error: {e}")
            await asyncio.sleep(30)

if __name__ == '__main__':
    asyncio.run(main())
  
