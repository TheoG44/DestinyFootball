from dataclasses import dataclass
import sqlite3
import random

# ================================================================================ #

@dataclass
class MediaEvent:

    id: int
    title: str
    description: str
    answer_1: str
    effect_1: str
    comment_1: str
    answer_2: str
    effect_2: str
    comment_2: str
    type_event: str # type d'event (ex: media, carrer,..)
    type_effect: str
    probability: float



    def display_event(self):
        """
          Formats the event for display in the terminal.

          Returns: Formatted text for the event.
        """
        return f"""
  {self.type_event} {self.id} {self.type_effect}

{self.title}

{self.description}

[1] {self.answer_1}

[2] {self.answer_2}

DEBUG : 
    - Comment1 : {self.comment_1} Effect : {self.effect_1}
    - Comment2 : {self.comment_2} Effect : {self.effect_2}
"""

# ================================================================================ #

@dataclass
class RelationshipEvent:
    
    id: int
    title: str
    description: str
    answer_1: str
    effect_1: str
    comment_1: str
    answer_2: str
    effect_2: str
    comment_2: str
    type_event: str # type d'event (ex: media, carrer,..)
    type_effect: str
    probability: float



    def display_event(self):
        """
          Formats the event for display in the terminal.

          Returns: Formatted text for the event.
        """
        return f"""
  {self.type_event} {self.type_effect}

{self.title}

{self.description}

[1] {self.answer_1}

[2] {self.answer_2}

DEBUG : 
    - Comment1 : {self.comment_1} Effect : {self.effect_1}
    - Comment2 : {self.comment_2} Effect : {self.effect_2}
"""





# ================================================================================ #

def get_event_media(id):
    """
      Recover an event from its id.
    
      Args: id (int)
    
      Returns: event (:MediaEvent) -> Object event
    """
    
    conn = sqlite3.connect("./data/events.db")
    c = conn.cursor()

    c.execute(
        "SELECT * FROM Media_Events WHERE id = ?",
        (id,)
    )

    row = c.fetchone()
    conn.close()

    if row is None:
        return None

    event = MediaEvent(
        row[0],
        row[1],
        row[2],
        row[3],
        row[4],
        row[5],
        row[6],
        row[7],
        row[8],
        row[9],
        row[10],
        row[11]
    )
    return event


def random_event():
  """
    Randomly selects a media event.

    Args: None

    Returns: an random event
  """
  id = random.randint(1, 65) # modify param based on number events
  return get_event_media(id)

# ================================================================================ #




# ================================================================================ #
"""
event = random_event()

if event is not None:
    print(event.display_event())
"""


