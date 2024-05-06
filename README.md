# datafun-01-attr
Project 1 
Specification for Project 1 Python Module
Overview
This project introduces Python for professional data analytics. We cover some syntax and Python basics, but there is much more to using Python professionally. In these first few projects, we introduce syntax along with key tools and skills used in industry. This project focues on basic data types and filel organization while building a reusable Python module. The module provides an introductory byline for a hypothetical data analytics consulting company, while demonstrating skills with data types, f-strings, descriptive statistics, and more.

Deliverable Names
GitHub Repository: datafun-01-attr
Documentation: README.md
Script: yourname_utils.py
Create a new GitHub repository with a default README.md. In your GitHub repository, create new empty file with the name listed above. The name can be your name as an analyst, or reflect a fake name or hypothetical data analytics consulting company, e.g., "case_utils.py" or "stellar_analytics_utils.py".

Objective
Develop a Python module with a byline function displaying information about your data analytics consulting business or analyst profile. The byline should be constructed using various Python data types.

Requirements
1. Project Start
Include a docstring at the top of the file describing its purpose. For example:

''' This module provides a reusable byline for the author's services. '''
2. Import Dependencies
We'll use at least the statistics module from the Python Standard Library. You may use math or others in your code. Anything in the standard library is fair game. After the docstring, we import the modules used in this script. For example:

import math
import statistics
3. Define Variables of Different Types
Define at least one variable of each of these types: str, int, float, bool, list of strings, list of numbers. The following example uses optional type hints. Follow naming conventions for variable names, but create your own names and values. Note boolean values are typically named as a question, e.g., has_international_presence.

company_name: str = "Stellar Analytics Inc."
count_active_projects: int = 5
has_international_presence: bool = False
average_client_satisfaction: float = 4.7
services_offered: list = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
4. Define Formatted Strings
Use f-strings to create formatted strings for non-string variables. For example:

active_projects_string: str = f"Active Projects: {count_active_projects}"
international_presence_string: str = f"International Presence: {has_international_presence}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"
5. Calculate Descriptive Statistics
Use built-in Python functions and the statistics module to calculate descriptive statistics for your numeric list. Python has built-in functions for calculating min(), max(), sum(), and len(). The statistics module provides additional functions for mean(), mode(), median(), and stdev().

CAUTION: Never name a variable min, max, sum, len, or any other built-in function name.

import statistics

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""
6. Define Byline String ⭐
Create a multiline string named byline to display your formatted information. We'll use this byline in a future project. For example:

byline: str = f"""
{company_name}
{active_projects_string}
{international_presence_string}
{client_satisfaction_string}
{services_offered_string}
{stats_string}
"""
7. Define Main Function
Define a main() function that we can call to test our code and display all information.

def main():
    ''' Display all output'''
    print(company_name)
    print(active_projects_string)
    print(international_presence_string)
    print(client_satisfaction_string)
    print(services_offered_string)
    print(numbers_string)
    print(stats_string)

    # If all of the above works, then the byline should work too:
    print(byline)
8. Conditional Script Execution
Execute the main() function when this script is run directly, but not if we import it as a module. Use standard boilerplate code.

if __name__ == '__main__':
    main()
Module Design
Keep the code simple and understandable, focusing on basic Python features. Add notes and experiments as you like. Your README.md should introduce and explain the project.

Evaluation Criteria
Functionality: The project should be functional and meet all requirements.
Documentation: The project should be well-written and well-documented.
Presentation: The project should be presented in a clear and organized manner.
Professionalism: The project should be submitted on-time and reflect an original, creative effort.
See rubric for additional information.

Python Module Examples
CPython JSON Tool
Requests Help Module
Speaking Wikipedia Module
Resources
Python Built-in Functions
Modules and Imports
Python Modules W3 Schools
