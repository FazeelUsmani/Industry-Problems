# Level 1 — Basic Operations

## Instructions

Your task is to implement a simplified version of a banking system.
All operations that should be supported are listed below.

Solving this task consists of several levels.
Subsequent levels are opened when the current level is correctly solved.
You always have access to the data for the current and all previous levels.

You are not required to provide the most efficient implementation.
Any code that passes the unit tests is sufficient.

## Requirements

The banking system should support creating new accounts and depositing or paying money.

## Methods

| Method | Description |
|--------|-------------|
| `create_account(self, timestamp, account_id)` | Creates a new account with the given ID. Returns `True` if successful or `False` if the account already exists. |
| `deposit(self, timestamp, account_id, amount)` | Deposits the given amount. Returns new balance or `None` if account doesn't exist. |
| `pay(self, timestamp, account_id, amount)` | Withdraws money. Returns balance or `None` if insufficient funds or account doesn't exist. |

## Example

| Query | Explanation |
|-------|-------------|
| `create_account(1, "account1")` | → True |
| `create_account(2, "account1")` | → False |
| `deposit(3, "account1", 2000)` | → 2000 |
| `pay(4, "account1", 500)` | → 1500 |

## Notes
- All timestamps are unique and strictly increasing.
- You may assume queries are processed in order.
- You have access to data from all previous levels.
- You do not need the most optimized implementation — only correctness matters.
