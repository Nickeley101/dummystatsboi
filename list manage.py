#open file with intent to add name, the '+' means to create a file if it doesnt exist
file = open("names.txt", 'a+')
#write the thing my guy
@client.event
async def on_message(message):
    if message.content.startswith('$cool'):
        await client.send_message(message.channel, 'Who is cool? Type $name namehere')

        def check(msg):
            return msg.content.startswith('$name')

        message = await client.wait_for_message(author=message.author, check=check)
        name = message.content[len('$name'):].strip()