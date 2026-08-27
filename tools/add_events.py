import sqlite3

conn = sqlite3.connect("./data/events.db")
c = conn.cursor()

# ====================== CREATE TYPE EVENTS ====================== #
c.execute("""
    CREATE TABLE IF NOT EXISTS Media_Events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    answer_1 TEXT NOT NULL,
    effect_1 TEXT NOT NULL,
    comment_1 TEXT NOT NULL,
    answer_2 TEXT NOT NULL,
    effect_2 TEXT NOT NULL,
    comment_2 TEXT NOT NULL,
    type_event TEXT,
    type_effect TEXT,
    probability REAL
    )
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS Relationship_Events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    answer_1 TEXT NOT NULL,
    effect_1 TEXT NOT NULL,
    comment_1 TEXT NOT NULL,
    answer_2 TEXT NOT NULL,
    effect_2 TEXT NOT NULL,
    comment_2 TEXT NOT NULL,
    type_event TEXT,
    type_effect TEXT,
    probability REAL
    )
""")


c.execute("""
    CREATE TABLE IF NOT EXISTS FootballMoment_Events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    answer_1 TEXT NOT NULL,
    effect_1 TEXT NOT NULL,
    comment_1 TEXT NOT NULL,
    answer_2 TEXT NOT NULL,
    effect_2 TEXT NOT NULL,
    comment_2 TEXT NOT NULL,
    answer_3 TEXT NOT NULL,
    effect_3 TEXT NOT NULL,
    comment_3 TEXT NOT NULL,
    post TEXT NOT NULL,
    type_event TEXT,
    probability REAL
    )
""")


# =============================================================== #




# ========================== ADD EVENT ========================== #

events = [

    {
        "id": 160,
        "title": "Dernière frappe",
        "description": "L'adversaire obtient une dernière occasion dans la surface. L'attaquant frappe à quelques mètres.",
        "answer_1": "**Sortie réflexe**",
        "effect_1": "reputation+3,mental+3,forme-1,locker_room+1",
        "comment_1": "Vous réalisez une parade exceptionnelle qui maintient votre équipe devant.",
        "answer_2": "**Fermer l'angle**",
        "effect_2": "mental+2,reputation+1",
        "comment_2": "Vous réduisez l'espace et repoussez la frappe.",
        "answer_3": "**Sortir les mains en avant sans contrôle**",
        "effect_3": "reputation-2,mental-3,locker_room-1",
        "comment_3": "Votre intervention est mal maîtrisée et le ballon revient dans les pieds adverses.",
        "post": "goalkeeper",
        "type_event": "FootballMoment",
        "probability": 1
    },
]
# ====================== INSERT DICT TO TABLE ====================== #

for i in range(len(events)):
  c.execute("""
      INSERT INTO FootballMoment_Events 
      VALUES (
          :id,
          :title,
          :description,
          :answer_1,
          :effect_1,
          :comment_1,
          :answer_2,
          :effect_2,
          :comment_2,
          :answer_3,
          :effect_3,
          :comment_3,
          :post,
          :type_event,
          :probability
      )
  """, events[i])

conn.commit()
conn.close()

# =============================================================== #

