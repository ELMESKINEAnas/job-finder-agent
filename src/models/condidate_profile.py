from pydantic import BaseModel, Field
from typing import Optional



class MyProfile (BaseModel) :
    title : str = Field (description= "Post name")
    required_skills : list[str] = Field(description= "My skills")
    contract_type : str = Field(default="internship", description="Type of contract")
    location : Optional[str] = Field (default=None, description="Prefered Localisation")
    availability : str = Field (default="September",description="Availability for internship")
    experience_level : str = Field(description="4th Year engineer student")
