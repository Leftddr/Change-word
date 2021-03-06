import hgtk
import sys
import urllib.request
import json
import threading

if len(sys.argv) < 3:
    print('Usage : python3 replace_text.py [word] [eng|kor]')
    sys.exit(1)

chosung = (
   "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ",
   "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ",
   "ㅌ", "ㅍ", "ㅎ")

jungsung = (
   "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ",
   "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ",
   "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ")

jongsung = (
   "", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ",
   "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ",
   "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ",
   "ㅋ", "ㅌ", "ㅍ", "ㅎ")

jom_text_dict = {
    'a' : 'ㅁ',
    'z' : 'ㅋ',
    'q' : 'ㅂ',
    'w' : 'ㅈ',
    's' : 'ㄴ',
    'x' : 'ㅌ',
    'e' : 'ㄷ',
    'd' : 'ㅇ',
    'c' : 'ㅊ',
    'r' : 'ㄱ',
    'f' : 'ㄹ',
    'v' : 'ㅍ',
    't' : 'ㅅ',
    'g' : 'ㅎ',
    'Q' : 'ㅃ',
    'W' : 'ㅉ',
    'E' : 'ㄸ',
    'R' : 'ㄲ',
    'T' : 'ㅆ',
    'rt' : 'ㄳ',
    'sw' : 'ㄵ',
    'sg' : 'ㄶ',
    'fr' : 'ㄺ',
    'fa' : 'ㄻ',
    'fq' : 'ㄼ',
    'ft' : 'ㄽ',
    'fv' : 'ㄿ',
    'fg' : 'ㅀ',
    'qt' : 'ㅄ',
    'fx' : 'ㄾ'
}

mom_text_dict = {
    'b' : 'ㅠ',
    'y' : 'ㅛ',
    'h' : 'ㅗ',
    'n' : 'ㅜ',
    'u' : 'ㅕ',
    'j' : 'ㅓ',
    'm' : 'ㅡ',
    'i' : 'ㅑ',
    'k' : 'ㅏ',
    'o' : 'ㅐ',
    'l' : 'ㅣ',
    'p' : 'ㅔ',
    'P' : 'ㅖ',
    'O' : 'ㅒ',
    'nj' : 'ㅝ',
    'hk' : 'ㅘ',
    'ho' : 'ㅙ',
    'hl' : 'ㅚ',
    'np' : 'ㅞ',
    'nl' : 'ㅟ',
    'ml' : 'ㅢ'
}

jom_text_dict_eng = {
    'ㅁ' : 'a',
    'ㅋ' : 'z',
    'ㅂ' : 'q',
    'ㅈ' : 'w',
    'ㄴ' : 's',
    'ㅌ' : 'x',
    'ㄷ' : 'e',
    'ㅇ' : 'd',
    'ㅊ' : 'c',
    'ㄱ' : 'r',
    'ㄹ' : 'f',
    'ㅍ' : 'v',
    'ㅅ' : 't',
    'ㅎ' : 'g',
    'ㅃ' : 'Q',
    'ㅉ' : 'W',
    'ㄸ' : 'E',
    'ㄲ' : 'R',
    'ㅆ' : 'T',
    'ㄳ' : 'rt',
    'ㄵ' : 'sw',
    'ㄶ' : 'sg',
    'ㄺ' : 'fr',
    'ㄻ' : 'fa',
    'ㄼ' : 'fq',
    'ㄽ' : 'ft',
    'ㄿ' : 'fv',
    'ㅀ' : 'fg',
    'ㅄ' : 'qt',
    'ㄾ' : 'fx'
}

mom_text_dict_eng = {
    'ㅠ' : 'b',
    'ㅛ' : 'y',
    'ㅗ' : 'h',
    'ㅜ' : 'n',
    'ㅕ' : 'u',
    'ㅓ' : 'j',
    'ㅡ' : 'm',
    'ㅑ' : 'i',
    'ㅏ' : 'k',
    'ㅐ' : 'o',
    'ㅣ' : 'l',
    'ㅔ' : 'p',
    'ㅖ' : 'P',
    'ㅒ' : 'O',
    'ㅝ' : 'nj',
    'ㅘ' : 'hk',
    'ㅙ' : 'ho',
    'ㅚ' : 'hl',
    'ㅞ' : 'np',
    'ㅟ' : 'nl',
    'ㅢ' : 'ml'
}

def translated_text(input_word):
    client_id = "input your Id" 
    client_secret = "input your Secret" 
    encText = urllib.parse.quote(input_word)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data = data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        json_rt = response.read().decode('utf-8')
        py_rt = json.loads(json_rt)
        print("translated_text : " + py_rt['message']['result']['translatedText'])
    else:
        print("Error Code:" + rescode)

def original_text(input_word):
    word_len = len(input_word)
    word = input_word
    index = 0
    result = ''

    while index < word_len:
        if word[index] == ' ':
            result += word[index]
            index += 1
            continue
        word_list = list(hgtk.letter.decompose(word[index]))
        for tmp_index, tmp_word in enumerate(word_list):
            if tmp_word in mom_text_dict_eng:
                result += mom_text_dict_eng[tmp_word]
            elif tmp_word in jom_text_dict_eng:
                result += jom_text_dict_eng[tmp_word]
            else:
                break
        index += 1
    
    print('original_text : ' + result)

''' 
My Code Cannot init because ㅡ + ㅣ => ml, ㅢ => ml, there are not different
def init():
    word = sys.argv[1]
    word_len = len(sys.argv[1])
    result = ''
    index = 0

    while index < word_len:
        if word[index] in mom_text_dict:
            # ㅡ....
            if index + 1 < word_len:
                result += word[index]
            # ㅡ + ㅣ ....
            elif word[index + 1] in mom_text_dict:
                #ㅢ.....
                if (word[index] + word[index + 1]) in mom_text_dict:
                    result += mom
'''

def to_korean(input_word):
    if sys.argv[len(sys.argv) - 1] == 'kor':
        word = input_word
        word_len = len(input_word)
        index = 0
        cho, jung, jong = 0, 0, 0

        while index < word_len:
            if word[index] in mom_text_dict:
                print(mom_text_dict[word[index]], end = '')
                index += 1
            #ㅁ,ㄱ....
            elif word[index] in jom_text_dict:
                cho = chosung.index(jom_text_dict[word[index]])
                if index + 1 >= word_len:
                    print(jom_text_dict[word[index]], end = '')
                    index += 1
                #ㅁ + ㅡ
                elif word[index + 1] in mom_text_dict:
                    if index + 2 >= word_len:
                        jung = jungsung.index(mom_text_dict[word[index + 1]])
                        print(chr(0xAC00 + ((cho*21)+jung)*28+0), end = '')
                        index += 2
                    # ㅁ + ㅡ + ㅣ
                    elif word[index + 2] in mom_text_dict:
                        if (word[index + 1] + word[index + 2]) in mom_text_dict:
                            jung = jungsung.index(mom_text_dict[word[index + 1] + word[index + 2]])
                            if index + 3 >= word_len:
                                print(chr(0xAC00 + ((cho*21)+jung)*28+0), end = '')
                                index += 3
                            elif word[index + 3] in mom_text_dict:
                                print(chr(0xAC00 + ((cho*21)+jung)*28+0), end = '')
                                index += 3
                            #ㅁ + ㅡ + ㅣ + ㅁ
                            else:
                                if word[index + 3] == ' ':
                                    print(chr(0xAC00 + ((cho*21)+jung)*28+0), end = '')
                                    index += 3
                                    continue
                                jong = jongsung.index(jom_text_dict[word[index + 3]])
                                if index + 4 >= word_len:
                                    print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                                    index += 4
                                #ㅁ + ㅡ + ㅣ + ㅁ + ㅣ....
                                elif word[index + 4] in mom_text_dict:
                                    print(chr(0xAC00 + ((cho*21)+jung)*28+0), end = '')
                                    index += 3
                                #ㅁ + ㅡ + ㅣ + ㅁ + ㅁ....
                                else:
                                    #ㅁ + ㅡ + ㄱ + ㅅ.. => ㅁ + ㅡ + ㄳ
                                    if (word[index + 3] + word[index + 4]) in jom_text_dict:
                                        # ㅁ + ㅡ + ㄱ + ㅅ + ㅜ => 믁수
                                        if index + 5 >= word_len:
                                            jong  = jongsung.index(jom_text_dict[word[index + 3] + word[index + 4]])
                                            print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                                            index += 5
                                        elif word[index + 5] in mom_text_dict:
                                            jong = jongsung.index(jom_text_dict[word[inex + 3]])
                                            print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                                            index += 4
                                        else:
                                            jong  = jongsung.index(jom_text_dict[word[index + 3] + word[index + 4]])
                                            print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                                            index += 5
                                    else:
                                        print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                                        index += 4
                    # ㅁ + ㅡ + ㅁ
                    elif word[index + 2] in jom_text_dict:
                        jung = jungsung.index(mom_text_dict[word[index + 1]])
                        jong = jongsung.index(jom_text_dict[word[index + 2]])
                        if index + 3 >= word_len:
                            print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                            index += 3
                        #ㅁ + ㅡ + ㅁ + ㅣ.....
                        elif word[index + 3] in mom_text_dict:
                            print(chr(0xAC00 + ((cho*21)+jung)*28+0), end = '')
                            index += 2
                        #ㅁ + ㅡ + ㄱ + ㅁ....
                        else:
                            #ㅁ + ㅡ + ㄱ + ㅅ.. => ㅁ + ㅡ + ㄳ
                            if (word[index + 2] + word[index + 3]) in jom_text_dict:
                                if index + 4 >= word_len:
                                    jong  = jongsung.index(jom_text_dict[word[index + 2] + word[index + 3]])
                                    print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                                    index += 4
                                elif word[index + 4] in mom_text_dict:
                                    jong = jongsung.index(jom_text_dict[word[index + 2]])
                                    print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                                    index += 3
                                else:
                                    jong  = jongsung.index(jom_text_dict[word[index + 2] + word[index + 3]])
                                    print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                                    index += 4
                            else:
                                print(chr(0xAC00 + ((cho*21)+jung)*28+jong), end = '')
                                index += 3
                    else:
                        jung = jungsung.index(mom_text_dict[word[index + 1]])
                        print(chr(0xAC00 + ((cho*21)+jung)*28+0), end = '')
                        index += 2
                else:
                    print(jom_text_dict[word[index]], end = '')
                    index += 1
            #space, or other word
            else:
                print(word[index], end = '')
                index += 1
        print()

def trans(input_word):
    if sys.argv[len(sys.argv) - 1] == 'eng':
        t1 = threading.Thread(target = original_text, args = (input_word,))
        #t2 = threading.Thread(target = translated_text, args = (input_word))
        t1.start()
        #t2.start()

def error():
    print('Usage : python3 replace_text.py [word] [eng|kor]')
    sys.exit(1)

def init():
    result = ''
    for i in range(1, len(sys.argv) - 1):
        result += (sys.argv[i] + ' ')
    return result

if __name__ == '__main__':
    input_word = init()
    if sys.argv[len(sys.argv) - 1] == 'kor':
        to_korean(input_word)
    elif sys.argv[len(sys.argv) - 1] == 'eng':
        trans(input_word)
    else:
        error()
