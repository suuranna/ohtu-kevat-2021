import requests
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def goals_and_assists(player):
    return player.goals + player.assists

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
#    response = requests.get(url).json()

#    print("JSON-muotoinen vastaus:")
#    print(response)

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

#    players = []

#    for player_dict in response:
#        player = Player(
#            player_dict['name'],
#            player_dict['team'],
#            player_dict['goals'],
#            player_dict['assists'],
#            player_dict['nationality']
#        )

#        players.append(player)

#    new_players = []
#    for player in players:
#        if player.nationality == "FIN":
#            new_players.append(player)
#
#    new_players.sort(key=goals_and_assists, reverse=True)

#    print("Oliot:")

#    for player in new_players:
#        print(player)

if __name__ == "__main__":
    main()
