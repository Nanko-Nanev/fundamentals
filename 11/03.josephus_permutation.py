j_list = input().split()
k = int(input())
i = k - 1
work_list = []
result = []
work_list += j_list * 10

result += work_list[i]
work_list = [a.replace(work_list[i], "redfgwesdrgsfdasd") for a in work_list]
for ii in work_list:
    if ii == "redfgwesdrgsfdasd":
        work_list.remove("redfgwesdrgsfdasd")

while len(work_list) > 0:
    i += k
    result += work_list[i]
    work_list = [a.replace(work_list[i], "redfgwesdrgsfdasd") for a in work_list]
    for ii in work_list:
        if ii == "redfgwesdrgsfdasd":
            work_list.remove("redfgwesdrgsfdasd")

print(result)