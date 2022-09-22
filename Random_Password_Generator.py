import random

def random_password_generator(length_of_password):
    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case="abcdefghijklmnopqrstuvwxyz"
    num="0123456789"
    symbols="(){}[]@#$%&*!"
    ans= upper_case + lower_case +  num + symbols
    password="".join(random.sample(ans,length_of_password))
    return password
    
Input_lenght = int(input("Enter the Lenght Of Password : "))
OutPut = random_password_generator(Input_lenght)
print(OutPut)

    