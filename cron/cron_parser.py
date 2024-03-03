from cron.cron_field import CronField

class CronParser:
    """
    CronParser class is responsible for parsing a cron string and displaying its components.

    Attributes:
    - fields: A list of CronField objects representing different components of the cron expression.
    - command: A string representing the command to be executed.

    Methods:
    - __init__(cron_string): Initializes a CronParser object with the provided cron string.
    - parse_cron_string(cron_string): Parses the provided cron string and populates the fields and command attributes.
    - display(): Displays the parsed components of the cron expression.
    """

    def __init__(self, cron_string):
        """
        Initializes a CronParser object with the provided cron string.

        Parameters:
        - cron_string (str): The cron string to be parsed.
        """
        self.fields = [
            CronField("minute", 0, 59),
            CronField("hour", 0, 23),
            CronField("day of month", 1, 31),
            CronField("month", 1, 12),
            CronField("day of week", 1, 7),  # Sunday = 1 through Saturday = 7
        ]
        self.command = ""
        self.parse_cron_string(cron_string)

    def parse_cron_string(self, cron_string):
        """
        Parses the provided cron string and populates the fields and command attributes.

        Parameters:
        - cron_string (str): The cron string to be parsed.
        """
        parts = cron_string.split()
        if len(parts) != 6:
            raise ValueError("Invalid cron string format. Expected 6 parts.")
        for i, part in enumerate(parts[:-1]):
            self.fields[i].parse(part)
        self.command = parts[-1]

    def display(self):
        """
        Displays the parsed components of the cron expression.
        """
        for field in self.fields:
            print(field.display())
        print(f"{'command'.ljust(14)}{self.command}")
