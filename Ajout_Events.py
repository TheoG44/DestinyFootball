
import sqlite3

conn = sqlite3.connect("./data/events.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS Media_Events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    answer_1 TEXT NOT NULL,
    effect_1 TEXT NOT NULL,
    answer_2 TEXT NOT NULL,
    effect_2 TEXT NOT NULL,
    probability REAL
)
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS Training_Events (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    effect TEXT NOT NULL,
    probability REAL NOT NULL
)
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS Career_Events (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    club_interest TEXT NOT NULL,
    probability REAL NOT NULL
)
""")

event = {
    "id": 1,
    "title": "Le jeune pigiste",
    "description": "Un jeune pigiste local vous suit depuis vos débuts. Après l'entraînement, il ose : « Le jour où tu soulèves un vrai trophée, c'est moi qui écris ta biographie. Promis ? »",
    "answer_1": "Promettre, poignée de main",
    "effect_1": "reputation+5",
    "answer_2": "Sourire sans promettre",
    "effect_2": "reputation-1",
    "probability": 2
}


c.execute("""
    INSERT INTO Media_Events
    VALUES (
        :id,
        :title,
        :description,
        :answer_1,
        :effect_1,
        :answer_2,
        :effect_2,
        :probability
    )
""", event)


conn.commit()
conn.close()
