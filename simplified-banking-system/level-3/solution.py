from banking_system import BankingSystem
MILLISECONDS_IN_1_DAY = 24 * 60 * 60 * 1000

class BankingSystemImpl(BankingSystem):
    def __init__(self):
        self.accounts = {}
        self.transfers = {}
        self.transfer_counter = 0

    def _expire_transfers(self, ts):
        for tr in self.transfers.values():
            if not tr["accepted"] and not tr["expired"]:
                if ts >= tr["start_time"] + MILLISECONDS_IN_1_DAY + 1:
                    tr["expired"] = True
                    src = self.accounts.get(tr["source"])
                    if src:
                        src["balance"] += tr["amount"]

    def create_account(self, ts, acc_id):
        if acc_id in self.accounts:
            return False
        self.accounts[acc_id] = {"balance": 0, "activity": 0}
        return True

    def deposit(self, ts, acc_id, amt):
        if acc_id not in self.accounts:
            return None
        self._expire_transfers(ts)
        acc = self.accounts[acc_id]
        acc["balance"] += amt
        acc["activity"] += amt
        return acc["balance"]

    def pay(self, ts, acc_id, amt):
        if acc_id not in self.accounts:
            return None
        self._expire_transfers(ts)
        acc = self.accounts[acc_id]
        if acc["balance"] < amt:
            return None
        acc["balance"] -= amt
        acc["activity"] += amt
        return acc["balance"]

    def top_activity(self, ts, n):
        self._expire_transfers(ts)
        sorted_accs = sorted(self.accounts.items(), key=lambda kv: (-kv[1]["activity"], kv[0]))
        return [f"{a}({v['activity']})" for a, v in sorted_accs[:n]]

    def transfer(self, ts, s, t, amt):
        if s == t or s not in self.accounts or t not in self.accounts:
            return None
        self._expire_transfers(ts)
        src = self.accounts[s]
        if src["balance"] < amt:
            return None
        src["balance"] -= amt
        self.transfer_counter += 1
        tid = f"transfer{self.transfer_counter}"
        self.transfers[tid] = {
            "source": s,
            "target": t,
            "amount": amt,
            "start_time": ts,
            "accepted": False,
            "expired": False,
        }
        return tid

    def accept_transfer(self, ts, acc_id, tid):
        self._expire_transfers(ts)
        tr = self.transfers.get(tid)
        if not tr or tr["accepted"] or tr["expired"]:
            return False
        if tr["target"] != acc_id:
            return False
        tr["accepted"] = True
        src = self.accounts[tr["source"]]
        tgt = self.accounts[tr["target"]]
        amt = tr["amount"]
        tgt["balance"] += amt
        src["activity"] += amt
        tgt["activity"] += amt
        return True
