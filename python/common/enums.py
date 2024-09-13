from enum import Enum
from dataclasses import dataclass

@dataclass
class EnumDetails:
    code: str
    description: str

class BaseEnum(Enum):
    def __str__(self):
        return self.value.code

    @property
    def code(self):
        return self.value.code

    @property
    def description(self):
        return self.value.description
    
class EventType(BaseEnum):
    TWELVE_HOUR = EnumDetails("TwelveHour", "12 Hour Prohibition")
    TWENTY_FOUR_HOUR = EnumDetails("TwentyFourHour", "24 Hour Prohibition")
    IRP = EnumDetails("IRP", "Immediate Roadside Prohibition")
    VI = EnumDetails("VI", "Vehicle Impoundment")

class ErrorCategory(BaseEnum):
    VALIDATION = EnumDetails("VALIDATION", "Validation Error")
    SYSTEM = EnumDetails("SYSTEM", "System Error")
    CONNECTION = EnumDetails("CONNECTION", "Connection Error")
    DATA = EnumDetails("DATA", "Data Error")
    OTHER = EnumDetails("OTHER", "Other Error")

class ErrorSeverity(BaseEnum):
    LOW = EnumDetails("LOW", "Low Severity")
    MEDIUM = EnumDetails("MEDIUM", "Medium Severity")
    HIGH = EnumDetails("HIGH", "High Severity")
    CRITICAL = EnumDetails("CRITICAL", "Critical Severity")

class ErrorStatus(BaseEnum):
    NEW = EnumDetails("NEW", "New Error")
    VIEWED = EnumDetails("VIEWED", "Viewed Error")
    IN_PROGRESS = EnumDetails("IN_PROGRESS", "In Progress")
    ASSIGNED = EnumDetails("ASSIGNED", "Assigned")
    RESOLVED = EnumDetails("RESOLVED", "Resolved")
    CANCELLED = EnumDetails("CANCELLED", "Cancelled")
    CLOSED = EnumDetails("CLOSED", "Closed")

@dataclass
class ErrorCodeDetails:
    code: str
    description: str # max 200 characters
    category: ErrorCategory
    severity: ErrorSeverity
    resolution: str
    is_business_error: bool

class ErrorCode(BaseEnum):
    # General error
    G00 = ErrorCodeDetails("G00", "General error", ErrorCategory.OTHER, ErrorSeverity.LOW, 
                           "Contact DF application support for further investigation", False)
    
    # Events related error
    
    E01 = ErrorCodeDetails("E01", "Event saving error", ErrorCategory.DATA, ErrorSeverity.HIGH, 
                           "Contact DF application support for further investigation", False)
    E02 = ErrorCodeDetails("E02", "Event PDF saving error", ErrorCategory.DATA, ErrorSeverity.HIGH, 
                           "Contact DF application support for further investigation", False)
    
    # Add more error codes as needed...

    @property
    def category(self):
        return self.value.category

    @property
    def severity(self):
        return self.value.severity

    @property
    def resolution(self):
        return self.value.resolution

    @property
    def is_business_error(self):
        return self.value.is_business_error
