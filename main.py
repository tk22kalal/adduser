# main.py

from bot import Bot

async def main():
    bot = Bot()
    await bot.start()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
