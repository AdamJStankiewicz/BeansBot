import json
import random
import discord

token_file = open("token.txt", "r")
TOKEN = token_file.read()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

user_data = {}

def init():
    try:
        with open('user_data.json', 'r') as openfile:
            global user_data
            user_data = json.load(openfile)
    except:
        with open('user_data.json', 'w') as outfile:
            outfile.write(json.dumps({}))

def save_user(id):
    id = str(id)
    global user_data
    if id in user_data:
        user_data[id] += 1
    else:
        user_data[id] = 0
    with open('user_data.json', 'w') as outfile:
        outfile.write(json.dumps(user_data))

def get_count(id):
    id = str(id)
    global user_data
    print(user_data)
    if id in user_data:
        return str(user_data[id])
    return str(0)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.content)
    if message.content.startswith('🫘'):
        file_obj = open("common.txt", "r")
        file_data = file_obj.read() 
        lines = file_data.splitlines()
        save_user(message.author.id)
        await message.channel.send(str(lines[random.randrange(0,len(lines)-1)] + " beans"))

    if message.content.startswith('/bean_count'):
        await message.channel.send(str("🫘 " + get_count(message.author.id)))

init()
client.run(TOKEN)