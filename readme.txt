This telegram bot is configured to run in an AWS lambda container.


Please remember to specify the appropraite environment variables 
SECRETARY_BOT_TO_USER (user id (NOT USERNAME)) of who it will message
SECRETARY_BOT_TOKEN token telegram gives you

users cannot receive messages from the bot until they press /start with it, per telegram policy.

Future plans to remove the SECRETARY_BOT_TO_USER environment variable and have it configurable per group. Not today, though