chars = "abcdefghijklmnopqrstuvwxyzAEIOUBCDFGHJKLMNPQRSTVXZWY"
c = check_string = input("Input : ")

print("Output : " ,  end="")
for char in chars:
  count = check_string.count(char)

  if count >= 1:
    print(char, end="")
    print(count, end="")

