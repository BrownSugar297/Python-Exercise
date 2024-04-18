class baba():
    car = "bmw"
    tk = "10 lakh"
    home = "10 stories"


class kaka1:
    phone = "iphone"
    ac = "singer"
    microphone = "jbl"


class kaka2:
    shop = "grocery"
    laptop = "apple"
    brain = "damaged"


class babaFriend(baba, kaka1, kaka2):
    brokenhouse = ""
    brokenphone = ""


k = babaFriend()
m = kaka1()
print(k.shop)
print(k.phone)
print(m.microphone)
# print(m.car)
