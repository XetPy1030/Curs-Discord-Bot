import re, conf
async def delete(self, message):
    msg = str(message.content)[len(list(conf.cell_char)):]
    try:
        name = re.findall(r"text=(.*?);", msg)[0]
        for i in self.all_db["word"]:
            if i["text"] == name:
                self.all_db["word"].remove(i)
                await message.channel.send("Удалено")
    except:
        try:
            num = int(re.findall(r"num=(.*?);", msg)[0])
            self.all_db["word"].pop(num+1)
            await message.channel.send("Удалено")
        except Exception as a:
            print(a)