import re
pattern = r"^(\$|%)(?P<tag>[A-Z]{1}[a-z]+)\1:\s\[(?P<t1>[0-9]+)\]\|\[(?P<t2>[0-9]+)\]\|\[(?P<t3>[0-9]+)\]\|"
n = int(input())

for i in range(n):
    data = input()
    result = re.match(pattern, data)
    if result:
        obj = result.groupdict()
        tag = (obj['tag'])
        a = chr(int(obj['t1']))
        b = chr(int(obj['t2']))
        c = chr(int(obj['t3']))
        print(f"{tag}: {a}{b}{c}")
    else:
        print(f"Valid message not found!")