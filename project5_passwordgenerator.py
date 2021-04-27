import random
password_len = int(input("enter the length of the passord that you want "))
password_list = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
final_password = "".join(random.sample(password_list, password_len))
print(final_password)
