'''
This Python file will make txt file of 한글 -> 영어 조합 
or 영어 -> 한글 조합 for shell
'''
import hgtk
import sys
import os

if len(sys.argv) < 2:
    print('Usage : python3 make_english.py [kor|eng]')
    sys.exit(1)

eng_file_name = "./key_map_english.sh"
kor_file_name = "./key_map_korean.sh"

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
    'fx' : 'ㄾ',
    "" : ""
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
    'ㄾ' : 'fx',
    "" : ""
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

#모든 영어 조합에 대한 한글
def make_eng():
    if os.path.exists(eng_file_name):
        print('File Already Exist')
        return
    
    fp = open(eng_file_name, 'w')
    fp.write('declare -A gksdud\n')

    chosung_list = list(chosung)
    jungsung_list = list(jungsung)
    jongsung_list = list(jongsung)

    for key in mom_text_dict:
        if key == "":
            continue
        txt = "gksdud["
        txt += key
        txt += "] = "
        txt += '"' + mom_text_dict[key] + '"'
        fp.write(txt + '\n')
    
    for key in jom_text_dict:
        if key == "":
            continue
        txt = "gksdud["
        txt += key
        txt += "] = "
        txt += '"' + jom_text_dict[key] + '"'
        fp.write(txt + '\n')

    for cho, _ in enumerate(chosung_list):
        for jung, _ in enumerate(jungsung_list):
            for jong, _ in enumerate(jongsung_list):
                txt = "gksdud["
                kor = chr(0xAC00 + ((cho*21)+jung)*28+jong)
                eng = ''
                if chosung_list[cho] in mom_text_dict_eng:
                    eng += mom_text_dict_eng[chosung_list[cho]]
                else:
                    eng += jom_text_dict_eng[chosung_list[cho]]
                
                if jungsung_list[jung] in mom_text_dict_eng:
                    eng += mom_text_dict_eng[jungsung_list[jung]]
                else:
                    eng += jom_text_dict_eng[jungsung_list[jung]]
                
                if jongsung_list[jong] in mom_text_dict_eng:
                    eng += mom_text_dict_eng[jongsung_list[jong]]
                else:
                    eng += jom_text_dict_eng[jongsung_list[jong]]
                
                txt += eng + '] = "' + kor + '"'
                fp.write(txt + '\n')
    fp.close()

#모든 한글 조합에 대한 영어
def make_kor():
    if os.path.exists(kor_file_name):
        print('File Already Exist')
        return
    
    fp = open(kor_file_name, 'w')
    fp.write('declare -A gksdud\n')

    chosung_list = list(chosung)
    jungsung_list = list(jungsung)
    jongsung_list = list(jongsung)

    for key in mom_text_dict:
        if key == "":
            continue
        txt = "gksdud["
        txt += mom_text_dict[key]
        txt += "] = "
        txt += '"' + key + '"'
        fp.write(txt + '\n')
    
    for key in jom_text_dict:
        if key == "":
            continue
        txt = "gksdud["
        txt += jom_text_dict[key]
        txt += "] = "
        txt += '"' + key + '"'
        fp.write(txt + '\n')

    for cho, _ in enumerate(chosung_list):
        for jung, _ in enumerate(jungsung_list):
            for jong, _ in enumerate(jongsung_list):
                txt = "gksdud["
                kor = chr(0xAC00 + ((cho*21)+jung)*28+jong)
                txt += kor + '] = "'
                if chosung_list[cho] in mom_text_dict_eng:
                    txt += mom_text_dict_eng[chosung_list[cho]]
                else:
                    txt += jom_text_dict_eng[chosung_list[cho]]
                
                if jungsung_list[jung] in mom_text_dict_eng:
                    txt += mom_text_dict_eng[jungsung_list[jung]]
                else:
                    txt += jom_text_dict_eng[jungsung_list[jung]]
                
                if jongsung_list[jong] in mom_text_dict_eng:
                    txt += mom_text_dict_eng[jongsung_list[jong]]
                else:
                    txt += jom_text_dict_eng[jongsung_list[jong]]
                
                txt += '"'
                fp.write(txt + '\n')
    fp.close()

if __name__ == '__main__':
    if sys.argv[1] == 'kor':
        make_kor()
    elif sys.argv[1] == 'eng':
        make_eng()





