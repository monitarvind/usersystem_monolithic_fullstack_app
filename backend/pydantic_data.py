from datetime import date
from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field, field_validator, model_validator
from typing import Optional, List, Annotated


class User_system (BaseModel):
    #name: str = Field(..., max_length=50)
    id: Annotated[str, Field(..., description='ID of the user', example='001 or 004')]
    name: Annotated[str, Field(..., max_length=50, description='Enter First and Last name of user', examples=['John Smith', 'Amit Kumar'])]
    email: EmailStr
    married: Optional[bool] = False
    weight: Annotated[float, Field(..., gt=0, lt=100, example='in kgs')]
    #allergy: List[str] = None
    allergy: Annotated[Optional[List[str]], Field(default=None, title='mention your allergies if there is any')]
    phone: Annotated[str, Field(..., description='Dont add country code in the beginning', min_length=10, max_length=10)]
    dob: date
    linkedin_url: Optional[AnyUrl] = None
    emergency_contact: Optional[int] = None
    #contact_details = Dict[str:str]

    #Field Validator for Email to allow certain email IDs only
    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, value):
        valid_domains = ['gmail.com', 'hdfc.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid email ID')
        return value

    #Field Validator for Name to convert the first char to CAPS only
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.capitalize()

    # #Field Validator for Phone to convert int to string
    # @field_validator('phone', mode='before')
    # @classmethod
    # def convert_phone(cls, value):
    #     return str(value)

    #Model Validator to mandate the emergency contact for users more than 60 years
    @model_validator(mode='after')
    def validate_emg_contact(self):
                
        if self.calculated_age > 60 and self.emergency_contact is None:
            raise ValueError('Emergency contact is mandatory for age greater than 60')
        return self
    #Computed Field to calculate the age by using available info from the class or model
    @computed_field()
    @property
    def calculated_age(self) -> int:
        today = date.today()
        age = (today - self.dob).days // 365
        return age


# data_obj = User_system()