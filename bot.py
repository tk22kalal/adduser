from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import PeerIdInvalid, UserAlreadyParticipant
from config import ADMINS, API_HASH, API_ID, TG_BOT_TOKEN

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=TG_BOT_TOKEN,
        )
        self.source_channel_id = None
        self.destination_channel_id = None
        self.admin_user_id = None

    async def start(self):
        print("Bot started. Please forward a message from the source channel.")
        await super().start()

    async def process_forward(self, message: Message):
        user_id = message.from_user.id

        if not self.is_admin(user_id):
            print(f"User {user_id} is not authorized to configure the bot.")
            return

        if not message.forward_from_chat:
            print("Please forward a message from a channel.")
            return

        chat_id = message.forward_from_chat.id

        if not self.source_channel_id:
            print(f"Source Channel ID set to: {chat_id}")
            self.source_channel_id = chat_id
            print("Please forward a message from the destination channel.")
        elif not self.destination_channel_id:
            print(f"Destination Channel ID set to: {chat_id}")
            self.destination_channel_id = chat_id
            print("Configuring complete. Adding users from the source channel to the destination channel.")

            try:
                # Get information about the source channel
                source_channel = await self.get_chat(self.source_channel_id)

                # Get information about the destination channel
                destination_channel = await self.get_chat(self.destination_channel_id)

                # Check if the bot is an admin in both channels
                source_admin = await self.get_chat_member(source_channel.id, (await self.get_me()).id)
                destination_admin = await self.get_chat_member(destination_channel.id, (await self.get_me()).id)

                if source_admin.status == "administrator" and destination_admin.status == "administrator":
                    self.admin_user_id = user_id
                    print(f"Both source and destination channels are configured. Starting to add users from the source channel to the destination channel.")

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

        else:
            print("Both source and destination channels are already configured.")

    async def on_message(self, message: Message):
        if message.text and message.text.lower() == '/start' and message.from_user.id == self.admin_user_id:
            await self.start_configuration(message)
        else:
            await self.process_forward(message)

    async def start_configuration(self, message: Message):
        print(f"User {message.from_user.id} started the configuration process.")
        print("Please forward a message from the source channel.")

if __name__ == "__main__":
    bot = Bot()
    bot.run(bot.start)
