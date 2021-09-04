from typing import List
from modules.widgets import g_constants as g_const
from modules.entities.constants import DAYS


def editDistance(str1, str2, m, n):
 
    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n
 
    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m
 
    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
 
    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert
                   editDistance(str1, str2, m-1, n),    # Remove
                   editDistance(str1, str2, m-1, n-1)    # Replace
                   )


def check_repetitions(array) -> List:
    rep_map = {}
    for elem in array:
        key = elem.__str__() 
        if key in rep_map.keys():
            rep_map[key].append(elem)
        else:
            rep_map[key] = [elem]
    return list(filter(lambda array: len(array)> 1, rep_map.values()))

def build_error_message(employee_array, day) -> str: 
    message = f"<font color={g_const.error_color}>"
    message += f"📅 {DAYS[day].upper()} - è stato assegnato <b>{employee_array[0].name.capitalize()}</b> contemporaneamente a: <br>"
    for employee in employee_array:
        message += f"❌ {employee.sala} come <u>{employee.job}</u> di <u>{employee.shift}</u> <br>"
    
    message += "</font>"
    return message


def formatString(data: str) -> str:
  return data.lower() if data else None
