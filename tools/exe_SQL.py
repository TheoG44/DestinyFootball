import sqlite3

conn = sqlite3.connect("./data/events.db")
c = conn.cursor()

# ====================== EXE COMMANDS ====================== #
c.execute("""
        DROP TABLE IF EXISTS FootballMoment_Events
      
      """)

conn.commit()
conn.close()

# SELECT short_name FROM Clubs WHERE tier = 'S'
# UPDATE Clubs SET tier = 'D2' WHERE league_id = '2016'
# UPDATE Clubs SET tier = 'C' WHERE tier IS NULL
# ALTER TABLE Media_Events ADD COLUMN comment_2 TEXT
# DELETE FROM Media_Events
# Pour sup une table: c.execute("DROP TABLE IF EXISTS Training_Events")