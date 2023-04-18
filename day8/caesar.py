alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# 텍스트가 test 라면 [t, e, s, t] 로 뽑아서
# 인덱스 번호 추출 한 뒤 인덱스 번호에서 shift 만큼 + 하기
# array.index(x) 함수를 사용하면 된다. -> 뽑아낸 뒤 새로운 배열에 append
# 새로운 배열에 인덱스 값을 shift 만큼 +
# 인덱스 값으로 알파벳 값 추출

arr_text_index = []
arr_encrypted_text = [] 
encrypted_text = ""
length_text = len(text)


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    arr_text = list(text)
    # print(arr_text)
    for i in range(length_text):
        # arr_text_index 에 alphabet
        arr_text_index = int(alphabet.index(arr_text[i]))+shift
        encrypted_text = alphabet[arr_text_index]
        arr_encrypted_text.append(encrypted_text)
    # print(arr_encrypted_text)
    for i in range(len(arr_encrypted_text)):
        encrypted_text = ''.join(arr_encrypted_text) # join 함수 => '구분자'.join(리스트)
    print(f"This is a encrypted input : {encrypted_text}")
        
def decrypt(text, shift):
    cipher_text = ""
    for i in text:
        position = alphabet.index(i) # index 함수는 배열의 인덱스 값을 추출 가능
        new_position = position - shift # shift 만큼 추출한 인덱스 값 빼기
        new_letter = alphabet[new_position] # 뉴포지션의 인덱스 값을 기반으로 알파벳 값 뽑아 내 new_letter 집어 넣기
        cipher_text += new_letter # cipher_text 에 new_letter 순차적으로 집어 넣기
    print(f"The Decoded text is {cipher_text}")





    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
