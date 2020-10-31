from bs4 import BeautifulSoup as bs
import requests


def main():
    print('MAIN')

    tc_html = requests.get("https://www.techcrunch.com/")
    soup = bs(tc_html.text, "html.parser")
    # print(soup.prettify())
    hyperlinks = soup.find_all('a');
    for link in hyperlinks:
        # for child in link.children:
        #     print(repr(child))
        # print(link)
        sub_soup = bs(str(link), 'html.parser')
        for strr in sub_soup.stripped_strings:
            print(strr)
        # print(sub_soup)
        # print(sub_soup.contents.a.href)


if __name__ == '__main__':
    main()
