class Character():
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender

    def intro(self):
        print("%s은/는 %d세이고, %s입니다."
        %(self.name, self.age , self.gender))

zzang9 = Character("짱구", 5, "남자")
ddora = Character("도라에몽", 14, "남자")
detective = Character("코난", 8, "남자")
choco = Character("쇼콜라", 15, "여자")
what = Character("아무", 12, "여자")
young = Character("가영", 16, "여자")

zzang9.intro()
ddora.intro()
detective.intro()
choco.intro()
what.intro()
young.intro()