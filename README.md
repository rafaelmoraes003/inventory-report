<h1 align="left">Inventory Report</h1>

###

<p align="left">In this project, a report generator was implemented that receives as input files (csv, json or xml) with data from a stock and generates, as output, a report about these data.<br><br>The objective of the project was to work with object-oriented programming and design patterns in Python.</p>

###

<h2 align="left">Technologies used</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50" width="62" alt="python logo"  />
</div>

###

<h2 align="left">How to use the application</h2>

###

Clone the application using the `git clone` command. After that, enter the project folder using the command `cd inventory-report`.

###

<h2 align="left">How to run the application</h2>

1. Create the virtual environment for the project
- `python3 -m venv .venv && source .venv/bin/activate`

2. Install the dependencies
- `python3 -m pip install -r dev-requirements.txt`

3. To get a report, use the command:
- `python3 -m inventory_report.main <path_to_file_with_data> <report_type>`

- Examples:
1. Simple Report: `python3 -m inventory_report.main inventory_report/data/inventory.csv simples`
2. Complete Report: `python3 -m inventory_report.main inventory_report/data/inventory.csv completo`

## `Important: Only csv, json and xml files are allowed.`

###
