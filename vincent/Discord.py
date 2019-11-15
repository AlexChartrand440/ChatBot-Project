import discord
import sys # To store the sentimental value
import random # So that the bot can reply with multiple different messages
import Convo # File containing the list of responses
#import texblob - An alternative to writing out all the positive or negative inputs

# References used for help:
# https://www.digitaltrends.com/gaming/how-to-make-a-discord-bot/
# https://discordpy.readthedocs.io/en/latest/

# Discord bot creation from: https://www.devdungeon.com/content/make-discord-bot-python - Start 1
if __name__ == '__main__':


    #Sentimental Value
    thismodule = sys.modules[__name__] # Referenced from https://stackoverflow.com/questions/3089208/overwrite-global-var-in-one-line-in-python
    thismodule.sentimental = 100
    #If the sentimental value is below 100 he gives a negative response
    #If between 100 and 200 he acts neutral
    #If it's above 200 he will act friendly
    #Different inputs will influence the sentimental value, whether it's positive or negative.


    TOKEN = 'NjM4MDcyNDY3NTgzMTM5ODQx.XbXufA.A_WZV05ZddlbaLPW6tDU1XQA__E'

    client = discord.Client()

    channel = client.get_channel("638019246085111809")

    @client.event
    async def on_message(message):
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

# Discord bot creation from: https://www.devdungeon.com/content/make-discord-bot-python - End 1
        #general
        user = message.content.lower()
        msg = '{0.author.mention}'.format(message) # In case Trump wanted to @ the user on the Discord server

       #All if statements here are my own

# STRINGS CAN BE REPLACED WITH REGEX
        if "hello" in user or "hey" in user: # A greeting message is considered positive, raising sentimental value
            thismodule.sentimental = thismodule.sentimental + 50
            # Neutral/Positive
            if  thismodule.sentimental > 100:
                await message.channel.send(random.choice(Convo.hello))

            # Negative
            else:
                thismodule.sentimental = thismodule.sentimental - 25
                await message.channel.send(random.choice(Convo.helloneg))

        if "how" in user and "you" in user: # Asking how a person is, also considered positive
            thismodule.sentimental = thismodule.sentimental + 25
            #Positive
            if thismodule.sentimental >= 200:
                await message.channel.send(random.choice(Convo.howpos))

            #Neutral
            elif thismodule.sentimental >= 100 and thismodule.sentimental <= 200:
                await message.channel.send(random.choice(Convo.howneu))

            #Negative
            else:
                thismodule.sentimental = thismodule.sentimental - 25
                await message.channel.send(random.choice(Convo.howneg))

        if "hate" in user: # Using any sentence with hate is obviously considered negative
            thismodule.sentimental = thismodule.sentimental - 50
            #Positive
            if thismodule.sentimental >= 200:
                await message.channel.send(random.choice(Convo.hatepos))
            #Negative
            else:
                await message.channel.send(random.choice(Convo.hateneg))

        if "favourite" in user and "president" in user: # Positive message
            thismodule.sentimental = thismodule.sentimental + 50
            #Positive
            if thismodule.sentimental >= 200:
                await message.channel.send(random.choice(Convo.favppos))
            #Negative
            else:
                await message.channel.send(random.choice(Convo.favpneg))

        #SPECIFIC INFORMATION:

        if "birth" in user and "born" in user: # For more specific info about Donald Trump (always gives same response)
            msg = 'I was born on the 14th of June 1946'.format(message)
            await message.channel.send(msg)

        if ("who" in user and "wife" in user) or ("who" in user and "married" in user):
            msg = 'I am happily married to Melania Trump.'
            await message.channel.send(msg)

        #prototype testing sentiment values, Team member can add more by editing the "Convo.py" file for different responses
        #They can also create more if statements for specific info about Donald Trump e.g. who his wife is.


# Discord bot creation from: https://www.devdungeon.com/content/make-discord-bot-python - Start 2

    @client.event
    async def on_ready():
        print("It's me, the one and only")
        print(client.user.name)
        print(client.user.id)
        print('------')

    client.run(TOKEN)

# Discord bot creation from: https://www.devdungeon.com/content/make-discord-bot-python - End 2