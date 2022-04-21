#Simple age trick script, whit discord webhook support!!

from discord_webhook import DiscordWebhook

me = "[Hector]#6969"
print("Hello my friend I guess you gotta answear all the qestions truly!!")
year = int(input("What year is it now for you?? (Numbers only)"))
print("Damn ALREADY???")
age100 = int(input("Add to your birtday date the number 100 and write it down here"))
age = year - (age100 - 100)
print("Damn you are only:", age)
print("MADE BY", me)

webhook = DiscordWebhook(url='your webhook in here', content=age)
response = webhook.execute()