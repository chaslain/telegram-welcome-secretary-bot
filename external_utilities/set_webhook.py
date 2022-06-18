import telegram

print("provide token")
token = input()
print("provide webhook url")
url = input()

bot = telegram.Bot(token=token)

bot.set_webhook(url) and print("Successfully updated")
