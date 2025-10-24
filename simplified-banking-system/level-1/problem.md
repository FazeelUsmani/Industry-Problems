# Level 1 — Basic Operations

## Overview
Implement a banking system class that supports basic account operations.
This is Level 1 of 4. Complete this level to unlock Level 2.

## Requirements

Implement the following methods:
- `create_account(timestamp, account_id)`
- `deposit(timestamp, account_id, amount)`
- `pay(timestamp, account_id, amount)`

## Behavior

| Method | Description |
|--------|-------------|
| `create_account` | Creates a new account if it doesn't exist. Returns `True` on success, `False` if already exists. |
| `deposit` | Adds money to account. Returns new balance or `None` if account doesn't exist. |
| `pay` | Withdraws money. Returns new balance, or `None` if insufficient funds or account doesn't exist. |

## Example

```python
create_account(1, "account1")  # → True
create_account(2, "account1")  # → False
create_account(3, "account2")  # → True
deposit(4, "account1", 2700)   # → 2700
pay(5, "account1", 200)        # → 2500
```
