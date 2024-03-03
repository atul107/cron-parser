import unittest
from cron.cron_parser import CronParser
from cron.cron_field import CronField

class TestCronField(unittest.TestCase):
    def test_parse_star(self):
        field = CronField("minute", 0, 59)
        field.parse("*")
        self.assertEqual(field.values, list(range(0, 60)))

    def test_parse_range(self):
        field = CronField("hour", 0, 23)
        field.parse("5-9")
        self.assertEqual(field.values, [5, 6, 7, 8, 9])

    def test_parse_list(self):
        field = CronField("day of month", 1, 31)
        field.parse("1,15,20")
        self.assertEqual(field.values, [1, 15, 20])

    def test_parse_step(self):
        field = CronField("month", 1, 12)
        field.parse("*/2")
        self.assertEqual(field.values, [1, 3, 5, 7, 9, 11])

class TestCronParser(unittest.TestCase):
    def test_valid_cron_string(self):
        cron_string = "*/15 0 1,15 * 1-5 /usr/bin/find"
        parser = CronParser(cron_string)
        parser.display()  
        self.assertEqual(parser.fields[0].values, list(range(0, 60, 15)))

    def test_invalid_cron_string(self):
        cron_string = "*/15"
        with self.assertRaises(ValueError):
            CronParser(cron_string)

if __name__ == '__main__':
    unittest.main()

