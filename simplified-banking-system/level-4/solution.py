from banking_system import BankingSystem
MILLISECONDS_IN_1_DAY = 24 * 60 * 60 * 1000

class BankingSystemImpl(BankingSystem):
    def __init__(self):
        self.accounts = {}
        self.transfers = {}
        self.transfer_counter = 0

    def _record_balance(self, acc_id, ts):
        acc = self.accounts[acc_id]
        acc["history"].append((ts, acc["balance"]))

    def _expire_transfers(self, ts):
        for tr in self.transfers.values():
            if not tr["accepted"] and not tr["expired"]:
                if ts >= tr["start_time"] + MILLISECONDS_IN_1_DAY + 1:
                    tr["expired"] = True
                    src = self.accounts.get(tr["source"])
                    if src:
                        src["balance"] += tr["amount"]
                        self._record_balance(tr["source"], ts)

    # --- Level 1 ---
    def create_account(self, ts, acc_id):
        if acc_id in self.accounts:
            return False
        self.accounts[acc_id] = {"balance": 0, "activity": 0, "history": []}
        self._record_balance(acc_id, ts)
        return True

    def deposit(self, ts, acc_id, amt):
        if acc_id not in self.accounts:
            return None
        self._expire_transfers(ts)
        acc = self.accounts[acc_id]
        acc["balance"] += amt
        acc["activity"] += amt
        self._record_balance(acc_id, ts)
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
        self._record_balance(acc_id, ts)
        return acc["balance"]

    # --- Level 2 ---
    def top_activity(self, ts, n):
        self._expire_transfers(ts)
        active = {k: v for k, v in self.accounts.items() if not k.startswith("_merged_")}
        sorted_accs = sorted(active.items(), key=lambda kv: (-kv[1]["activity"], kv[0]))
        return [f"{a}({v['activity']})" for a, v in sorted_accs[:n]]

    # --- Level 3 ---
    def transfer(self, ts, s, t, amt):
        if s == t or s not in self.accounts or t not in self.accounts:
            return None
        self._expire_transfers(ts)
        src = self.accounts[s]
        if src["balance"] < amt:
            return None
        src["balance"] -= amt
        self._record_balance(s, ts)
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
        self._record_balance(tr["source"], ts)
        self._record_balance(tr["target"], ts)
        return True

    # --- Level 4 ---
    def merge_accounts(self, ts, acc1, acc2):
        if acc1 == acc2 or acc1 not in self.accounts or acc2 not in self.accounts:
            return False
        self._expire_transfers(ts)

        for tr in self.transfers.values():
            if not tr["expired"] and not tr["accepted"]:
                if tr["source"] == acc2 or (tr["source"] == acc1 and tr["target"] == acc2):
                    tr["expired"] = True
                    src = self.accounts.get(tr["source"])
                    if src:
                        src["balance"] += tr["amount"]
                        self._record_balance(tr["source"], ts)
                elif tr["target"] == acc2:
                    tr["target"] = acc1

        acc1_data = self.accounts[acc1]
        acc2_data = self.accounts[acc2]
        acc1_data["balance"] += acc2_data["balance"]
        acc1_data["activity"] += acc2_data["activity"]
        self._record_balance(acc1, ts)

        acc2_data["merged_at"] = ts
        self.accounts[f"_merged_{acc2}"] = acc2_data
        del self.accounts[acc2]
        return True

    def get_balance(self, ts, acc_id, time_at):
        self._expire_transfers(ts)
        acc = self.accounts.get(acc_id) or self.accounts.get(f"_merged_{acc_id}")
        if not acc:
            return None
        if "merged_at" in acc and time_at >= acc["merged_at"]:
            return None
        hist = acc["history"]
        if not hist or time_at < hist[0][0]:
            return None
        res = None
        for t, b in hist:
            if t <= time_at:
                res = b
            else:
                break
        return res if res is not None else 0
