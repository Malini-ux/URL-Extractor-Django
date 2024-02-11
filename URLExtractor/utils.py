from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_urls_from_webpage(html_content, base_url):
    soup = BeautifulSoup(html_content, "html.parser")
    links = []
    for link_tag in soup.find_all("a", href=True):
        link = link_tag["href"]
        link_type = get_link_type(link, base_url)
        links.append({"link": link, "link_type": link_type})
        #print("link type",links)
    return links

def get_link_type(link, base_url):
    parsed_link = urlparse(link)
    parsed_base_url = urlparse(base_url)
    if parsed_link.scheme and parsed_link.netloc:
        if parsed_link.netloc == parsed_base_url.netloc:
            return "Internal"
        else:
            return "External"
    elif parsed_link.scheme == '' and parsed_link.netloc == '':
        return "Relative"
    else:
        return "Other"
