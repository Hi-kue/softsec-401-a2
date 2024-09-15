from dataclasses import dataclass
from typing import List, Optional


@dataclass
class User:
    id: int
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_active: int
    is_superuser: int

    def validate_booleans(self):
        if self.is_active and self.is_superuser not in [0, 1]:
            raise ValueError("is_active and is_superuser must be 0 or 1.")


@dataclass
class BankAccount:
    id: int
    user_id: int
    balance: float
    currency_type: str
    withdraw_limit: float
    is_active: int

    def validate_boolean(self):
        if self.is_active not in [0, 1]:
            raise ValueError("is_active must be 0 or 1.")


@dataclass
class Transaction:
    id: int
    user_id: int
    bank_account_id: int
    amount: float
    transaction_type: str
    description: Optional[str]
    is_approved: int
    timestamp: str

    def validate_boolean(self):
        if self.is_approved not in [0, 1]:
            raise ValueError("is_approved must be 0 or 1.")
