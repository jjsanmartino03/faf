from enum import Enum


class ValidationStatus(Enum):
    PENDING = 'pending'
    FAILED = 'failed'
    PASSED = 'passed'
