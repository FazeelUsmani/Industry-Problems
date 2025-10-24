# Level 2 — Ranking Accounts by Activity

## Overview
Extend the banking system to rank accounts by their transaction activity.
This builds on Level 1. Complete this level to unlock Level 3.

## New Requirement

Add:
- `top_activity(timestamp, n)`

## Behavior

Returns top `n` accounts by total transaction value (sum of deposits + successful withdrawals).

**Ties:** Sort alphabetically by account ID.

**Format:** `["account_id(value)", "account_id(value)", ...]`

## Example

```python
create_account(1, "account1")
create_account(2, "account2")
deposit(3, "account1", 2000)
deposit(4, "account2", 3000)
pay(5, "account1", 1000)
top_activity(6, 2)
# → ["account2(3000)", "account1(3000)"]
```

## Note
All Level 1 methods (create_account, deposit, pay) must still work.
