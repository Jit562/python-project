from instabot import Bot

bot = Bot()

bot.login(username = "", password="")

bot.follow('instid')

bot.upload_photo("photopath",caption="any things")

bot.unfollow('instaid')

bot.send_message("type message", ["instaid"])

followers = bot.get_user_followers("userid")

for follow in followers:

    print(bot.get_user_info(follow))