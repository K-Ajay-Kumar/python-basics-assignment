# ============================================
# Assignment: Python Functions and Lists
# ============================================

def calculate_total(marks):
    """
    Calculate the total sum of marks in the list.
    
    Parameters:
        marks (list): List of numerical marks
    
    Returns:
        int/float: Sum of all marks
    """
    total = 0
    for mark in marks:
        total += mark
    return total


def calculate_average(marks):
    """
    Calculate the average of marks using calculate_total().
    
    Parameters:
        marks (list): List of numerical marks
    
    Returns:
        float: Average of marks
    """
    total = calculate_total(marks)
    count = 0
    for _ in marks:
        count += 1
    return total / count if count != 0 else 0


def get_grade(average):
    """
    Determine grade based on average marks.
    
    Parameters:
        average (float): Average marks
    
    Returns:
        str: Grade (A, B, or C)
    """
    if average > 90:
        return "A"
    elif average > 75:
        return "B"
    else:
        return "C"


def display_report(marks):
    """
    Display total, average, and grade by calling other functions.
    
    Parameters:
        marks (list): List of numerical marks
    """
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)

    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")


# ============================================
# Test the solution
# ============================================
marks_list = [88, 76, 95, 60, 82]
display_report(marks_list)
