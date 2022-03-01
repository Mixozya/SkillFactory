# B5.6 ИТОГОВОЕ ПРАКТИЧЕСКОЕ ЗАДАНИЕ

print("Привет. Введите поле, куда Вы хотите поставить "
      "\nкрестик или нолик по формату: хa1 или oc2 или xb2 и тп. "
      "\n(Крестик и Нолик - английские буквы x и o)")

str1 = "   1 2 3\n"
str2 = "a - - -\n"
str3 = "b - - -\n"
str4 = "c - - -"

liststr2 = list(str2)
liststr3 = list(str3)
liststr4 = list(str4)
krestik = "x"
nolik = "o"

print(str1, str2, str3, str4)

while True:
    vvod = str(input("Введите поле: "))
    if vvod == "xa1":
        liststr2[2] = krestik
        str2 = ''.join(liststr2)
        print(str1, str2, str3, str4)
    elif vvod == "xa2":
        liststr2[4] = krestik
        str2 = ''.join(liststr2)
        print(str1, str2, str3, str4)
    elif vvod == "xa3":
        liststr2[6] = krestik
        str2 = ''.join(liststr2)
        print(str1, str2, str3, str4)
    elif vvod == "xb1":
        liststr3[2] = krestik
        str3 = ''.join(liststr3)
        print(str1, str2, str3, str4)
    elif vvod == "xb2":
        liststr3[4] = krestik
        str3 = ''.join(liststr3)
        print(str1, str2, str3, str4)
    elif vvod == "xb3":
        liststr3[6] = krestik
        str3 = ''.join(liststr3)
        print(str1, str2, str3, str4)
    elif vvod == "xc1":
        liststr4[2] = krestik
        str4 = ''.join(liststr4)
        print(str1, str2, str3, str4)
    elif vvod == "xc2":
        liststr4[4] = krestik
        str4 = ''.join(liststr4)
        print(str1, str2, str3, str4)
    elif vvod == "xc3":
        liststr4[6] = krestik
        str4 = ''.join(liststr4)
        print(str1, str2, str3, str4)
    elif vvod == "oa1":
        liststr2[2] = nolik
        str2 = ''.join(liststr2)
        print(str1, str2, str3, str4)
    elif vvod == "oa2":
        liststr2[4] = nolik
        str2 = ''.join(liststr2)
        print(str1, str2, str3, str4)
    elif vvod == "oa3":
        liststr2[6] = nolik
        str2 = ''.join(liststr2)
        print(str1, str2, str3, str4)
    elif vvod == "ob1":
        liststr3[2] = nolik
        str3 = ''.join(liststr3)
        print(str1, str2, str3, str4)
    elif vvod == "ob2":
        liststr3[4] = nolik
        str3 = ''.join(liststr3)
        print(str1, str2, str3, str4)
    elif vvod == "ob3":
        liststr3[6] = nolik
        str3 = ''.join(liststr3)
        print(str1, str2, str3, str4)
    elif vvod == "oc1":
        liststr4[2] = nolik
        str4 = ''.join(liststr4)
        print(str1, str2, str3, str4)
    elif vvod == "oc2":
        liststr4[4] = nolik
        str4 = ''.join(liststr4)
        print(str1, str2, str3, str4)
    elif vvod == "oc3":
        liststr4[6] = nolik
        str4 = ''.join(liststr4)
        print(str1, str2, str3, str4)
    else:
        print("Неверно указано поле")
    if (liststr2[2] == krestik and liststr2[4] == krestik and liststr2[6] == krestik) or (
            liststr3[2] == krestik and liststr3[4] == krestik and liststr3[6] == krestik) or (
            liststr4[2] == krestik and liststr4[4] == krestik and liststr4[6] == krestik) or (
            liststr2[2] == krestik and liststr3[2] == krestik and liststr4[2] == krestik) or (
            liststr2[4] == krestik and liststr3[4] == krestik and liststr4[4] == krestik) or (
            liststr2[6] == krestik and liststr3[6] == krestik and liststr4[6] == krestik) or (
            liststr2[2] == krestik and liststr3[4] == krestik and liststr4[6] == krestik) or (
            liststr2[6] == krestik and liststr3[4] == krestik and liststr4[2] == krestik):
        print("Игра закончилась. Победили крестики")
        break
    elif (liststr2[2] == nolik and liststr2[4] == nolik and liststr2[6] == nolik) or (
            liststr3[2] == nolik and liststr3[4] == nolik and liststr3[6] == nolik) or (
            liststr4[2] == nolik and liststr4[4] == nolik and liststr4[6] == nolik) or (
            liststr2[2] == nolik and liststr3[2] == nolik and liststr4[2] == nolik) or (
            liststr2[4] == nolik and liststr3[4] == nolik and liststr4[4] == nolik) or (
            liststr2[6] == nolik and liststr3[6] == nolik and liststr4[6] == nolik) or (
            liststr2[2] == nolik and liststr3[4] == nolik and liststr4[6] == nolik) or (
            liststr2[6] == nolik and liststr3[4] == nolik and liststr4[2] == nolik):
        print("Игра закончилась. Победили нолики")
        break
