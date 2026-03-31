import math
from datetime import datetime
from helper import read_hr_data


def remove_null_salaries(data):
    """
    Remove all records where Salary (index 4) is NaN or missing.
    
    Modifies the data list in place. Returns the list of removed entries.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        list: List of removed employee records
    """
    pass

def standardize_departments(data):
    """
    Convert all Department names (index 1) to lowercase.
    
    Modifies the data list in place. Returns nothing.
    
    Args:
        data (list): 2D list of employee records
    """
    pass


def remove_invalid_performance_ratings(data):
    """
    Remove records with Performance_Rating (index 6) outside range [0, 5].
    
    Modifies the data list in place. Returns the list of removed entries.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        list: List of removed employee records
    """
    pass


def fix_format_dates(data):
    """
    Fix the formatting of hire dates that are not in YYYY-MM-DD format.
    
    Some dates may be in DD/MM/YYYY format; convert these to YYYY-MM-DD.
    Expected format: YYYY-MM-DD
    
    Modifies the data list in place. Returns nothing.
    
    Args:
        data (list): 2D list of employee records
    """
    pass


def remove_invalid_dates(data):
    """
    Remove records with invalid hire dates.
    
    Removes entries where:
    - The year is before 2015 (company was founded in 2015)
    - The year is after 2025 (future dates beyond company scope)
    - The date is logically invalid:
      - Days less than 1 or greater than 30
      - For February: check leap year (29 days in leap years, 28 otherwise)
      - Months less than 1 or greater than 12
    
    Modifies the data list in place. Returns the list of removed entries.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        list: List of removed employee records
    """
    pass


if __name__ == "__main__":
    # Load uncleaned data from CSV file
    data = read_hr_data('uncleaned_dataset.csv')
    print(f"Loaded {len(data)} employee records\n")
    
    print("=" * 70)
    print("DATA CLEANING")
    print("=" * 70)
    
    # Test data cleaning functions
    # Uncomment the lines below to test each cleaning function
    # You can modify the function arguments to test different inputs
    
    # 1. Remove null salaries
    # removed_salaries = remove_null_salaries(data)
    # print(f"Removed {len(removed_salaries)} records with null salaries")
    # print(f"Remaining records: {len(data)}\n")
    
    # 2. Standardize departments
    # standardize_departments(data)
    # print("Standardized department names to lowercase\n")
    
    # 3. Remove invalid performance ratings
    # removed_ratings = remove_invalid_performance_ratings(data)
    # print(f"Removed {len(removed_ratings)} records with invalid performance ratings")
    # print(f"Remaining records: {len(data)}\n")
    
    # 4. Fix hire date formatting
    # fix_format_dates(data)
    # print("Fixed hire date formatting\n")
    
    # 5. Remove invalid dates
    # removed_dates = remove_invalid_dates(data)
    # print(f"Removed {len(removed_dates)} records with invalid dates")
    # print(f"Remaining records: {len(data)}\n")
