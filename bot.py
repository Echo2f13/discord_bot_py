import random
import discord
import os
from discord.ext import commands
#google-api-python-client library, grtting build class
from googleapiclient.discovery import build

# imported discord module
# from discord.ext brought out the commands.

intents = discord.Intents.all()
# intnts.members = True
# intnts.message_content = True

# introducing new veriable for client input "c"
c = commands.Bot(command_prefix='$', intents=intents)
# commands.Bot will envoke the bot and command_prefix is the the command that we have to use to envoke the bot.

#apikey
api_key='AIzaSyDT88ZeDKlcoCtdo9xl8U3dgAC2PdxUF1o'

# creating events that bot needs to perform
# when_ready is a async function which will be triggered once the bot is running. [agenda of the the when_ready function]
@c.event
async def on_ready():
    print(f'Logged in as {c.user} (ID: {c.user.id})')

#help function
@c.command()
async def bothelp(ctx):
    embededtext = discord.Embed(title='prefix *$* \n3 main commands \n$ass\n$boobs\n$search <search> \n   (this search any image)\nclear')
    await ctx.send(embed=embededtext)
    # await ctx.send('prefix *$* \n3 main commands \n-ass\nboobs\nshow <search> \n   (this search any image)\nclear')

#command for boobs pics
@c.command()
async def boobs(ctx):
    pics = ['https://navbharattimes.indiatimes.com/thumb/83635834/boobs-press-83635834.jpg?imgsize=204959&width=540&height=405&resizemode=75', 'https://static-ca-cdn.eporner.com/gallery/BH/2V/aCUpqSl2VBH/1021284-sexy-boobs-nude.jpg',
            'https://static-ca-cdn.eporner.com/gallery/CH/86/IDeUMMg86CH/975623-sexy-boobs-nude.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ73y9_jQn1gd7ADinuAeJS-nYVBU9tJJml8Q&usqp=CAU']
    await ctx.send(f'{random.choice(pics)}')

#command for ass pics
@c.command()
async def ass(ctx):
    pics = ['https://cdn77-pic.xvideos-cdn.com/videos/thumbs169ll/07/00/fd/0700fd9a787b6430c96d7264e6a10eb0/0700fd9a787b6430c96d7264e6a10eb0.15.jpg', 'https://myteenwebcam.com/thefapp/thumbs/jpgs/ec93847680f38c04f765f48be73458db.jpg', 'https://i1.sndcdn.com/avatars-0jtLzt9YsDBn47zm-eyfVlw-t500x500.jpg',
            'http://sc04.alicdn.com/kf/Hba934e21d39d4bea8b7e5fe1c3e0f7c7c.jpg', 'https://ei.phncdn.com/videos/202101/10/381460282/thumbs_5/(m=eGNdHgaaaa)(mh=a5PpqN1-WT_QpWcl)12.jpg', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmvIf9o6pSqgZdxC1ofRtqeiCzCcZRTrl9Sw&usqp=CAU']
    await ctx.send(f'{random.choice(pics)}')

#command for google image search, with $search <search>
@c.command(aliases=["search"])
async def showpic(ctx, *, search):
    r = random.randint(0, 9)
    #resource veriable envokes the api which is connects to my google cloud [custom search api]
    #.cse is the module inside build, [build.cse]
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    #resource veriable get the module from resource [resource.list.execute]
    #list is the templete, where cx is the apikey
    result = resource.list(
        q=f"{search}", cx="a0039021d66464b64", searchType="image"
    ).execute()
    #url generates the image url
    #result is what we get
    url = result["items"][r]["link"]
    #embed1 veriable envokes the class 'discord.Embed' to make the embed
    embed1 = discord.Embed()
    #using 'url' as object
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)

#command to clear text
@c.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


# to run the event
c.run('MTA1MDA3ODUzODI0NzcwNDY2Ng.GN5L_0.ddF2vPXGoAwq_TiigCpbYV5c2ju-nLi4BW_60c')
# the token of the bot is placed in the clients event run as a string
