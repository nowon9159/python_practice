### 암복호화 하기
## 로직
# 1. 암호화 하기
# 2. 복호화 하기
# 

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
        if shift_amount >= 26 :
          shift_amount = shift_amount % 26
          print(shift_amount)
    for char in start_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        # 숫자나 심볼 스페이스가 들어갔을 때 text 값을 보존할 수 있게끔 해야된다.
        # 어차피 char 값을 받아서 end_text 에 집어 넣기 때문에 if 조건문으로 알파벳에 없다면 그냥 그대로 집어 넣게 끔 해줬다.
        if char not in alphabet: 
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

program_restart = "yes"
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
# While 반복문 밖에 변수를 하나 설정하고 while 반복문에 조건을 달아 input 값이 no 라면 변수 값을 바꿔주게 끔 설정
while program_restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    #Hint: Think about how you can use the modulus (%).
    # shift 의 숫자가 26보다 크다면 어떻게 해야하는가?
    # 26으로 나눈 나머지의 수를 인덱스 값에 다시 집어 넣으면 된다.
    

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    program_restart = input("Do you want restart?:\n").lower()
    if program_restart == "no":
        break
