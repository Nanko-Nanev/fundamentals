# factor = int(input())
# count = int(input())
# list_with_numbers = []
# stop = True
#
# while stop:
#     for i in range(factor, 9999999):
#         if i % factor == 0:
#             list_with_numbers.append(i)
#         if len(list_with_numbers) == count:
#             stop = False
#             break
#
#     print(list_with_numbers)

factor = int(input())
count = int(input())
numbers = [ele * factor for ele in range(1, count + 1)]
print(numbers)