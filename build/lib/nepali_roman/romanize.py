import json


with open('nepali_roman/characters_map.json') as f:
    d2r_dict = json.load(f)
    
    
def romanize_text(text):
    if type(text) == float:
        return
    for key,value in d2r_dict.items():
        text=text.replace(key,value)  
    return text

def romanize(in_file, out_file):
    with open(in_file) as f:
        text = f.read()
    
    with open(out_file, 'w+') as f:
        romanized_text = romanize_text(text)
        f.write(romanized_text)