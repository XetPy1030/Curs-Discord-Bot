async def profile(self, message):
    marrie = ""
    if self.all_db["accounts"][str(message.author.id)]["married"]:
        marrie+="Женат(-а): да\nПартнер: {}\nДата женитьбы(ахах, что?): {}".format(str((await self.get_user(self.all_db["accounts"][str(message.author.id)]["married_to"])).mention))
    else:
        marrie+="Женат(-а): нет\n"
        if self.all_db["accounts"][str(message.author.id)]["married_request"] != 0:
            marrie+="Ждешь ответа от: {}".format(str((await self.fetch_user(self.all_db["accounts"][str(message.author.id)]["married_request"])).mention))
    a = "Профиль\nПрефикс: {}\nXP: {}\nadmin: {}\nОтветки бота: {}\n{}".format(message.author.mention, self.all_db["accounts"][str(message.author.id)]["xp"], self.all_db["accounts"][str(message.author.id)]["admin"], self.all_db["accounts"][str(message.author.id)]["enable_msg_reply"], marrie)
    await message.channel.send(a)
    #{"married": False, "married_to": 0, "xp": 0, "married_date": "", "married_request": 0, "admin": False, "enable_msg_reply": True}}