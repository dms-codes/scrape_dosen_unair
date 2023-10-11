import requests
from bs4 import BeautifulSoup as bs
import csv
import string

# Constants
BASE_URL = "https://unair.ac.id/daftar-fakultas/"
TIMEOUT = 30
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

# Function to extract and clean text from an element
def extract_text(element):
    return element.text.strip() if element else ''

# Function to extract faculty URLs
def extract_faculties(soup):
    faculty_elements = soup.find_all('div', class_='elementor-button-wrapper')[2:-5]
    return [e.find('a', href=True)['href'] for e in faculty_elements]

# Function to generate pages URLs for each faculty
def extract_pages(faculty_url):
    return [f"{faculty_url}&pages={atoz}" for atoz in string.ascii_lowercase]

# Function to extract information from lecturer pages
def extract_dosen_pages(soup):
    results = []
    for col in soup.find_all('div', class_="col-md-10"):
        url = col.find('a', href=True)['href']
        rows = [d.text for d in col.find_all('div', class_='row')]
        rows[2] = url
        rows[3] = rows[3].replace(' (at) ','@')
        results.append(rows)
    return results

s = requests.Session()
html = s.get(BASE_URL, timeout=TIMEOUT, headers=HEADERS).content
soup = bs(html, 'html.parser')

with open('data_dosen_unair.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    header = ['Nama', 'Fakultas', 'URL', 'Email']
    writer.writerow(header)
    
    for faculty_url in extract_faculties(soup):
        for page_url in extract_pages(faculty_url):
            html_ = s.get(page_url, timeout=TIMEOUT, headers=HEADERS).content
            soup_ = bs(html_, 'html.parser')
            dosen_pages = extract_dosen_pages(soup_)
            writer.writerows(dosen_pages)
            f.flush()
