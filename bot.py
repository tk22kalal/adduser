from pyrogram import Client
from pyrogram.errors import PeerIdInvalid, UserAlreadyParticipant

api_id = '24316517'
api_hash = 'ab33479d43c662f11cf9ae4b26350709'
bot_token = '6922414869:AAEZ4iSuI2eTiLwlGDGbT-_h_18951vxgNM'

# Replace these with the actual numeric IDs of your private channels
source_channel_id = -1001845192858
destination_channel_id = -1002121021005

from pyrogram import Client
from pyrogram.errors import PeerIdInvalid, UserAlreadyParticipant

app = Client("session_name", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

async def add_users():
    async with app:
        try:
            # Get information about the source channel
            source_channel = await app.get_chat(source_channel_id)

            # Get information about the destination channel
            destination_channel = await app.get_chat(destination_channel_id)

            # Check if the bot is an admin in both channels
            source_admin = await app.get_chat_member(source_channel.id, app.get_me().id)
            destination_admin = await app.get_chat_member(destination_channel.id, app.get_me().id)

            if source_admin.status == "administrator" and destination_admin.status == "administrator":
                # Get all the members from the source channel
                members = await app.get_chat_members(source_channel.id)

                # Add each member to the destination channel
                for member in members:
                    try:
                        await app.add_chat_members(destination_channel.id, member.user.id)
                        print(f"Added user {member.user.id} to the destination channel.")
                    except UserAlreadyParticipant:
                        print(f"User {member.user.id} is already in the destination channel.")
                    except Exception as e:
                        print(f"Error adding user {member.user.id} to the destination channel: {e}")

        except PeerIdInvalid:
            print("Invalid source or destination channel ID.")

if __name__ == '__main__':
    app.run(add_users)
