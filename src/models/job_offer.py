from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime


class JobOffer (BaseModel) :
    title : str = Field(description= "Post name")
    company : str = Field(description= "Company name")
    contract_type: str = Field( description= "Here is the contract type eg : internship, part-time, full-time...")
    location: str = Field (description= "Location of the job offer ")
    salary : Optional[str] = Field (default=None, description="Annual/monthly salary or salary range")
    required_skills : list[str] = Field (description= "Required skills for the job offer")
    nice_to_have : Optional[list[str]] = Field (default=None, description="Nice to have skills")
    posted_date: Optional[datetime] = Field(default=None, description="Date when the job offer was posted")
    description_summary : str = Field (description= "A summary description of the job offer")
    source_url : Optional[HttpUrl] = Field(default=None, description="URL link to the job offer")
