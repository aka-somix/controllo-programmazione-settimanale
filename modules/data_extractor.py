from modules.entities.Employee import Employee
from modules.entities.constants import EN_TO_IT
from typing import List
import openpyxl

# excel column for every role and every day 
DAY_LETTER = {
  'mon': {
    'str': 'B',
    'vol': 'C',
    'edo': 'D'
  },
  'tue': {
    'str': 'E',
    'vol': 'F',
    'edo': 'G'
  },
  'wed': {
    'str': 'H',
    'vol': 'I',
    'edo': 'J'
  },
  'thu': {
    'str': 'K',
    'vol': 'L',
    'edo': 'M'
  },
  'fri': {
    'str': 'N',
    'vol': 'O',
    'edo': 'P'
  },
  'sat': {
    'str': 'Q',
    'vol': 'R',
  },
  'sun': {
    'str': 'S',
    'vol': 'T',
  },
}

# excel row for every shift and sala
SALA_LETTER = {
  'morning': {
    'Sala 1': 4,
    'Sala 2': 5,
    'Sala 3': 6,
    'Sala 4': 7,
    'Sala 5': 8,
    'ENDO': 9,
    'JOLLY': 12
  },
  'afternoon': {
    'Turno 2/12': 13,
    'Turno 2': 14,
    'Picchetto': 15
  },
}

class DataExtractor():
  def __init__(self, document=None):
    if(document):
      wb_obj = openpyxl.load_workbook(document) 
      # Read the active sheet:
      self.sheet = wb_obj.active
    else:
      print("NO file found")
    
  def get_employeeList(self,
                       day="mon",
                       shift="morning") -> List:
    employeeList = []
    for sala in SALA_LETTER[shift].keys():
      # strumentista
      name = self.sheet[f"{DAY_LETTER[day]['str']}{SALA_LETTER[shift][sala]}"].value
      employeeList.append(
        Employee(
          name= self.sheet[f"{DAY_LETTER[day]['str']}{SALA_LETTER[shift][sala]}"].value,
          job="Strumentista",
          shift= EN_TO_IT[shift],
          sala= sala
        )
      )
      # volante
      employeeList.append(
        Employee(
          name= self.sheet[f"{DAY_LETTER[day]['vol']}{SALA_LETTER[shift][sala]}"].value,
          job="Volante",
          shift= EN_TO_IT[shift],
          sala= sala
        )
      )
      if(day not in ('sat', 'sun')):
        # edome...
        employeeList.append(
          Employee(
            name= self.sheet[f"{DAY_LETTER[day]['edo']}{SALA_LETTER[shift][sala]}"].value,
            job="E. Domestiche",
            shift= EN_TO_IT[shift],
            sala= sala
          )
        )
    return list(filter(lambda e: e.name, employeeList))
