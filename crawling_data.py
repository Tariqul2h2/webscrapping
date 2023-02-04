from requests import get
from bs4 import BeautifulSoup
for i in range(1,10):
    url = f'https://www.cba.org/For-The-Public/Find-A-Lawyer/Results?searchradius=25&page={i}'
    print('Page:',i)
    response = get(url)
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")
    six_columns_det = soup.find_all("div", {"class": "six columns det"})
    if six_columns_det:
        with open(f"lawyer_data.txt", "a") as f:
            for item in six_columns_det:
                    f.write(item.text)
    else:
        print("No matching elements found")