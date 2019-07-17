from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import re

def readWordsFromDeck():
    list = [re.findall(r'(?<=\「).+?(?=\」)',line)
            for line in open('deck.txt',encoding='utf-8')]
    for e in list:
        print(e[0])
    
def filterWordsFromDeck() -> None:
    with open('deck.txt','r+',encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            #Regex to search for words inside 「」
            match = re.search(r'(?<=\「).+?(?=\」)',line)
            #Some lines don't have these brackets. If so, continue.
            if match is None:
                continue
            print("Checking word: ", match[0]," . Result:", end=" ")
            if not getWordLevelFromKan(match[0]):
                f.write(line)
        f.truncate()
    
    
def getWordLevelFromKan(word: str) -> bool:
    kan_url = "https://www.kanshudo.com/word/" + quote(word)
    kan_page = urllib.request.urlopen(kan_url).read()
    soup = BeautifulSoup(kan_page,'html.parser')

    child = soup.find(href='/howto/usefulness')
    try:
        parent = child.find_parent("div")
        level = int(parent.contents[2][2]+parent.contents[2][3])
    except:
        print("revision needed")
        return False
        
    if level < 8:
        print("keep. Level: "+str(level))
        return False
    else:
        print("delete. Level: "+str(level))
        return True

def isHigherThanLevel(wordLevel: int) -> bool:
    if

def main():
    filterWordsFromDeck()

if __name__ == "__main__":
    main()
