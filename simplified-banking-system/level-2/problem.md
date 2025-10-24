# Level 2 — Ranking Accounts by Activity

## Instructions

Your task is to implement a simplified version of a banking system.
All operations that should be supported are listed below.

Solving this task consists of several levels.
Subsequent levels are opened when the current level is correctly solved.
You always have access to the data for the current and all previous levels.

You are not required to provide the most efficient implementation.
Any code that passes the unit tests is sufficient.

## Requirements

The system should support ranking accounts based on total transaction value.

## Method

**`top_activity(self, timestamp, n)`**

Returns the top `n` accounts with the highest total transaction value (sum of all successful deposits and withdrawals).
- If there are ties, sort alphabetically.
- If fewer than `n` accounts exist, return all.

**Output format:**
```
["<account_id_1>(<transactions_value_1>)", "<account_id_2>(<transactions_value_2>)", ...]
```

## Example

| Query | Explanation |
|-------|-------------|
| `create_account(1, "account1")` | → True |
| `create_account(2, "account2")` | → True |
| `deposit(3, "account1", 2000)` | → 2000 |
| `deposit(4, "account2", 3000)` | → 3000 |
| `top_activity(5, 2)` | → ["account2(3000)", "account1(2000)"] |

## Notes
- All timestamps are unique and strictly increasing.
- You may assume queries are processed in order.
- You have access to data from all previous levels.
- You do not need the most optimized implementation — only correctness matters.
- All Level 1 methods must still work.
