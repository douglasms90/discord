from bs4 import BeautifulSoup
import requests


def website(source):
    return BeautifulSoup(requests.get(source).content, "html.parser")
