import re
async def enable(self, message):
    a = not len(re.findall(r"false", message.content.lower()))>0
    self.all_db["accounts"][str(message.author.id)]["enable_msg_reply"] = a