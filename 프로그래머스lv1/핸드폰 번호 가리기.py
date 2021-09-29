# phone_number = "01033334444"

# for i in range(len(phone_number)-4):
#     phone_number = phone_number.replace(phone_number[i], '*', 1)
# print(phone_number)

phone_number = "01033334444"
print('*' * int(len((phone_number)-4)) + phone_number[-4:])
