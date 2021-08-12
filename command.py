import re, conf, datetime, check
async def davay(*args):
    self = args[0]
    message = args[1]
    msg = str(message.content)[len(list(conf.bot_word)):]
    i = args[2]
    user_1 = message.author
    id = re.findall("<@!\d{18}>", msg)[0]
    id = re.findall("<@!(.*?)>", id)[0]
    user_2 = await self.fetch_user(id)
    check.check(self, user_2)
    if self.all_db["accounts"][str(user_1.id)]["married"] or self.all_db["accounts"][str(user_2.id)]["married"]:
        await message.channel.send("Ктото из вас уже поженился, а может и вы оба, мне лень делать проверку на каждого поотдельности, поэтому както так")
    else:
        self.all_db["accounts"][str(user_1.id)]["married_request"] = user_2.id
        if self.all_db["accounts"][str(user_2.id)]["married_request"] == user_1.id:
            self.all_db["accounts"][str(user_1.id)]["married"] = True
            self.all_db["accounts"][str(user_2.id)]["married"] = True
            self.all_db["accounts"][str(user_1.id)]["married_to"] = user_2.id
            self.all_db["accounts"][str(user_2.id)]["married_to"] = user_1.id
            date = datetime.datetime().today().strftime("%d.%m.%d %H:%M:%S")
            self.all_db["accounts"][str(user_1.id)]["married_date"] = date
            self.all_db["accounts"][str(user_2.id)]["married_date"] = date
            self.all_db["accounts"][str(user_1.id)]["married_request"] = 0
            self.all_db["accounts"][str(user_2.id)]["married_request"] = 0
            await message.channel.send("Поздравляю, теперь {} и {} женаты".format(user_1.mention, user_2.mention))
        else:
            await message.channel.send("Вы подали заявку, ждем когда {} ответит".format(user_2.mention))
        #{"married": False, "married_to": 0, "xp": 0, "married_date": "", "married_request": 0, "admin": False, "enable_msg_reply": True}})