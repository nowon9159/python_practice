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





def ceaser(direction, text, shift):
    if direction == "encode" :
        encrypt_text = ""
        for i in text:
            position = alphabet.index(i)
            new_position = position + shift
            new_letter = alphabet[new_position] 
            encrypt_text += new_letter 
    elif direction == "decode" :
        decrypt_text = ""
        for i in text:
            position = alphabet.index(i)
            new_position = position - shift
            new_letter = alphabet[new_position] 
            decrypt_text += new_letter

ceaser(direction, text, shift)

    # cipher_text = ""
    # for i in text:
    #     position = alphabet.index(i) # index 함수는 배열의 인덱스 값을 추출 가능
    #     new_position = position - shift # shift 만큼 추출한 인덱스 값 빼기
    #     new_letter = alphabet[new_position] # 뉴포지션의 인덱스 값을 기반으로 알파벳 값 뽑아 내 new_letter 집어 넣기
    #     cipher_text += new_letter # cipher_text 에 new_letter 순차적으로 집어 넣기
    # print(f"The Decoded text is {cipher_text}")

