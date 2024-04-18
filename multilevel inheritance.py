class baba():
    car = "bmw"
    tk = "10 lakh"
    home = "10 stories"


class son1(baba):
    phone = "iphone"
    ac = "singer"
    microphone = "jbl"


class son2(son1):
    shop = "grocery"
    laptop = "apple"
    brain = "damaged"


class son3(son2):
    brokenhouse = ""
    brokenphone = ""


k = son3()
m = son1()

print(k.shop)
print(k.phone)
print(m.car)
