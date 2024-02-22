# header documentation
from typing import Dict, List

class Human:
    def __init__(self, name='John', age=24, gender='M', height_in_inches=56, weight_in_pounds=155, eye_count=2, teeth_count=23, hair_style='short', eye_color='blue',
        teeth_color='yellow', hair_color='blonde', skin_tone=3, hair_length=3, energy_percentage=100) -> None:
        self.name: str = name
        self.age: int = 
        self.gender: str = gender
        self.height: int = height_in_inches
        self.weight: float = weight_in_pounds
        self.eye_count: int = eye_count
        self.teeth_count: int = teeth_count
        self.hair_style: str = hair_style
        self.eye_color: str = eye_color
        self.teeth_color: str = teeth_color
        self.hair_color: str = hair_color
        self.skin_tone: int = skin_tone
        self.hair_length: int = hair_length
        self.energy_percentage: float = energy_percentage


    def __repr__(self) -> str:
        return f'''Human({self.name}, {self.age}, \n
    {self.gender}, {self.height}, {self.weight}, {self.eye_count}, \n
    {self.teeth_count}, {self.hair_style}, {self.eye_color}, \n
    {self.teeth_color}, {self.hair_color}, {self.skin_tone}, {self.hair_length}, \n
    {self.energy_percentage}'''
        
    
    def __str__(self) -> str:
        return f'''name {self.name}, \n
    {self.age}, {self.gender}, {self.height} {self.weight}  \n
    {self.eye_count}, {self.teeth_count}, {self.hair_style},  {self.eye_color}, \n
    {self.teeth_color}, {self.hair_color}, {self.skin_tone}, {self.hair_length}, \n
    {self.energy_percentage}'''
        
        
    def day_pasts(self, age_in_years):
        one_day = 0.00279397260273972603 # 1 year = 365 days = 365/1 = one_day
        one_hour = one_day / 60
        
        age_in_years = self.age
        
        if _ < 0:
            raise ValueError('Age cannot be negative')
        elif _ == 0:
            under_one = one_day * age_in_days
            return under_one
        
        
        self.energy_percentage += 0.1
        self.energy_percentage = round(self.energy_percentage, 2)
        self.energy_percentage = max(self.energy_percentage, 0)
        self.energy_percentage = min(self.energy_percentage, 100)