from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannel
from telethon.tl.types import InputChannel

api_id = '24316517'
api_hash = 'ab33479d43c662f11cf9ae4b26350709'
bot_token = '6922414869:AAEZ4iSuI2eTiLwlGDGbT-_h_18951vxgNM'

source_channel_username = 'source_channel_username'
destination_channel_username = 'destination_channel_username'

client = TelegramClient('session_name', api_id, api_hash)

async def add_users():
    async with client:
        # Get information about the source channel
        source_channel = await client.get_entity(source_channel_username)

        # Get information about the destination channel
        destination_channel = await client.get_entity(destination_channel_username)

        # Check if the bot is an admin in both channels
        source_admin = await client.get_permissions(source_channel)
        destination_admin = await client.get_permissions(destination_channel)

        if source_admin.is_creator and destination_admin.is_creator:
            # Get all the participants from the source channel
            participants = await client.get_participants(source_channel)

            # Add each participant to the destination channel
            for participant in participants:
                try:
                    await client(InviteToChannel(destination_channel, [InputChannel(participant.id, participant.access_hash)]))
                    print(f"Added user {participant.id} to the destination channel.")
                except Exception as e:
                    print(f"Error adding user {participant.id} to the destination channel: {e}")

if __name__ == '__main__':
    client.loop.run_until_complete(add_users())
