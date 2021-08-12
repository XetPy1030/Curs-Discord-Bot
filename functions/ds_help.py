async def help(a, mc):
    aa = open("functions/texts/help.txt", "r")
    await mc.channel.send(aa.read())
    aa.close()