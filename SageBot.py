import discord #import discord.py library
import random #import library for entropy in commands

client = discord.Client() #Initialise a discord client

#Report if connection was successful and ready for commands
@client.event
async def on_ready():
	print('Connected!')
	print('Username: ' + client.user.name)
	print('ID: ' + client.user.id)

#Report if someone starts playing a game
@client.event
async def on_member_update(before, after):
	if str(before.game) != str(after.game) and str(after.game) != 'None':
		sagegeneral = client.get_channel('channel'))
		lvmsg = '{} is now playing {}'.format(after.name, after.game)
		await client.send_message(sagegeneral, lvmsg, tts=False)

#Handle chat commands
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content =='.debug_random_image':
		sagegeneral = client.get_channel('channel'))
		line = random.choice(open('debug_random_image.txt').readlines())
		print("Debug: ",line)
		await client.send_message(sagegeneral, line, tts=False)




#Run this if the bot is being started not as a master thread
if __name__ == '__main__':
	print('=========\n=SAGEBOT=\n=========\nTHIS IS A DEVELOPMENT BUILD')
	client.run('email', 'password') #Login using the discord client we initialised
