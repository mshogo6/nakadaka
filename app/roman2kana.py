import json

def _is_vowel(char):
	if(char == 'a' or char == 'i' or char == 'u' or char == 'e' or char == 'o'):
		return True
	return False

def _get_kana(roman):
	with open('rom2kana_dict.json', encoding='utf8') as dict_file:
		dict = json.load(dict_file)
		return dict[roman]

def convert(phoneme):
	roman = ''
	roman_hist = ''
	hist_cnt = 0
	kana = ''
	for char in phoneme:
		if(char != ' ' and char != '_'):
			if(char == '[' or char == ']'):
				kana += char
			else:
				roman += char
				if(_is_vowel(char)):
					if(char == roman_hist and hist_cnt < 1):
						hist_cnt += 1
						kana += 'ー'
					else:
						kana += _get_kana(roman)
						roman_hist = char
						hist_cnt = 0
					roman = ''
				else:
					if(char == 'n'):
						if(char == roman_hist):
							kana += 'ン'
							roman = 'n'
							roman_hist = 'n'
						else:
							roman_hist = char
					else:
						if(char == 'N'):
							kana += 'ン'
							roman = ''
						elif(roman_hist == 'n'):
							kana += 'ン'
							roman = char
						elif(roman == 'cl'):
							kana += 'ッ'
							roman = ''
						roman_hist = ''
	return kana