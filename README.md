# **Cron Expression Parser**

## **Introduction**

This Python project provides a simple tool for parsing cron expressions. It interprets the individual fields of a cron expression (minute, hour, day of the month, month, day of the week) and the command to be executed. The tool then displays the times at which a given cron job will run.

## **Installation**

### **Requirements**

- Python 3.6 or higher

### **Setup**

Clone this repository to your local machine using:

```bash
git clone https://github.com/atul107/cron-parser.git
cd cron-parser

```

## **Usage**

To use the cron expression parser, run the **`main.py`** script from the command line, passing the cron expression as a single argument:

```bash
python main.py "*/15 0 1,15 * 1-5 /usr/bin/find"

```

This will output the parsed cron fields and the command, like so:

```bash
minute         0 15 30 45
hour           0
day of month   1 15
month          1 2 3 4 5 6 7 8 9 10 11 12
day of week    1 2 3 4 5
command        /usr/bin/find

```

Ensure your cron string is enclosed in quotes to be correctly interpreted by the shell.

## **Development**

### **Project Structure**

The project contains three main files:

- **`cron_field.py`**: Defines the **`CronField`** class for parsing and displaying individual cron fields.
- **`cron_parser.py`**: Contains the **`CronParser`** class for parsing entire cron expressions using **`CronField`** instances.
- **`main.py`**: The entry point of the program, handling command-line input and displaying parsed results.


## **Running Tests**

The test covers basic functionalities of both the **`CronField`** and **`CronParser`** classes:

- For **`CronField`**, it tests parsing of all field types: **``** for every possible value, a range like **`5-9`**, a list like **`1,15,20`**, and a step value like **`/2`**.
- For **`CronParser`**, it includes tests for a valid cron string to check if the parsing is correctly applied, and also for an invalid cron string to ensure it raises a **`ValueError`** as expected.

Run the tests with the following command in your terminal:

```
python -m unittest tests/test_cron_parser.py

```

This command will discover and run all the tests defined in **`test_cron_parser.py`**, reporting the results in the terminal.

