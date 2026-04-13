import math
from datetime import datetime
from helper import read_hr_data
from collections import Counter
import statistics as st

data = read_hr_data('cleaned_dataset.csv')


def get_unique_departments(data):
    """
    Return a set of all unique department names in the dataset.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        set: Set of department names
        
    Example:
        >>> get_unique_departments(data)
        {'engineering', 'sales', 'hr', 'marketing', 'product'}
    """
    departments = set() #to solve this question we use a set because it only takes in unique keys, this allows us to only have a set with unique departments
    
    #in each row the department is in the second column so we use a list to iterate through each row and add the value at index 1 of each row to the set
    for row in data: 
        departments.add(row[1])


    return departments


############################################################################################33
######################################################################################################3



def get_gender_distribution(data):
    """
    Return gender distribution (as percentages) for each department.
    
    All percentages should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        dict: Dictionary where each key is a department name and each value is a dictionary
              of gender percentages
        
    Example:
        >>> get_gender_distribution(data)
        {
            'engineering': {'Male': 45.5, 'Female': 35.2, 'Non-binary': 19.3},
            'sales': {'Male': 40.0, 'Female': 50.0, 'Non-binary': 10.0},
            ...
        }
    """
    #first step is to get the unique departments
    list_of_departments = list(get_unique_departments(data))
    
    #to solve this problem we use dictionary and list comprehension
    #we first create a dictionary that will have department as key and a list with all the genders in that deparment
    #this will allow us to count each gender in the department
    #we then use dictionary comprehension to create the final dictionary with department as key and the gender distribution in the department as values
    department_dictionary = {department: [row[2] for row in data if row[1] == department]
                             
                             
                             for department in list_of_departments

    }

    department_distribution = {departments: 
                               
                               {gender: round((count/len(gender_list))*100, 2) for gender, count in Counter(gender_list).items()

    } 
                               for departments, gender_list in department_dictionary.items()}

    return department_distribution
    
get_gender_distribution(data)           


def get_avg_age_by_department(data):
    """
    Return average age for each department.
    
    All averages should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        dict: Dictionary where each key is a department name and each value is the average age
        
    Example:
        >>> get_avg_age_by_department(data)
        {'engineering': 38.5, 'sales': 35.2, 'hr': 42.1, 'marketing': 33.8, 'product': 36.9}
    """
    #This problem is similar to the previous function we will follow the same steps
    
    #we first create a list with the unique department
    departments = list(get_unique_departments(data))

    #instead of using loops we will use dictionary and list comprehensions
    average_age = {department: round(st.mean([row[3] for row in data if row[1] == department]),2) for department in departments}
    
    
    return average_age



#########################################################################################################
##########################################################################################################
    


def get_retention_rate(data):
    """
    Calculate overall retention rate as a percentage.
    
    Formula: (Active Employees / Total Employees) × 100
    
    Status column (index 8) contains 'Active' or 'Resigned'
    
    Result should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        float: Retention rate as a percentage (0-100)
        
    Example:
        >>> get_retention_rate(data)
        87.5
    """
    

    #to solve this problem we again opt for list comprehensions 
    active_employees_count = len([row[8] for row in data if row[8] == 'Active']) # create a list with all the active employees and count the number of active employees using len()
    
    retention_rate = round(((active_employees_count / len(data)) * 100), 2) # use the retention formular to calculate the retention rate
    
    return retention_rate


def get_turnover_rate_by_department(data):
    """
    Calculate turnover rate for each department as a percentage.
    
    Formula (per department): (Resigned Employees in Department / Total Employees in Department) × 100
    
    All rates should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        dict: Dictionary where each key is a department name and each value is the turnover rate
        
    Example:
        >>> get_turnover_rate_by_department(data)
        {'engineering': 15.5, 'sales': 22.3, 'hr': 10.0, 'marketing': 18.5, 'product': 12.0}
    """
    pass


def get_avg_salary_by_age_range(data, min_age, max_age):
    """
    Return average salary for employees within an age range (inclusive).
    
    Result should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        min_age (int): Minimum age (inclusive)
        max_age (int): Maximum age (inclusive)
        
    Returns:
        float: Average salary for employees in the age range
        
    Example:
        >>> get_avg_salary_by_age_range(data, 25, 35)
        68500.75
    """
    pass

def get_avg_dept_performance_by_training_range(data, min_hours, max_hours):
    """
    Return average performance rating for each department within a training hours range (inclusive).
    
    Calculates the average performance rating for employees within the specified training hours range,
    grouped by department.
    
    All ratings should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        min_hours (int): Minimum training hours (inclusive)
        max_hours (int): Maximum training hours (inclusive)
        
    Returns:
        dict: Dictionary where each key is a department name and each value is the average performance rating
              for employees in that department within the training hours range
        
    Example:
        >>> get_avg_dept_performance_by_training_range(data, 20, 40)
        {
            'engineering': 4.2,
            'sales': 3.9,
            'hr': 4.0,
            'marketing': 3.6,
            'product': 4.3
        }
    """
    pass


if __name__ == "__main__":
    # Load cleaned data from CSV file
    data = read_hr_data('cleaned_dataset.csv')
    print(f"Loaded {len(data)} employee records\n")
    
    print("=" * 70)
    print("METRICS CALCULATION")
    print("=" * 70)
    
    # Test metrics functions
    # Uncomment the lines below to test each metrics function
    # You can modify the function arguments to test different inputs
    
    # 1. Get unique departments
    # depts = get_unique_departments(data)
    # print(f"\nUnique departments: {depts}")
    
    # 2. Get gender distribution per department
    # gender_dist = get_gender_distribution(data)
    # print(f"\nGender distribution by department:")
    # for dept, dist in gender_dist.items():
    #     print(f"  {dept}: {dist}")
    
    # 3. Get average age per department
    # avg_age = get_avg_age_by_department(data)
    # print(f"\nAverage age by department:")
    # for dept, age in avg_age.items():
    #     print(f"  {dept}: {age}")
    
    # 4. Get retention rate
    # retention = get_retention_rate(data)
    # print(f"\nOverall retention rate: {retention}%")
    
    # 5. Get turnover rate per department
    # turnover = get_turnover_rate_by_department(data)
    # print(f"\nTurnover rate by department:")
    # for dept, rate in turnover.items():
    #     print(f"  {dept}: {rate}%")
    
    # 6. Get average salary for age range
    # avg_sal_age = get_avg_salary_by_age_range(data, 25, 35)
    # print(f"\nAverage salary for employees aged 25-35: ${avg_sal_age}")
    
    # 7. Get average department performance by training hours range
    # avg_perf_training = get_avg_dept_performance_by_training_range(data, 20, 40)
    # print(f"\nAverage performance rating by department for employees with 20-40 training hours:")
    # for dept, rating in avg_perf_training.items():
    #     print(f"  {dept}: {rating}")
