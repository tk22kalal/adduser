from bot import Bot

bot = Bot(
    api_id='24316517',
    api_hash='ab33479d43c662f11cf9ae4b26350709',
    bot_token='6922414869:AAEZ4iSuI2eTiLwlGDGbT-_h_18951vxgNM',
    source_channel_id=-1001845192858,
    destination_channel_id=-1002121021005
)
bot.app.run(bot.add_users)

