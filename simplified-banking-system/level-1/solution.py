from banking_system import BankingSystem

class BankingSystemImpl(BankingSystem):
    def __init__(self):
        self.accounts = {}  # account_id → balance

    def create_account(self, timestamp: int, account_id: str) -> bool:
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        return True

    def deposit(self, timestamp: int, account_id: str, amount: int) -> int | None:
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        return self.accounts[account_id]

    def pay(self, timestamp: int, account_id: str, amount: int) -> int | None:
        if account_id not in self.accounts:
            return None
        if self.accounts[account_id] < amount:
            return None
        self.accounts[account_id] -= amount
        return self.accounts[account_id]
