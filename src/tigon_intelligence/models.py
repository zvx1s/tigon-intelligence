from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

from pydantic import BaseModel

class Company(BaseModel):
    id: str
    name: str
    domain: str
    industry: str
    location: str
    employee_estimate: int | None = None

class Evidence(BaseModel):
    id: str
    company_id: str
    source: str
    source_url: str
    evidence_type: str
    observed_value: str
    observed_text: str | None = None
    observed_at: datetime | None = None

class Signal(str, Enum):
    SIZE_FIT = "SIZE_FIT"
    OWNER_ACCESSIBILITY: "OWNER_ACCESSIBILITY"
    SPANISH_RELEVANCE: "SPANISH_RELEVANCE"
    INTERNAL_IT_PRESENCE: "INTERNAL_IT_PRESENCE"
    MICROSOFT_SIGNAL: "MICROSOFT_SIGNAL"

class Signaltwo(BaseModel):

    type = SIZE_FIT
    value = STRONG
    evidence_ids = HIGH


class Qualification(BaseModel, Enum):
    High = "HIGH"
    Medium = "MEDIUM"
    Skip = "SKIP"
    Needs_review = "NEEDS_REVIEW"
