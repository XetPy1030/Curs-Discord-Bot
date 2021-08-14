import conf, discord, pickle, check
import functions
from functions import davay as kilogrammm
import reply, re, sys, os
class DisBot(discord.Client):
    all_db = {"accounts":{}, "word": []}

    async def on_ready(self):
        self.load()
        if conf.cell_char == conf.bot_word:
            raise CallChar("Знаки вызова для общения с ботом и вызовом для команды не могут быть одинаковы")
        #print(self.all_db)
        #self.all_db["word"].append({"re": True, "command": True, "text": r"давай <@!\d{18}> поженимся", "repl": kilogrammm})
        #print(self.all_db)
        print("Бот начал работу")

    async def on_message(self, message):
        #self.all_db["accounts"] = {}
        #if message.content.startswith("-"):
        #    await message.channel.send(message.content[1:])
        #self.all_db = {"accounts":{}, "word": [{"re": False, "command": False, "text": "надеюсь", "repl": "что будет писать бот взамен"}, {"re": True, "command": False, "text": r"надеюсь <@!\d{18}> прид[её]т", "repl": r"что будет писать [{bot}] взамен. автор - [{author}]. [{0}] упоминание"}]}
        #self.all_db["accounts"][str(message.author.id)]["game"] = ""
        #self.all_db.update({"other": {"base_map_game_green": message.content}})
        #print(message.content)
        try:
            if str(message.author)!=str(self.user):
                check.check(self, message.author)
                if str(message.content).startswith(conf.cell_char):
                    msg = str(message.content)[len(list(conf.cell_char)):].split(" ")
                    if hasattr(globals()["functions"], msg[0].lower()):
                        await getattr(globals()["functions"], msg[0].lower())(self, message)
                    else:
                        await message.channel.send("Такой команды не существует")
                elif len(conf.bot_word) == 0 or str(message.content).startswith(conf.bot_word):
                    msg = str(message.content)[len(list(conf.bot_word)):].split(" ")
                    if self.all_db["accounts"][str(message.author.id)]["enable_msg_reply"]:
                        for i in self.all_db["word"]:
                            if i["re"]:
                                if re.findall(i["text"], " ".join(msg).lower()):
                                    await reply.reply_re(self, message, i)
                            else:
                                if " ".join(msg).lower() == i["text"]:
                                    await reply.reply(self, message, i)
        except Exception as e:
            await message.channel.send(e)

        self.save()

    def save(self):
        with open('db.pickle', 'wb') as f:
            pickle.dump(self.all_db, f)

    def load(self):
        with open('db.pickle', 'rb') as f:
            self.all_db = pickle.load(f)

client = DisBot()
client.run(conf.bot_token)