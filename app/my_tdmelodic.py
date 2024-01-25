import MeCab, re, pandas as pd, io
 
def _format_string(input):
    matches = re.findall(r'\w+\t([^\n]+)\r\n', input)
    output = '\n'.join(matches)
    return output

def tdmelodic(target_str):
	mecab = MeCab.Tagger("-d ./tdmelodic-ipadic")
	mecab_parse = mecab.parse(target_str)

	_csv = '0,1,2,3,4,5,6,7,8\n' + _format_string(mecab_parse)

	df = pd.read_csv(io.StringIO(_csv))

	string = ''.join(df['8'].values.flatten())
	return string