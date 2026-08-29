import sqlite3

conn = sqlite3.connect("./data/events.db")
c = conn.cursor()

# ====================== EXE COMMANDS ====================== #
c.execute("""
        UPDATE Media_Events
    SET effect_1 = REPLACE(effect_1, 'Relationship_coach', 'relationship_coach'),
    effect_2 = REPLACE(effect_1, 'Relationship_coach', 'relationship_coach');

  """)

conn.commit()
conn.close()

# SELECT short_name FROM Clubs WHERE tier = 'S'
# UPDATE Clubs SET tier = 'D2' WHERE league_id = '2016'
# UPDATE Clubs SET tier = 'C' WHERE tier IS NULL
# ALTER TABLE Media_Events ADD COLUMN comment_2 TEXT
# DELETE FROM Media_Events
# Pour sup une table: c.execute("DROP TABLE IF EXISTS Training_Events")
"""UPDATE FootballMoment_Events
    SET effect_1 = REPLACE(effect_1, 'Locker room', 'Locker_room'),
    effect_2 = REPLACE(effect_2, 'Locker room', 'Locker_room'),
    effect_3 = REPLACE(effect_3, 'Locker room', 'Locker_room');
"""