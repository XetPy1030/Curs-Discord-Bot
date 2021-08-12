import discord, re, conf

async def command_call(self, message, i):
    await i["repl"](self, message, i)

async def reply(self, message, i):
    if i["command"]:
        await command_call(self, message, i)
    else:
        await message.channel.send(i["repl"])

async def reply_re(self, message, i):
    if i["command"]:
        await command_call(self, message, i)
    else:
        msg = str(message.content)[len(list(conf.bot_word)):]
        res = i["repl"]
        res = res.replace(r"[{bot}]", f"<@!{str(self.user.id)}>")
        res = res.replace(r"[{author}]", f"<@!{message.author.id}>")
        lis = re.findall("<@!\d{18}>", msg)
        for n, t in enumerate(lis):
            try:
                res = res.replace(r"[{"+str(n)+"}]", t)
            except:
                continue
        await message.channel.send(res)


"""
self.all_db = {"accounts":{}, "word": [{"re": False, "command": False, "text": "надеюсь", "repl": "что будет писать бот взамен"}]}
self.all_db = {"accounts":{}, "word": [{"re": True, "command": False, "text": r"awdwad <@!\d{18}> надеюсь", "repl": "что будет писать [{bot}] взамен"}]}
[{bot}]
[{author}]
[{0}]




"""