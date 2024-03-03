import sys
from cron.cron_parser import CronParser

def main():
    """
    Main function to parse and display the components of a cron string.

    Usage:
    python main.py '<cron_string>'

    Example:
    python main.py '*/15 * * * * /usr/bin/find'

    The cron string should consist of six space-separated fields:
    minute hour day_of_month month day_of_week command

    Each field accepts various formats including single values, ranges, and step values.

    Raises:
    - ValueError: If the provided cron string does not contain six parts.
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py '<cron_string>'")
        sys.exit(1)

    cron_string = sys.argv[1]
    parser = CronParser(cron_string)
    parser.display()

if __name__ == "__main__":
    main()
