import conf, discord
import re as ree
async def set(self, message):
    msg = str(message.content)[len(list(conf.cell_char)):]
    re = len(ree.findall(r"re=1;", msg))>0
    command = False
    text = ree.findall(r"text=(.*?);", msg)[0].lower()
    repl = ree.findall(r"repl=(.*?);", msg)[0]
    a = {"re": re, "command": command, "text": text, "repl": repl}
    b = False
    for i in self.all_db["word"]:
        if i["text"] == a["text"]:
            i = a
            await message.channel.send("Обновлено успешно")
            b = True
    if not b:
        self.all_db["word"].append(a)
        await message.channel.send("Добавлено успешно")