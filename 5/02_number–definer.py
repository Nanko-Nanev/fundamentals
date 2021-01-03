num = float(input())

if num == 0:
    print("zero")
elif 0 < num < 1:
    print("small positive")
elif -1 < num < 0:
    print("small negative")
elif num > 1000000:
    print("large positive")
elif num < -1000000:
    print("large negative")
elif num > 1:
    print("positive")
else:
    print("negative")




# while True:
#     current_num = float(input())
#     if current_num == 0:
#         print("zero")
#     elif current_num > 0:
#         if 1 > current_num > 0:
#             print("small", end=" ")
#         if current_num > 1000000:
#             print("large", end=" ")
#         print("positive")
#     else:
#         if 0 > current_num > -1:
#             print("small", end=" ")
#         if current_num < -1000000:
#             print("large", end=" ")
#         print("negative")