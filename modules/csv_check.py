from typing import List
from modules.data_extractor import DataExtractor
from modules.entities.constants import DAYS
from modules.util import check_repetitions, build_error_message
from modules.widgets import g_constants as g_const

class CheckCsv:
  def __init__(self, document_name= None):
    self.set_document(document_name)
  
  def set_document(self, document_name):
    self.document_name = document_name
    self.extractor = DataExtractor(document_name)
  
  def __check_day(self, day: str)-> List:
    errors = []
    warnings = []
    
    morning_employees = self.extractor.get_employeeList(day=day, shift="morning")
    afternoon_employees = self.extractor.get_employeeList(day=day, shift="afternoon")
    errors = [build_error_message(employee_array, day) for employee_array in check_repetitions(morning_employees)]
    errors.extend([build_error_message(employee_array, day) for employee_array in check_repetitions(afternoon_employees)])
    return errors, warnings


  def check_file(self):
    if not self.document_name:
      return [f"<font color={g_const.error_color}>Caricare il documento prima di avviare</font>"], []
    
    errors = []
    warnings = []
    
    for day in DAYS.keys():
      day_errors, day_warnings = self.__check_day(day)
      errors.extend(day_errors)
      warnings.extend(day_warnings)
    
    return errors, warnings
      