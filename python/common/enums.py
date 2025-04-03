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
    OTHER = EnumDetails("OTHER", "Other")

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
    
    E03 = ErrorCodeDetails("E03", "Error putting event to queue", ErrorCategory.SYSTEM, ErrorSeverity.HIGH, 
                           "Contact DF application support for further investigation", False)
    E04 = ErrorCodeDetails("E04", "Form handler: Unknown Event Type", ErrorCategory.DATA, ErrorSeverity.CRITICAL, 
                           "Contact DF application support for further investigation", False)
    E05 = ErrorCodeDetails("E05", "Form handler: Retry count exceed maximum retires", ErrorCategory.DATA, ErrorSeverity.CRITICAL, 
                           "Contact DF application support for further investigation", False)
    E06 = ErrorCodeDetails("E06", "Form handler: Event On Hold", ErrorCategory.DATA, ErrorSeverity.CRITICAL, 
                           "Contact DF application support for further investigation", False)
    E07 = ErrorCodeDetails("E07", "Form handlerr: Event process error", ErrorCategory.DATA, ErrorSeverity.CRITICAL, 
                           "Contact DF application support for further investigation", False)
    E08 = ErrorCodeDetails("E08", "General Event process error", ErrorCategory.SYSTEM, ErrorSeverity.CRITICAL, 
                           "Contact DF application support for further investigation", False)
    E09 = ErrorCodeDetails("E09", "Application ID already exists", ErrorCategory.DATA, ErrorSeverity.LOW, 
                           "Contact DF application support for further investigation", False)
    
    # Forms related error
    
    F01 = ErrorCodeDetails("F01", "Form id lease error", ErrorCategory.DATA, ErrorSeverity.HIGH, 
                           "Contact DF application support for further investigation", False)
    F02 = ErrorCodeDetails("F02", "Renew form id lease error", ErrorCategory.DATA, ErrorSeverity.HIGH, 
                           "Contact DF application support for further investigation", False)
    F03 = ErrorCodeDetails("F02", "Admin form create error", ErrorCategory.DATA, ErrorSeverity.HIGH, 
                           "Contact DF application support for further investigation", False)
    
    # Ride actions related error
    
    R01 = ErrorCodeDetails("R01", "Error in sending  event to RIDE", ErrorCategory.CONNECTION, ErrorSeverity.HIGH, 
                           "Contact DF application support for further investigation", False)
    
    # ICBC actions related error
    
    I01 = ErrorCodeDetails("I01", "Error in sending  event to ICBC", ErrorCategory.CONNECTION, ErrorSeverity.HIGH, 
                           "Contact DF application support for further investigation", False)
    I02 = ErrorCodeDetails("I02", "Error in preparing payload to ICBC", ErrorCategory.DATA, ErrorSeverity.HIGH, 
                           "Contact DF application support for further investigation", False)
    

    # Geocoding location related error

    L01 = ErrorCodeDetails("L01", "Error in getting coordinates", ErrorCategory.CONNECTION, ErrorSeverity.MEDIUM,
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
