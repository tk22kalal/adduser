from bot import Bot

async def main():
    # Create an instance of the Bot class
    bot = Bot()

    # Run the add_users method
    await bot.start()
    await bot.add_users()
    await bot.stop()

# Run the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
