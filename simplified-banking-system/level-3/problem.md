# Level 3 — Transfers and Acceptance

## Overview
Add money transfer functionality with acceptance mechanism and expiration.
This builds on Levels 1 & 2. Complete this level to unlock Level 4.

## New Requirements

Add:
- `transfer(timestamp, src, tgt, amount)`
- `accept_transfer(timestamp, account_id, transfer_id)`

## Behavior

| Method | Description |
|--------|-------------|
| `transfer` | Withdraws from `src`, holds until accepted or expired (24h = 86400000ms). Returns unique ID `"transferX"`. |
| `accept_transfer` | Adds money to target if valid & not expired. Returns `True` or `False`. |
| **Expired transfers** | Funds return to source automatically after 24 hours. |

## Transfer Expiration

A transfer created at time `t` expires at time `t + 86400000` (24 hours in milliseconds).
If not accepted by expiration time, funds are automatically returned to the source account.

## Example

```python
create_account(1, "a1")
create_account(2, "a2")
deposit(2, "a1", 2000)
transfer(3, "a1", "a2", 1000)     # → "transfer1"
accept_transfer(4, "a2", "transfer1")  # → True
```

## Note
All Level 1 and Level 2 methods must still work.
