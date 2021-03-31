seulgi = {
    '이화여대 멋사 대표님' : '현숙' ,
    '멋사 창립자':'두희' ,
    '파이썬 세션 튜터':'세은',
    '야옹':'마루'
    }



for key, val in seulgi.items():
    print("다음은 누구에 대한 설명일까요?\n", key, "\n" , "1. 현숙 2. 세은 3. 두희 4. 마루")

    sg = input()
    if sg == val :
        print("정답입니다!\n")
    else:
        print("오답입니다!\n")