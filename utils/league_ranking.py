from utils.player import Player
import sqlite3
import random

def create_league_ranking(player: Player) :
  
  club = player.club
  
  conn = sqlite3.connect("./data/clubs.db")
  c = conn.cursor()
  
  c.execute(
          "SELECT league_id FROM Clubs WHERE short_name = ?",
            (club,)
      )
  
  league = c.fetchone()
  league = league[0]
  
  c.execute(
        "SELECT short_name, tier FROM Clubs WHERE league_id = ?",
          (league,)
    )
  
  row = c.fetchall() 
  conn.close()
  
  #trier alea le row
  random.shuffle(row)
  rank = {"S": 0,"A": 1,"B": 2,"C": 3}
  
  # ligne a revoir pour trier et ajouter dans la list en fonction tier
  ranking = [club for club, tier in sorted(row, key=lambda x: rank[x[1]])]
  
  return display_league_ranking(ranking)

  
  
def display_league_ranking(ranking: list):
        table = (
          "┌──────────────────────┐\n"
          "│ Ranking              │\n"
          "├──────────────────────┤\n"
        )

        for team in ranking:
          table += f"│ {team:<20} │\n"
          table += f"├──────────────────────┤\n"

        table += "└──────────────────────┘"
        
        return table