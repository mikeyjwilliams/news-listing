# header documentation

from typing import Dict, List

def main():
    John = Human(name='John Doe')
    print(John)






class Human:
    def __init__(self, name: str,
                age: int = 18, 
                gender: str = 'M', 
                height_in_inches: int = 64,
                weight_in_pounds: float = 172,
                eye_count: int = 2,
                teeth_count: int = 32,
                hair_style: str = 'long',
                eye_color: str = 'blue-green',
                teeth_color: str = 'semi-white',
                hair_color: str = 'red',
                skin_tone: int = 3,
                hair_length: int = 36,
                energy_percentage: float = 1.0
                ) -> None:
        """
        Initialize a Human object.

        Args:
            name (str): The name of the Human. REQUIRED
            age (int, optional): The age of the Human. Defaults to 18.
            gender (str, optional): The gender of the Human. Defaults to 'M'.
            height_in_inches (int, optional): The height of the Human in inches. Defaults to 64.
            weight_in_pounds (float, optional): The weight of the Human in pounds. Defaults to 172.
            eye_count (int, optional): The number of eyes of the Human. Defaults to 2.
            teeth_count (int, optional): The number of teeth of the Human. Defaults to 32.
            hair_style (str, optional): The hair style of the Human. Defaults to 'long'.
            eye_color (str, optional): The eye color of the Human. Defaults to 'blue-green'.
            teeth_color (str, optional): The teeth color of the Human. Defaults to 'semi-white'.
            hair_color (str, optional): The hair color of the Human. Defaults to 'red'.
            skin_tone (int, optional): The skin tone of the Human. Defaults to 3.
            hair_length (int, optional): The hair length of the Human. Defaults to 36.
            energy_percentage (float, optional): The energy percentage of the Human. Defaults to 1.0.

        Raises:
            ValueError: If the energy percentage is less than 0 or greater than 1.
        """
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

        if energy_percentage < 0 or energy_percentage > 1:
            raise ValueError('Energy percentage must be between 0 and 1.')


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
        return full_name_dict

    def get_first_name(self) -> str:
        """
        Returns the first name of the Human.

        Parameters:
            self (Human): The Human object for which to retrieve the first name.

        Returns:
            str: The first name of the Human.
        """
        return self.get_full_name_dict()['first_name']

    def get_last_name(self) -> str:
        if len(self.get_full_name_dict()) == 2:
            return self.get_full_name_dict()['last_name']
        else:
            return ''


    # Age section
    def age_getter(self) -> int:
        return self.__age

    def age_setter(self, age: int) -> None:
        self.__age = age

    # Gender section
    def gender_getter(self) -> str:
        return self.__gender

    def gender_setter(self, gender: str) -> None:
        self.__gender = gender
    # Height section
    def height_getter(self) -> int:
        return self.__height

    def height_setter(self, height: int) -> None:
        self.__height = height
    # Weight section
    def weight_getter(self) -> float:
        return self.__weight

    def weight_setter(self, weight: float) -> None:
        self.__weight = weight
    # Eye count section
    def eye_count_getter(self) -> int:
        return self.__eye_count

    def eye_count_setter(self, eye_count: int) -> None:
        self.__eye_count = eye_count
    # Teeth count section
    def teeth_count_getter(self) -> int:
        return self.__teeth_count

    def teeth_count_setter(self, teeth_count: int) -> None:
        self.__teeth_count = teeth_count
    # hair_style section
    def hair_style_getter(self) -> str:
        return self.__hair_style

    def hair_style_setter(self, hair_style: str) -> None:
        self.__hair_style = hair_style
    # Eye color section
    def eye_color_getter(self) -> str:
        return self.__eye_color

    def eye_color_setter(self, eye_color: str) -> None:
        self.__eye_color = eye_color
    # Teeth color section
    def teeth_color_getter(self) -> str:
        return self.__teeth_color

    def teeth_color_setter(self, teeth_color: str) -> None:
        self.__teeth_color = teeth_color

    # skin tone section
    def skin_tone_getter(self) -> int:
        return self.__skin_tone

    def skin_tone_setter(self, skin_tone: int) -> None:
        self.__skin_tone = skin_tone
    # hair length section
    def hair_length_getter(self) -> int:
        return self.__hair_length

    def hair_length_setter(self, hair_length: int) -> None:
        self.__hair_length = hair_length
    # Energy percentage section
    def energy_percentage_getter(self) -> float:
        return f'{self.__energy_percentage:.5f}'

    def energy_percentage_setter(self, energy_percentage: float) -> None:
        if energy_percentage < 0:
            raise ValueError('Energy percentage must be between 0 and 1.')
        if energy_percentage > 1:
            self.__energy_percentage = 1
        else:
            self.__energy_percentage = energy_percentage

    # method that reduces the energy percentage by 25%
    def reduce_energy_percentage(self, reduce_amount) -> None:
        self.__energy_percentage -= reduce_amount
        self.__energy_percentage = round(self.__energy_percentage, 2)
        self.__energy_percentage = max(self.__energy_percentage, 0)
        self.__energy_percentage = min(self.__energy_percentage, 100)


    # energy sleep add method that increases the energy percentage by 10%
    def increase_energy_percentage(self, increase_amount) -> None:
        self.__energy_percentage += increase_amount
        self.__energy_percentage = round(self.__energy_percentage, 2)
        self.__energy_percentage = max(self.__energy_percentage, 0)
        self.__energy_percentage = min(self.__energy_percentage, 100)

    def sleep(self) -> None:
        self.__energy_percentage += 0.35
        self.__energy_percentage = round(self.__energy_percentage, 2)
        self.__energy_percentage = max(self.__energy_percentage, 0)
        self.__energy_percentage = min(self.__energy_percentage, 100)






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
