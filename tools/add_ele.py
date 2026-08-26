import sqlite3

conn = sqlite3.connect("./data/clubs.db")
c = conn.cursor()

# --------- Add Column --------- #
# ALTER TABLE Clubs ADD COLUMN tier TEXT


# --------- Update Column Tier --------- #
c.execute("""
    UPDATE Clubs SET tier = 'S' WHERE short_name IN ('PSG', 'Arsenal')
    """)

conn.commit()
conn.close()



# SELECT short_name FROM Clubs WHERE tier = 'S'
