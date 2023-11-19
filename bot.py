from pyrogram import Client
from pyrogram.errors import PeerIdInvalid, UserAlreadyParticipant
from config import API_HASH, API_ID, TG_BOT_TOKEN, SOURCE_CHANNEL_ID, DESTINATION_CHANNEL_ID

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
            source_channel_id = SOURCE_CHANNEL_ID,
            destination_channel_id = DESTINATION_CHANNEL_ID
        )

    async def add_users(self):
        async with self.app:
            try:
                # Get information about the source channel
                source_channel = await self.app.get_chat(self.source_channel_id)

                # Get information about the destination channel
                destination_channel = await self.app.get_chat(self.destination_channel_id)

                # Check if the bot is an admin in both channels
                source_admin = await self.app.get_chat_member(source_channel.id, self.app.get_me().id)
                destination_admin = await self.app.get_chat_member(destination_channel.id, self.app.get_me().id)

                if source_admin.status == "administrator" and destination_admin.status == "administrator":
                    # Get all the members from the source channel
                    members = await self.app.get_chat_members(source_channel.id)

                    # Add each member to the destination channel
                    for member in members:
                        try:
                            await self.app.add_chat_members(destination_channel.id, member.user.id)
                            print(f"Added user {member.user.id} to the destination channel.")
                        except UserAlreadyParticipant:
                            print(f"User {member.user.id} is already in the destination channel.")
                        except Exception as e:
                            print(f"Error adding user {member.user.id} to the destination channel: {e}")

            except PeerIdInvalid:
                print("Invalid source or destination channel ID.")

bot = Bot()

# Run the add_users method
bot.run(bot.add_users)

