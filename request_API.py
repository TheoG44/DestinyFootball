# API : https://www.football-data.org/

import requests # type: ignore
import sqlite3

TOKEN = "f21402049a1349b7b4033ed510944121"

conn = sqlite3.connect("./data/database.db")
c = conn.cursor()

headers = {
    "X-Auth-Token": TOKEN
}

# Table des championnats
c.execute("""
    CREATE TABLE IF NOT EXISTS Leagues (
        id INTEGER PRIMARY KEY,
        name TEXT,
        country TEXT
    )
""")

# Table des clubs
c.execute("""
    CREATE TABLE IF NOT EXISTS Clubs (
        id INTEGER PRIMARY KEY,
        name TEXT,
        short_name TEXT,
        tla TEXT,
        crest TEXT,
        founded INTEGER,
        club_colors TEXT,
        venue TEXT,
        league_id INTEGER,

        FOREIGN KEY (league_id) REFERENCES Leagues(id)
    )
""")

conn.commit()

response = requests.get(
    "https://api.football-data.org/v4/competitions/",
    headers=headers
)
data = response.json()

league_id = None

for competition in data["competitions"]:
    print(competition["name"])
    if competition["name"] == "Primera Division":
      
      league_id = competition["id"]
      print(competition["id"])

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

c.execute("""
    SELECT name, short_name, league_id
    FROM Clubs
""")

clubs = c.fetchall()

print("\nClubs dans la BDD :")

for club in clubs:
    print(club)

conn.close()