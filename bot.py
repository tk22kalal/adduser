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
            bot_token=TG_BOT_TOKEN,
            # Remove source_channel_id and destination_channel_id from here
        )
        
        # Set source_channel_id and destination_channel_id as attributes
        self.source_channel_id = SOURCE_CHANNEL_ID
        self.destination_channel_id = DESTINATION_CHANNEL_ID

    async def add_users(self):
        try:
            # Get information about the source channel
            source_channel = await self.get_chat(self.source_channel_id)

            # Get information about the destination channel
            destination_channel = await self.get_chat(self.destination_channel_id)

            # Check if the bot is an admin in both channels
            source_admin = await self.get_chat_member(source_channel.id, self.get_me().id)
            destination_admin = await self.get_chat_member(destination_channel.id, self.get_me().id)

            if source_admin.status == "administrator" and destination_admin.status == "administrator":
                # Get all the members from the source channel
                members = await self.get_chat_members(source_channel.id)

                # Add each member to the destination channel
                for member in members:
                    try:
                        await self.add_chat_members(destination_channel.id, member.user.id)
                        print(f"Added user {member.user.id} to the destination channel.")
                    except UserAlreadyParticipant:
                        print(f"User {member.user.id} is already in the destination channel.")
                    except Exception as e:
                        print(f"Error adding user {member.user.id} to the destination channel: {e}")

        except PeerIdInvalid:
            print("Invalid source or destination channel ID.")

# Create an instance of the Bot class
bot = Bot()

# Run the add_users method
await bot.start()
await bot.add_users()
await bot.stop()
