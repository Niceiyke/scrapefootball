import requests
from bs4 import BeautifulSoup


def scrape_links():
    years =list(range(2023,2009 ,-1))
    standing_url=f'https://fbref.com/en/comps/9'
    all_links=[]
    links=[]
    for year in years:
            print(year)
            print(standing_url)
            data=requests.get(standing_url)
            soup=BeautifulSoup(data.text)
            standing_table=soup.select('table.stats_table')[0]
            lin=standing_table.find_all('a')
            lin=[link.get('href')for link in lin]
            lin=[link for link in lin if '/squads' in link]
            team_urls =[f'https://fbref.com{link}' for link in lin]
            print(team_urls)
            links.append(team_urls)

            previous_season = soup.find_all("a", class_="prev")[0].get('href')
            print(previous_season)
            standing_url =f'https://fbref.com{previous_season}'

    for link in links:
        for team in link:
            all_links.append(team)
    
    return all_links

if __name__ =="__main__":
    scrape_links() 