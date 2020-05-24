from urllib3 import PoolManager
from bs4 import BeautifulSoup
from tqdm import tqdm

page_count = 1
prefix = "https://footballia.net"
player_full_name = "Cristiano Ronaldo dos Santos Aveiro"  # The complete full name of the player is required
url_name = "-".join(player_full_name.split(" "))

with open('matches.txt', 'w+') as file:
    file.writelines("------ List of Football Matches played by " + player_full_name + " ------")


while True:
    url = "https://footballia.net/players/" + url_name + "?mode=player&page=" + str(page_count)
    getUrl = PoolManager().request('GET', url).data
    soup = BeautifulSoup(getUrl, "lxml")

    games_list = soup.findAll('td', attrs={'class': 'match'})
    competition = soup.findAll('td', attrs={'class': 'competition hidden-xs'})
    season = soup.findAll('td', attrs={'class': 'season'})

    serial = 1
    counter = 0

    if len(games_list) == 0:
        break

    with open('matches.txt', 'a') as file:
        file.writelines("\n\n Page " + str(page_count))

    for item in tqdm(games_list):
        match = item.findChildren('div', attrs={'class': 'hidden-md hidden-lg'})
        fixture = match[0].findChildren('a')[0].contents[0].encode('utf-8').decode('ascii', 'ignore')
        link = match[0].findChildren('a')[0].get('href')
        match_season = season[counter].contents[0]
        match_type = competition[counter].contents[0]
        with open('matches.txt', 'a') as file:
            file.writelines("\n" + str(serial) + ". " + str(match_type) + " Match: " + str(fixture) + " " + str(match_season) +
            " season" + "\tLink: " + prefix + str(link))
        serial += 1
        counter += 1

    page_count += 1

print("All Matches Updated")



# for date in list(season):
#     print(date.contents[0], type(date))
#
# mySeason = list(season)
# print(season[0].contents[0])

# url = "https://footballia.net/players/lionel-leo-andres-messi?mode=player&page=1000"
# # print("Page "+str(page_count) + "\n")
# getUrl = PoolManager().request('GET', url).data
# soup = BeautifulSoup(getUrl, "lxml")
# games_list = soup.findAll('td', attrs={'class': 'match'})
# print(len(games_list))

