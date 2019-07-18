from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote
import re
import pytest

MINWORDLEVEL = 7

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
            if isLowerThanMinLevel(getWordLevelFromKan(match[0])):
                f.write(line)
                print("keep")
            else:
                print("delete")
        f.truncate()
    
def getWordLevelFromKan(word: str) -> int:
    kan_url = "https://www.kanshudo.com/word/" + quote(word)
    kan_page = urllib.request.urlopen(kan_url).read()
    soup = BeautifulSoup(kan_page,'html.parser')
    child = soup.find(href='/howto/usefulness')
    try:
        parent = child.find_parent("div")
        level = int(parent.contents[2][2]+parent.contents[2][3])
    except:
        print("revision needed")
        return -1
    return level

def isLowerThanMinLevel(wordLevel: int) -> bool:
    if wordLevel < MINWORDLEVEL:
        return True
    else:
        return False

def test_wordLevelLowerThanMinLevel():
    assert isLowerThanMinLevel(1) == True

def test_wordLevelHigherThanMinLevel():
    assert isLowerThanMinLevel(8) == False

def main():
    filterWordsFromDeck()

if __name__ == "__main__":
    main()
