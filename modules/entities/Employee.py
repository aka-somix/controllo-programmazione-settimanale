class Employee():
  def __init__(self, name: str, sala: str, shift: str, job: str):
    self.name = name
    self.sala = sala
    self.shift = shift
    self.job = job
  
  def __eq__(self, o: object) -> bool:
      return self.name == str(o)
  
  def __str__(self) -> str:
      return self.name
