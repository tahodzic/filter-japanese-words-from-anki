import pytest
import kanshuudo.main

def test_wordLevelLowerThanMinLevel():
    assert kanshuudo.main.isLowerThanMinLevel(1) == True

def test_wordLevelHigherThanMinLevel():
    assert kanshuudo.main.isLowerThanMinLevel(8) == False