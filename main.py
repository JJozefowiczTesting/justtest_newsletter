import bs4
import requests

# https://nostarch.com/automatestuff2
# https://nostarch.com/automatestuffresources
# https://automatetheboringstuff.com/
# https://www.youtube.com/watch?v=1F_OgqRuSdI&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW
# https://codewith.mu/en/
#
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    res = requests.get('https://testuj.pl/blog/')
    res.raise_for_status()
    soup   = bs4.BeautifulSoup(res.text, "html.parser")
    titles = soup.select('.col-lg-3 h3')
    par    = soup.select('.col-lg-3 p')
    j      = 0
    dates  = []
    group  = []
    for i in range(len(par)):
        if i % 2 == 0:
            group.append(par[i].text)
        else:
            dates.append(par[i].text)
    links = soup.select('.popular-article__image a')
    for i in range(len(titles)):
        print(str(i) + ' [' + dates[i].strip() + '] ' + titles[i].text.strip() + ' ' + links[i].get("href"))
