from bs4 import BeautifulSoup
import requests


def soup(source):
    return BeautifulSoup(requests.get(source).content, "html.parser")
