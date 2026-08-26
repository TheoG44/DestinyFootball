# API : https://www.football-data.org/

import requests 
import sqlite3

TOKEN = "f21402049a1349b7b4033ed510944121"



conn = sqlite3.connect("./data/clubs.db")
c = conn.cursor()

headers = {
    "X-Auth-Token": TOKEN
}


# ====================== INSERT NEW LEAGUE INTO LEAGUE ====================== #
response = requests.get(
    "https://api.football-data.org/v4/competitions/",
    headers=headers
)
data = response.json()

league_id = None

for competition in data["competitions"]:
    if competition["name"] == "Eredivisie":
      
      league_id = competition["id"]

      c.execute("""
            INSERT OR IGNORE INTO Leagues (
                id,
                name,
                country
            )
            VALUES (?, ?, ?)
        """, (
            competition["id"],
            competition["name"],
            competition["area"]["name"]
        ))

      break
    
conn.commit()


# ====================== INSERT NEW CLUB INTO CLUB ====================== #
response = requests.get(
    f"https://api.football-data.org/v4/competitions/{league_id}/teams",
    headers=headers
)

teams = response.json()

for team in teams["teams"]:
    print(team["id"], team["name"])
    
    c.execute("""
        INSERT OR IGNORE INTO Clubs (
            id,
            name,
            short_name,
            tla,
            crest,
            founded,
            club_colors,
            venue,
            league_id
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        team["id"],
        team["name"],
        team["shortName"],
        team["tla"],
        team["crest"],
        team["founded"],
        team["clubColors"],
        team["venue"],
        league_id
    ))

conn.commit()

# ====================== DISPLAY ALL CLUBS ====================== #
c.execute("""
    SELECT name, short_name, league_id
    FROM Clubs
""")

clubs = c.fetchall()

print("\nClubs dans la BDD :")

for club in clubs:
    print(club)

conn.close()
