import re
import string


class User:
    
    def __init__(self, first_name: str, last_name:str, phone_number: str="", address: str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __repr__(self) -> str:
        return f"User({self.first_name}, {self.last_name})"

    def __str__(self) -> str:
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def _check(self):
        self._check_phone_number()
        self._check_names()


    def _check_phone_number(self):
        
        phone_digits = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_digits) < 10 or not phone_digits.isdigit():
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide.")

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError("Le prénom et le nom de famille ne peuvent être vides")

        special_characters = string.digits + string.punctuation
        for character in self.first_name + self.last_name:
            if character in special_characters:
                raise ValueError(f"Nom invalide {self.full_name}.")


if __name__ == "__main__":
    pass
    

    # from faker import Faker

    # fake = Faker(locale="fr_FR")

    
    # user = User(first_name = fake.first_name(),
    #             last_name=fake.last_name(),
    #             phone_number="5468546547",
    #             address=fake.address())

    # user._check_phone_number()

    # print("-" * 10)