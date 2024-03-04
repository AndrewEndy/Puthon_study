# Perfect text

def get_perfect_text_on_puti(puti):
    file = open(f'{puti}','r')
    s=file.read()
    s=s.split()
    file.close()

    text=[]
    for word in s:
        word=word.strip('-')
        word=word.strip('+')
        word=word.strip('!?')
        word=word.strip('[')
        word=word.strip(']')
        word=word.strip('}')
        word=word.strip('{')
        word=word.strip('(')
        word=word.strip(')')
        word=word.strip('`')
        word=word.strip('~')
        word=word.strip('!')
        word=word.strip('?')
        word=word.strip('/')
        word=word.strip('"')
        word=word.strip('\'')
        word=word.strip(':')
        word=word.strip(';')
        word=word.strip('.')
        word=word.strip(',')
        word=word.lower()
        text.append(word)
    return text

def get_perfect_text_on_line(line):
    line=line.split()
    text=[]
    for word in line:
        word=word.strip('-')
        word=word.strip('+')
        word=word.strip('!?')
        word=word.strip('[')
        word=word.strip(']')
        word=word.strip('}')
        word=word.strip('{')
        word=word.strip('(')
        word=word.strip(')')
        word=word.strip('`')
        word=word.strip('~')
        word=word.strip('!')
        word=word.strip('?')
        word=word.strip('/')
        word=word.strip('"')
        word=word.strip('\'')
        word=word.strip(':')
        word=word.strip(';')
        word=word.strip('.')
        word=word.strip(',')
        word=word.lower()
        text.append(word)
    return text