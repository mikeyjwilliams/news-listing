# header documentation
from typing import Dict, List



class Human:
    def __init__(self, name, age=24, gender='M', height_in_inches=56, weight_in_pounds=155, eye_count=2, teeth_count=23, hair_style='short', eye_color='blue',
        teeth_color='yellow', hair_color='blonde', skin_tone=3, hair_length=3, energy_percentage=100) -> None:
        self.__name: str = name
        self.__age: int = age
        self.__gender: str = gender
        self.__height: int = height_in_inches
        self.__weight: float = weight_in_pounds
        self.__eye_count: int = eye_count
        self.__teeth_count: int = teeth_count
        self.__hair_style: str = hair_style
        self.__eye_color: str = eye_color
        self.__teeth_color: str = teeth_color
        self.__hair_color: str = hair_color
        self.__skin_tone: int = skin_tone
        self.__hair_length: int = hair_length
        self.__energy_percentage: float = energy_percentage


    def __repr__(self) -> str:
        return f'''Human({self.__name}, {self.__age}, \n
    {self.__gender}, {self.__height}, {self.__weight}, {self.__eye_count}, \n
    {self.__teeth_count}, {self.__hair_style}, {self.__eye_color}, \n
    {self.__teeth_color}, {self.__hair_color}, {self.__skin_tone}, {self.__hair_length}, \n
    {self.__energy_percentage}'''
        
    
    def __str__(self) -> str:
        return f'''name {self.__name}, \n
    {self.__age}, {self.__gender}, {self.__height} {self.__weight}  \n
    {self.__eye_count}, {self.__teeth_count}, {self.__hair_style},  {self.__eye_color}, \n
    {self.__teeth_color}, {self.__hair_color}, {self.__skin_tone}, {self.__hair_length}, \n
    {self.__energy_percentage}'''
        

    # NAME SECTION
    def name_getter(self) -> str:
        return self.__name

    def name_setter(self, name) -> None:
        self.__name = name
        
    
    def get_full_name_dict(self) -> Dict[str, str]:
        """
        Returns a dictionary containing the full name of the Human, 
        with keys 'first_name' and 'last_name'.

        If the Human's name only contains one word, the 'last_name' key will be set to an empty string.

        Parameters:
            self (Human): The Human object for which to retrieve the full name.

        Returns:
            Dict[str, str]: A dictionary containing the full name, with keys 'first_name' and 'last_name'.
        """
        full_name_dict: dict = {}
        full_name_split = self.name_getter().split()
        if len(full_name_split) == 2:
             full_name_dict['last_name'] = self.name_getter().split()[-1]
        full_name_dict['first_name'] = self.name_getter().split()[0]
        


        # full_name_dict['first_name'] = self.name_getter().split()[0]
        # if self. :
        #     full_name_dict['last_name'] = self.name_getter().split()[1] 
        # else:
        #     full_name_dict['last_name'] = ''
        return full_name_dict
    
    # get first name from dict of full name
    def get_first_name(self) -> str:
        return self.full_name()['first_name']
    
    # get last name from dict of full name
    def get_last_name(self) -> str:
        if len(self.full_name()) == 2:
            return self.full_name()['last_name']
        else:
            return ''
        
    
    # Age section
    def age_getter(self):
        return self.__age

    def age_setter(self, age):
        self.__age = age
    
    # Gender section
    def gender_getter(self):
        return self.__gender

    def gender_setter(self, gender):
        self.__gender = gender
    # Height section
    def height_getter(self):
        return self.__height

    def height_setter(self, height):
        self.__height = height
    # Weight section
    def weight_getter(self):
        return self.__weight

    def weight_setter(self, weight):
        self.__weight = weight
    # Eye count section
    def eye_count_getter(self):
        return self.__eye_count

    def eye_count_setter(self, eye_count):
        self.__eye_count = eye_count
    # Teeth count section
    def teeth_count_getter(self):
        return self.__teeth_count

    def teeth_count_setter(self, teeth_count):
        self.__teeth_count = teeth_count
    # hair_style section
    def hair_style_getter(self):
        return self.__hair_style

    def hair_style_setter(self, hair_style):
        self.__hair_style = hair_style
    # Eye color section
    def eye_color_getter(self):
        return self.__eye_color

    def eye_color_setter(self, eye_color):
        self.__eye_color = eye_color
    # Teeth color section
    def teeth_color_getter(self):
        return self.__teeth_color

    def teeth_color_setter(self, teeth_color):
        self.__teeth_color = teeth_color

    # skin tone section
    def skin_tone_getter(self):
        return self.__skin_tone
    
    def skin_tone_setter(self, skin_tone):
        self.__skin_tone = skin_tone
    # hair length section
    def hair_length_getter(self):
        return self.__hair_length

    def hair_length_setter(self, hair_length):
        self.__hair_length = hair_length
    # Energy percentage section
    def energy_percentage_getter(self):
        return self.__energy_percentage

    def energy_percentage_setter(self, energy_percentage):
        self.__energy_percentage = energy_percentage
    
        

        
        
        

    # def day_pasts(self, age_in_years):
    #     one_day = 0.00279397260273972603 # 1 year = 365 days = 365/1 = one_day
    #     one_hour = one_day / 60
    #     age_in_years = self.__age
    #     if _ < 0:
    #         raise ValueError('Age cannot be negative')
    #     elif _ == 0:
    #         under_one = one_day * age_in_days
    #         return under_one
    #     self.__energy_percentage += 0.1
    #     self.__energy_percentage = round(self.__energy_percentage, 2)
    #     self.__energy_percentage = max(self.__energy_percentage, 0)
    #     self.__energy_percentage = min(self.__energy_percentage, 100)
    
    