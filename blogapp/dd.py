

def a(sente):
    root={}
    for sentence in sente:
        base=root
        for word in sentence.split(' '):
            if not base.get(word):
                base[word]={}
            base=base[word]
    return root

tree = a(['Hello world','hello there'])