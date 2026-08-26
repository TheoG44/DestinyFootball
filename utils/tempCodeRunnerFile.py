 def display_event(self):
        """
          Formats the event for display in the terminal.

          Returns: Formatted text for the event.
        """
        return f"""
🖋️ Médias

{self.title}

{self.description}

[1] {self.answer_1}

[2] {self.answer_2}
"""