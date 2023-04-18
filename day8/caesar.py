alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
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

arr_text = list(text)
arr_text_index = []

encrypted_text = "" 
length_text = len(text)

print(arr_text)
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    for i in range(length_text):
        arr_text_index = int(alphabet.index(arr_text[i]))+1
        encrypted_text = alphabet[arr_text_index]
        


        
    

    




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
