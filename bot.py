from pyrogram import Client
from pyrogram.errors import PeerIdInvalid, UserAlreadyParticipant
from config import API_HASH, API_ID, TG_BOT_TOKEN, SOURCE_CHANNEL_ID, DESTINATION_CHANNEL_ID

class Bot:
    def __init__(self, api_id, api_hash, bot_token, source_channel_id, destination_channel_id):
        self.api_id = API_ID
        self.api_hash = API_HASH
        self.bot_token = TG_BOT_TOKEN
        self.source_channel_id = SOURCE_CHANNEL_ID
        self.destination_channel_id = DESTINATION_CHANNEL_ID

        self.app = Client(
            "session_name",
            api_id=self.api_id,
            api_hash=self.api_hash,
            bot_token=self.bot_token
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


