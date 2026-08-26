import sqlite3


# ================================================================================ #

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
            "SELECT short_name, club_colors, country, tier FROM Clubs JOIN Leagues ON Clubs.league_id = Leagues.id WHERE tier = 'D2' ORDER BY RANDOM() LIMIT 1"
            )
      row = c.fetchone()
      
      if row is None:
            conn.close()
            return None

      club_list.append(row)
      
    conn.close()
    
    return club_list


# ================================================================================ #


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
        "Gold": "🟡",
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
    i = 0
    for club, chain, countrys, tier in club_list:

        i += 1
        club_colors = chain.split(" / ")

        emojis = []

        for color in club_colors:
            emojis.append(colors[color])

          
        print(f"[{i}]{club}, {''.join(emojis)}, {flags[countrys]}, {tier}]\n")



# ================================================================================ #

def stat_update_event(effect: str, dic):
  chain_effect = effect.split(",")

  list_stat = []
  list_effect = []

  for i in range(len(chain_effect)):
    
    chain = chain_effect[i]
    
    if chain.rfind('-') != -1:
        ind = chain.rfind('-') + 1
        num = "-"
        num += chain[ind] 
        num = int(num)
        list_effect.append(num)
        tr = chain[:chain.rfind('-')]
        list_stat.append(tr.capitalize())
        
    elif chain.rfind('+') != -1:
        ind = chain.rfind('+') + 1
        num = chain[ind] 
        num = int(num)
        list_effect.append(num)
        tr = chain[:chain.rfind('+')]
        list_stat.append(tr.capitalize())
    
  for j in range(len(list_stat)):
    dic[list_stat[j]] = dic[list_stat[j]]+list_effect[j]
    
    
  return dic


# ================================================================================ #

def choice_answer_event(event):
  
  choice = int(input("Choissisez votre réponse (1. ou 2.): "))
  if choice == 1:
    effect = event.effect_1
  elif choice == 2:
    effect = event.effect_2
  else:
    print("Error")
    return -1
  
  return effect

# ================================================================================ #

def choice_answer_club(club_list):

  choice = int(input("Choissisez votre réponse (1/2/3/4/5): "))
  if choice == 1:
      club = club_list[0][0]
  elif choice == 2:
      club = club_list[1][0]
  elif choice == 3:
      club = club_list[2][0]
  elif choice == 4:
      club = club_list[3][0]
  elif choice == 5:
      club = club_list[4][0]
  else:
    print("Error")
    return -1
  print(f"Vous avez bien choisi {club} comme club de départ !")
  
  return club
