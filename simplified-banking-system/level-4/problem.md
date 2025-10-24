# Level 4 — Merging & Historical Balance

## Instructions

Your task is to implement a simplified version of a banking system.
All operations that should be supported are listed below.

Solving this task consists of several levels.
Subsequent levels are opened when the current level is correctly solved.
You always have access to the data for the current and all previous levels.

You are not required to provide the most efficient implementation.
Any code that passes the unit tests is sufficient.

## Requirements

The system should support merging accounts and retrieving historical balances.

## Methods

| Method | Description |
|--------|-------------|
| `merge_accounts(self, timestamp, account_id_1, account_id_2)` | Merges account2 into account1. Returns `True` on success, `False` otherwise. Cancels outgoing transfers from account2, redirects incoming ones to account1, and adds balances and histories. |
| `get_balance(self, timestamp, account_id, time_at)` | Returns balance of the account at a given past timestamp. Returns `None` if the account didn't exist at that time. |

## Example

| Query | Explanation |
|-------|-------------|
| `create_account(1, "account1")` | → True |
| `create_account(2, "account2")` | → True |
| `deposit(3, "account1", 1000)` | → 1000 |
| `deposit(4, "account2", 1000)` | → 1000 |
| `merge_accounts(5, "account1", "account2")` | → True |
| `get_balance(6, "account1", 3)` | → 1000 |
| `get_balance(7, "account2", 6)` | → None |

## Notes
- All timestamps are unique and strictly increasing.
- You may assume queries are processed in order.
- You have access to data from all previous levels.
- You do not need the most optimized implementation — only correctness matters.
- All methods from Levels 1, 2, and 3 must still work.
