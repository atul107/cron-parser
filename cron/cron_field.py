class CronField:
    """
    CronField class represents a field in a cron expression.

    Attributes:
    - name: The name of the cron field.
    - min_value: The minimum allowed value for the field.
    - max_value: The maximum allowed value for the field.
    - values: A list containing the parsed values of the field.

    Methods:
    - parse(field): Parses the input field string and populates the 'values' list accordingly.
    - display(): Generates a formatted string representing the name of the field and its parsed values.
    """

    def __init__(self, name, min_value, max_value):
        """
        Initializes a CronField object with the specified name, minimum value, and maximum value.

        Parameters:
        - name (str): The name of the cron field.
        - min_value (int): The minimum allowed value for the field.
        - max_value (int): The maximum allowed value for the field.
        """
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.values = []

    def parse(self, field):
        """
        Parses the input field string and populates the 'values' list accordingly.

        Parameters:
        - field (str): The field string to be parsed.
        """
        if field == "*":
            self.values = list(range(self.min_value, self.max_value + 1))
        elif "," in field:
            for part in field.split(","):
                self.parse(part)
        elif "-" in field:
            start, end = map(int, field.split("-"))
            self.values.extend(range(start, end + 1))
        elif "/" in field:
            base, step = field.split("/")
            if base == "*":
                base = self.min_value
            else:
                base = int(base)
            step = int(step)
            self.values.extend(range(base, self.max_value + 1, step))
        else:
            self.values.append(int(field))

    def display(self):
        """
        Generates a formatted string representing the name of the field and its parsed values.

        Returns:
        - str: A formatted string containing the name of the field and its parsed values.
        """
        return f"{self.name.ljust(14)}{' '.join(map(str, self.values))}"
