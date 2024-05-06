import statistics

''' 
This module provides a reusable byline for the author's services.
'''

# Define Variables of Different Types
company_name: str = "Data Insights Solutions"
owner_name: str = "Laura Dooley"
count_active_projects: int = 5
has_international_presence: bool = False
average_client_satisfaction: float = 4.7
services_offered: list = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
service_prices: dict = {"Data Analysis": 1500, "Machine Learning Consulting": 2500, "Business Intelligence Solutions": 2000}
satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
service_completed_projects: dict = {"Data Analysis": 25, "Machine Learning Consulting": 15, "Business Intelligence Solutions": 18}

def calculate_descriptive_statistics(scores: list) -> dict:
    '''Calculate descriptive statistics for the given list of scores'''
    smallest = min(scores)
    largest = max(scores)
    total = sum(scores)
    count = len(scores)
    mean = statistics.mean(scores)
    mode = statistics.mode(scores)
    median = statistics.median(scores)
    standard_deviation = statistics.stdev(scores)
    return {
        "smallest": smallest,
        "largest": largest,
        "total": total,
        "count": count,
        "mean": mean,
        "mode": mode,
        "median": median,
        "standard_deviation": standard_deviation
    }

def generate_byline():
    '''Generate the byline string'''
    active_projects_string = f"Active Projects: {count_active_projects}"
    total_completed_projects = sum(service_completed_projects.values())
    completed_projects_string = f"Total Completed Projects: {total_completed_projects}"
    international_presence_string = f"International Presence: {has_international_presence}"
    client_satisfaction_string = f"Average Client Satisfaction: {average_client_satisfaction}"

    # Combine services with their prices
    services_with_prices = [f"{service} (${service_prices[service]})" for service in services_offered]

    # Calculate the average cost of all services combined
    average_cost = statistics.mean(service_prices.values())

    services_offered_string = f"Services Offered: {', '.join(services_with_prices)}"
    average_cost_string = f"Average Cost of Services: ${average_cost:.2f}"

    # Calculate descriptive statistics for satisfaction scores
    stats = calculate_descriptive_statistics(satisfaction_scores)

    # Format the total with one decimal place
    total_formatted = f"{stats['total']:.1f}"

    stats_string = f"""
    Descriptive Statistics for Our Satisfaction Scores:
      Smallest: {stats['smallest']}
      Largest: {stats['largest']}
      Total: {total_formatted}
      Count: {stats['count']}
      Mean: {stats['mean']}
      Mode: {stats['mode']}
      Median: {stats['median']}
      Standard Deviation: {stats['standard_deviation']}
    """

    # String indicating looking forward to helping
    looking_forward_string = "We look forward to helping you unlock the insights hidden within your data!"

    byline = f"""
    {company_name}
    Created by: {owner_name}
    {active_projects_string}
    {completed_projects_string}
    {international_presence_string}
    {client_satisfaction_string}
    {services_offered_string}
    {average_cost_string}
    {stats_string}
    {looking_forward_string}
    """
    return byline

# Define Main Function
def main():
    ''' Display all output'''
    print(generate_byline())

# Conditional Script Execution
if __name__ == '__main__':
    main()
