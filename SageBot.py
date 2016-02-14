import discord #import discord.py library

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
      sagegeneral = client.get_channel('channelid')
      lvmsg = '{} is now playing {}'.format(after.name, after.game)
      await client.send_message(sagegeneral, lvmsg, tts=False)

#Run this if the bot is being started not as a master thread
if __name__ == '__main__':
      client.run('email', 'password') #Login using the discord client we initialised
