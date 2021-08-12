async def list(self, mc):
    a = "№(регулярное?, команда?). текст\n"
    for i, o in enumerate(self.all_db["word"]):
        a += str(i+1)+"("+str(o["re"])+", "+str(o["command"])+"). "+o["text"]+"\n"
    await mc.channel.send(a)