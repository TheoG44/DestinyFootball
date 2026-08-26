import sqlite3


def random_choice_club():
    """
      Randomly select 5 clubs in clubs.db
      
      Args: Nationality (str)
      
      Returns: List of 5 clubs
    """
    club_list = []
    
    conn = sqlite3.connect("./data/clubs.db")
    c = conn.cursor()
    
    for _ in range(5):
      c.execute(
            "SELECT short_name, club_colors, country FROM Clubs JOIN Leagues ON Clubs.league_id = Leagues.id ORDER BY RANDOM() LIMIT 1"
            )
      row = c.fetchone()
      
      if row is None:
            conn.close()
            return None

      club_list.append(row)
      
    conn.close()
    
    return display_color_club(club_list)


def display_color_club(club_list):

    colors = {
        "White": "⚪",
        "Red": "🔴",
        "Crimson": "🔴",
        "Claret": "🔴",
        "Blue": "🔵",
        "Navy Blue": "🔵",
        "Sky Blue": "🩵",
        "Yellow": "🟡",
        "Green": "🟢",
        "Black": "⚫",
        "Orange": "🟠",
        "Brown": "🟤",
        "Purple": "🟣",
        "Violet": "🟣"
    }

    flags = {
      "Spain": "🇪🇸 ",
      "Italy": "🇮🇹 ",
      "France": "🇫🇷 ",
      "Germany": "🇩🇪 ",
      "Netherlands": "🇳🇱 ",
      "England": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
      "Portugal": "🇵🇹 ",
      
      
    }
    for club, chain, countrys in club_list:

        club_colors = chain.split(" / ")

        emojis = []

        for color in club_colors:
            emojis.append(colors[color])

          
        print(f"[{club}, {''.join(emojis)}, {flags[countrys]}]\n")


