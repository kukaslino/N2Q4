def criptografar_string(s):

    if validate(s) == False:
        return "The value cannot be a number"

    words = s.split()
    word_final = ""
    index = 0

    for word in words:
        if len(word) < 2:
            word_final = concat_word(word)

        word = trocar_segundo_caracter(word)
        primeiro_caracter_asc = ord(word[0])  # Obtém o valor ASCII do primeiro caractere

        word = str(primeiro_caracter_asc) + word[1:len(word)]

        word_final = concat_word(word,word_final,index)

        index = index + 1   
    
    return word_final

def trocar_segundo_caracter(s):
    caracteres = list(s)
    caracteres[1], caracteres[-1] = caracteres[-1], caracteres[1]
    nova_string = ''.join(caracteres)
    return nova_string

def concat_word(newWord,word_final,index):
    if index != 0:
        word_final += " "
        word_final +=newWord
    else:
        word_final += newWord
    
    return word_final

def validate(s):
    isValid = True

    if type(s) != str:
        isValid = False

    
    return isValid

print(criptografar_string("hello world"))