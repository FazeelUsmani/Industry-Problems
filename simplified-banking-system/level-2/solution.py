from banking_system import BankingSystem

class BankingSystemImpl(BankingSystem):
    def __init__(self):
        self.accounts = {}  # {id: {"balance": int, "activity": int}}

    def create_account(self, timestamp, account_id):
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = {"balance": 0, "activity": 0}
        return True

    def deposit(self, timestamp, account_id, amount):
        acc = self.accounts.get(account_id)
        if not acc:
            return None
        acc["balance"] += amount
        acc["activity"] += amount
        return acc["balance"]

    def pay(self, timestamp, account_id, amount):
        acc = self.accounts.get(account_id)
        if not acc or acc["balance"] < amount:
            return None
        acc["balance"] -= amount
        acc["activity"] += amount
        return acc["balance"]

    def top_activity(self, timestamp, n):
        ranked = sorted(
            self.accounts.items(),
            key=lambda x: (-x[1]["activity"], x[0])
        )
        return [f"{aid}({data['activity']})" for aid, data in ranked[:n]]
