myStr = "hello,hoho"

# 字符串不支持直接修改
# myStr[0] = "a"
print(myStr.index("hoho"))

myStr2 = myStr.replace("o", "a")
print(myStr)
print(myStr2)

list3 = myStr.split(",")
print(list3)

myStr4 = " haha "
str4 = myStr4.strip()
print(str4)

myStr5 = "123haha321"
str5 = myStr5.strip("123")
print(str5)

print(myStr5.count("a"))
