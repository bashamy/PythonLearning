lst = ["apple","banana","citrus"]
print(lst)
lst.append("Dates")
print(lst)

tpl = ("apple","banana","citrus")
print(tpl)
tpllst = list(tpl)
tpllst.append("Dewberry")
print(tpllst)
tpl = tuple(tpllst)
print(tpl)
