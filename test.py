"""import re
a = r"<@!\d{18}>"
a = r"фф(11)|(22)"
a = input()
b = " <@!654263151145639997> фф11 awjhdjwdbjka <@!794265151145639997> фф1[123] jxgsjzgc фф22<@!794263151145639997> z"
#b = [" <@!654263151145639997> awjhdjwdbjka <@!794265151145639997>  jxgsjzgc <@!794263151145639997> z"]
i = re.findall(a, b)
print(i)
c = {
r"<@!\d{18}>": "qa"
}
for i in c.keys():
    if re.findall(i, b):
        print(c[i])
#m = re.findall(a, b)
#print(m)

a = [0, 1, 2, 3]
a.pop(2)
print(a)"""
def b(a):
    return a
a = {"a": b}
print(a["a"](2))