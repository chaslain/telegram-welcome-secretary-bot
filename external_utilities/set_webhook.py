import telegram

print("provide token")
token = input()
print("provide webhook url")
url = "https://vqclyfzjrf.execute-api.us-east-2.amazonaws.com/default/secretary-bot"

bot = telegram.Bot(token=token)

bot.set_webhook(url, allowed_updates=["MESSAGE"]) and print("Successfully updated")
