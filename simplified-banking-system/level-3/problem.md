# Level 3 — Transfers and Acceptance

## Instructions

Your task is to implement a simplified version of a banking system.
All operations that should be supported are listed below.

Solving this task consists of several levels.
Subsequent levels are opened when the current level is correctly solved.
You always have access to the data for the current and all previous levels.

You are not required to provide the most efficient implementation.
Any code that passes the unit tests is sufficient.

## Requirements

The banking system should support scheduling transfers and checking transfer status.

## Methods

| Method | Description |
|--------|-------------|
| `transfer(self, timestamp, source, target, amount)` | Initiates a transfer from source to target. Returns `"transferX"` if successful, otherwise `None`. |
| `accept_transfer(self, timestamp, account_id, transfer_id)` | Accepts the transfer. Returns `True` if successful, `False` otherwise. |

**Transfer Rules:**
- Transfers expire after 24 hours (86400000 ms).
- If expired, the held funds are returned to the source.

## Example

| Query | Explanation |
|-------|-------------|
| `create_account(1, "account1")` | → True |
| `create_account(2, "account2")` | → True |
| `deposit(3, "account1", 2000)` | → 2000 |
| `transfer(4, "account1", "account2", 1000)` | → "transfer1" |
| `accept_transfer(5, "account2", "transfer1")` | → True |

## Notes
- All timestamps are unique and strictly increasing.
- You may assume queries are processed in order.
- You have access to data from all previous levels.
- You do not need the most optimized implementation — only correctness matters.
- All Level 1 and Level 2 methods must still work.
