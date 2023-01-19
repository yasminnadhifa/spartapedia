import requests
from bs4 import BeautifulSoup
# Ini adalah koneksi stringnya 
from pymongo import MongoClient
client = MongoClient('mongodb+srv://yasmin:yasmin28@cluster0.uxms5uf.mongodb.net/?retryWrites=true&w=majority')
#Dipanggil dan dbsparta adalah nama databasenya 
db = client.dbspartaTraining




# Baca URLnya dan ambil HTMLnya,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# Kamu akan memulai "scraping" dari data pada halaman ini
url = 'https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=HCDFFFABJAV421Y70V44&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'

# Gunakan requests library untuk mendapatkan kode HTML dari link diatas
data = requests.get(url=url, headers=headers)

# library BeautifulSoup memudahkan kita dalam
# menguraikan kode HTML tersebut,
soup = BeautifulSoup(data.text, 'html.parser')

# Menggunakan select
movies = soup.select_one('.lister-list >  tr')

title = soup.select_one('meta[property="og:title"]')
print(title['content'])

