# SAGEBOT DEVELOPMENT BUILD
# - Ability to Join Servers - Done
# - Command Enable/Disable Based on Server Topic Tags - Done
# - Constructed Help Command to Report Availiable Commands

import discord #import discord.py library
import random #import library for entropy in commands
import configparser #import library for reading config.ini

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
	if str(before.game) != str(after.game) and str(after.game) != 'None' and '[SB]' in before.server.default_channel.topic:
		lvmsg = '{} is now playing {}'.format(after.name, after.game)
		await client.send_message(before.server, lvmsg, tts=False)

#Handle chat commands
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if 'https://discord.gg/' in message.content and message.channel.is_private == True:
		await client.accept_invite(message.content[message.content.find('https://discord.gg/'):35+message.content.find('https://discord.gg/')])

	if message.content.startswith('.sbi_'):
		tmpimgtopost = message.content
		imgtopost = tmpimgtopost[5:]
		filetoread = 'commands/'+imgtopost+'.txt'
		image = random.choice(open(filetoread).readlines())
		await client.send_message(message.channel, image, tts=False)

#Run this if the bot is being started not as a master thread
if __name__ == '__main__':
	config = configparser.ConfigParser()
	config._interpolation = configparser.ExtendedInterpolation()
	config.read('config.ini')
	config.sections()
	print('=========\n=SAGEBOT=\n=========\nTHIS IS A DEVELOPMENT BUILD')
	client.run(config.get('DiscordClient', 'email'), config.get('DiscordClient', 'password')) #Login using the discord client we initialised
