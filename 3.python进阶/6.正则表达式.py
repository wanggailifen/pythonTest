import re

s = "python gagagaggag  python"
s2 = "1python gagagagg@!$asdc321"

result = re.match("python", s)
print(result)

result = re.match("python", s2)
print(result)

result = re.search("python", s2)
print(result)

result = re.findall("python", s)
print(result)

# 前面带上r的标记，表示字符串中转义字符无效，就是普通字符的意思
result = re.findall(r'\d', s2)
print(result)

result = re.findall(r'\W', s2)
print(result)
