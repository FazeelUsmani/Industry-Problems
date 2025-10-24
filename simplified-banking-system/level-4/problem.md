# Level 4 — Merging & Historical Balance

## Overview
Add account merging and historical balance query functionality.
This is the final level, building on all previous levels.

## New Requirements

Add:
- `merge_accounts(timestamp, acc1, acc2)`
- `get_balance(timestamp, acc_id, time_at)`

## Behavior

| Method | Description |
|--------|-------------|
| `merge_accounts` | Merge `acc2` into `acc1`. Cancels outgoing transfers, redirects incoming transfers, adds balances, removes `acc2`. |
| `get_balance` | Returns balance of account at historical time `time_at`. Returns `None` if not yet created or after merge. |

## Merge Details

When merging `acc2` into `acc1`:
1. Cancel all outgoing transfers from `acc2` or between `acc1` and `acc2`
2. Redirect incoming transfers to `acc2` to go to `acc1` instead
3. Add `acc2`'s balance to `acc1`
4. Add `acc2`'s activity to `acc1`
5. Remove `acc2` from the system

## Historical Balance

`get_balance(timestamp, acc_id, time_at)` returns:
- The balance of `acc_id` at time `time_at`
- `None` if the account didn't exist at `time_at`
- `None` if querying `acc2` after it was merged

## Example

```python
create_account(1, "a1")
create_account(2, "a2")
deposit(2, "a1", 1000)
deposit(3, "a2", 500)
merge_accounts(4, "a1", "a2")
get_balance(5, "a1", 3)  # → 1000
get_balance(6, "a2", 3)  # → 500
get_balance(7, "a2", 6)  # → None (a2 was merged at time 4)
```

## Note
All methods from Levels 1, 2, and 3 must still work.
