import re

#大文字や語頭，語末文字の削除
def strip(w):
    x = w.replace('#','')
    x = x.replace('φ','')
    x = x.replace('e','(a|i)')
    x = x.replace('o','(e|a)')
    x = x.replace('q','(b|u)')
    x = x.replace('x',"(sa|s'i)")
    x = x.replace('l',"(r'a|ri)")
    x = x.lower()
    #print('strip:'+x)
    return x

#前処理イジェール語正書法への適合
def ortho1(w):
    x = w.translate(str.maketrans('AIUEO','12345'))
    x = x.lower()
    x = x.translate(str.maketrans('12345','AIUEO'))
    x = x.replace('ki','kyi')
    x = x.replace('kI','kyI')
    x = x.replace('sh','sy')
    x = x.replace('si','syi')
    x = x.replace('sI','syI')
    x = x.replace('ti','tyi')
    x = x.replace('tI','tyI')
    x = x.replace('ch','ty')
    x = x.replace('ts','c')
    x = x.replace('tu','cu')
    x = x.replace('tU','cU')
    x = x.replace('fu','hu')
    x = x.replace('fU','hU')
    x = x.replace('dh','dy')
    x = x.replace('j','zy')
    #print('ortho1:'+x)
    return x

#後処理イジェール語正書法への適合
def ortho2(w):
    p = re.compile("([stnzdbrSTNZDBR])y")
    x = p.sub(r"\1'",w)
    x = x.replace('#y','#i')
    x = x.translate(str.maketrans('yw','iu'))
   # print('ortho2:'+x)
    return x

def commonf(w):
    x = w.replace('#hu','#fu')
    p = re.compile("(\#)h([^y])")
    x = p.sub(r"\1\2",x)
    x = x.translate(str.maketrans('AIUEO','EAOIU'))
    #oとeは正規表現マッチしやすいよう母音にしているだけで，
    #実際はstrip関数で置換される．
    x = x.translate(str.maketrans('aiueo','uiaeo'))
    p = re.compile("([^c])uφ")
    x = p.sub(r"\1φ",x)
    #print('common,f:'+x)
    return x

def commone(w):
    x = w.replace('#hu','#fu')
    p = re.compile("(\#)h([^y])")
    x = p.sub(r"\1\2",x)
    x = x.translate(str.maketrans('AIUEO','EAOIU'))
    #oとeは正規表現マッチしやすいよう母音にしているだけで，
    #実際はstrip関数で置換される．
    x = x.translate(str.maketrans('aiueo','uiaeo'))
    p = re.compile("([^c])uφ")
    x = p.sub(r"\1eφ",x)
    #print('common,e:'+x)
    return x

def sekore(w):
    ###C1強勢時(後の変化に巻き込まれないよう大文字化)
    p = re.compile("h([AIUEO])")
    x = p.sub(r"F\1",w)
    p = re.compile("r(y*?)([AIUEO])")
    x = p.sub(r"D\1\2",x)
    ###C2強勢時(後の変化に巻き込まれないよう大文字化)
    p = re.compile("([AIUEO])[uw]")
    x = p.sub(r"\1V",x)
    p = re.compile("([AIUEO])t")
    x = p.sub(r"\1C",x)
    p = re.compile("([AIUEO])r")
    x = p.sub(r"\1D",x)
    ###強勢VC後C1(後の変化に巻き込まれないよう大文字化)
    p = re.compile("([AIUEO])[^AIUEOaiueo][sc]")
    x = p.sub(r"\1Z",x)
    p = re.compile("([AIUEO])[^AIUEOaiueo]t")
    x = p.sub(r"\1D",x)
    p = re.compile("([AIUEO])[^AIUEOaiueo]f")
    x = p.sub(r"\1V",x)
    p = re.compile("([AIUEO])[^AIUEOaiueo][kh]")
    x = p.sub(r"\1G",x)
    p = re.compile("([AIUEO])[^AIUEOaiueo]p")
    x = p.sub(r"\1B",x)
    ###C1の子音変化
    p = re.compile("p(y*?)([aiueo])")
    x = p.sub(r"f\1\2",x)
    p = re.compile("v(y*?)([aiueo])")
    x = p.sub(r"u\1\2",x)
    p = re.compile("d(y*?)([aiueo])")
    x = p.sub(r"r\1\2",x)
    p = re.compile("[kg](y*?)([aiueo])")
    x = p.sub(r"h\1\2",x)
    ###C2の子音変化
    p = re.compile("([aiueo])f")
    x = p.sub(r"\1p",x)
    p = re.compile("([aiueo])[td]")
    x = p.sub(r"\1r",x)
    p = re.compile("([aiueo])v")
    x = p.sub(r"\1u",x)
    p = re.compile("([aiueo])g")
    x = p.sub(r"\1h",x)
    ###強勢のない半母音の母音化
    p = re.compile("[y']([^AIUEO])")
    x = p.sub(r"\1",x)
    ###ts-->c
    p = re.compile("[tT][sS]")
    x = p.sub(r"c",x)
    #print('sekore:'+x)
    x = ortho2(x)
    x = strip(x)
    return x

def titauini(w):
    ###3母音化
    x = w.translate(str.maketrans('oOE','eUI'))
    ###C2強勢時(後の変化に巻き込まれないよう大文字化)
    x = w.translate(str.maketrans('jdbw','drwq'))
    #print('titauini:'+x)
    x = ortho2(x)
    x = strip(x)
    return x

def kaiko(w):
    ###s,r変化
    p = re.compile("s([ieIE])")
    x = p.sub(r"sy\1",w)
    x = x.replace('se','x')
    p = re.compile("r([auAU])")
    x = p.sub(r"ry\1",x)
    x = x.replace('ro','l')
    ###強勢音節母音変化
    x = x.replace('Easi','AU')
    x = x.replace('A','AI')
    x = x.replace('O','EI')
    x = x.replace('U','OU')
    ###語末子音削除
    p = re.compile("[^aiueoAIUEO]φ")
    x = p.sub(r"φ",x)
    ###子音変化
    p = re.compile("g([aiueoAIUEO])")
    x = p.sub(r"ny\1",x)
    x = x.translate(str.maketrans('vh','uu'))
    x = x.replace('zy','i')
    ###連続子音変化
    p = re.compile("[^aiueoAIUEOxly#]([^aiueoAIUEOxly])")
    x = p.sub(r"\1\1",x)
    p = re.compile("[^aiueoAIUEOxly#]x")
    x = p.sub(r"sx",x)
    p = re.compile("[^aiueoAIUEOxly#]l")
    x = p.sub(r"rl",x)
    #print('kaiko:'+x)
    x = ortho2(x)
    x = strip(x)
    return x

def arzafire(w):
    x = w.translate(str.maketrans('aiueoAIUEO','iueoaIUEOA'))
    x = x.translate(str.maketrans('kstnhmyrwgzdbp','stnhmrrrkzdbgp'))
    #print('arzafire:'+x)
    return x

while True:
    word = '#'+input('元単語（アクセントは大文字）: ')+'φ'
    word = ortho1(word)
    
    if commone(word)==commonf(word):
        print('旗艦方言(Sekore)        :'+sekore(commone(word)))
        print('資源循環艦方言(Titauini):'+titauini(commone(word)))
        print('探査艦方言(Kaiko)       :'+kaiko(commone(word)))
    else:
        print('旗艦方言(Sekore)        :'+sekore(commone(word))+'または'+sekore(commonf(word)))
        print('資源循環艦方言(Titauini):'+titauini(commone(word))+'または'+titauini(commonf(word)))
        print('探査艦方言(Kaiko)       :'+kaiko(commone(word))+'または'+kaiko(commonf(word)))
    if commone(arzafire(word))==commone(arzafire(word)):
        print('教団暗号(Arzafire)      :'+sekore(commone(arzafire(word))))
    else:
        print('教団暗号(Arzafire)      :'+sekore(commone(arzafire(word)))+'または'+sekore(commonf(arzafire(word))))
    print('---------------------------')
