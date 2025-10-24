# Industry Problems

A collection of incremental coding challenges designed to build complex systems step-by-step. Each problem consists of 4 levels that progressively add functionality, allowing you to master system design through hands-on practice.

## 📚 Problem Structure

Each problem follows a consistent structure:

```
problem-name/
├── level-1/
│   ├── problem.md    # Problem statement, requirements, and examples
│   └── solution.py   # Complete solution code
├── level-2/
│   ├── problem.md
│   └── solution.py
├── level-3/
│   ├── problem.md
│   └── solution.py
└── level-4/
    ├── problem.md
    └── solution.py
```

### How It Works

- **Sequential Unlocking**: Each level must be completed before moving to the next
- **Incremental Complexity**: New features build upon previous levels
- **Backward Compatibility**: Solutions must maintain all functionality from earlier levels
- **Real-World Scenarios**: Problems mirror actual industry challenges

## 🎯 Available Problems

### 1. In-Memory Database
**Difficulty**: Medium | **Topics**: Data structures, TTL management, Backup/Restore

Build a simplified in-memory database with field-level operations and time-based features.

- **Level 1**: Basic Operations (set, get, delete)
- **Level 2**: Filtering and Display (scan, prefix matching)
- **Level 3**: TTL (Time-To-Live) with timestamp-aware operations
- **Level 4**: Backup and Restore with TTL recalculation

**Key Concepts**: Hash maps, time-based expiration, state snapshots

---

### 2. Simplified Banking System
**Difficulty**: Medium-Hard | **Topics**: Transaction management, State tracking, Event handling

Implement a banking system with accounts, transfers, and historical data tracking.

- **Level 1**: Basic Operations (create account, deposit, pay)
- **Level 2**: Ranking Accounts by Activity (transaction value tracking)
- **Level 3**: Transfers and Acceptance (scheduled transfers with expiration)
- **Level 4**: Merging & Historical Balance (account consolidation, time-travel queries)

**Key Concepts**: Account management, deferred operations, historical state queries

---

### 3. Cloud Storage System
**Difficulty**: Medium-Hard | **Topics**: User quotas, File operations, Compression

Create a cloud storage system with user management, capacity limits, and file compression.

- **Level 1**: Basic File Operations (add, copy, get file size)
- **Level 2**: File Search (prefix/suffix matching, sorting)
- **Level 3**: User Management (capacity limits, quota enforcement)
- **Level 4**: File Compression (size reduction, capacity recalculation)

**Key Concepts**: Quota management, file systems, compression algorithms

---

## 🚀 Getting Started

1. **Choose a Problem**: Pick one that interests you or matches your learning goals
2. **Start with Level 1**: Read `level-1/problem.md` for requirements
3. **Implement Your Solution**: Try solving it yourself before checking the solution
4. **Compare Solutions**: Review `solution.py` to learn different approaches
5. **Progress to Next Level**: Build upon your previous solution

## 💡 Tips for Success

- **Understand Requirements**: Read problem statements carefully
- **Plan Your Design**: Consider how future levels might extend your solution
- **Test Thoroughly**: Make sure all edge cases are covered
- **Refactor**: Clean up your code before moving to the next level
- **Learn from Solutions**: Study the provided solutions for best practices

## 📝 Problem Philosophy

These problems are designed to:
- Simulate real-world system design challenges
- Teach incremental development practices
- Build intuition for handling complexity
- Demonstrate how requirements evolve over time

## 🎓 Learning Path

**Recommended Order for Beginners:**
1. In-Memory Database (foundation in data structures)
2. Cloud Storage System (quota and state management)
3. Simplified Banking System (complex state transitions)

**For Experienced Developers:**
- Tackle any problem in any order
- Try solving without looking at solutions first
- Focus on edge cases and optimization

## 📖 Additional Resources

- Each `problem.md` includes detailed examples
- Solutions demonstrate clean, working implementations
- All timestamps are strictly increasing (no time-travel paradoxes!)
- No optimization required—correctness is key

## 🤝 Contributing

Feel free to:
- Add new test cases
- Suggest improvements to problem statements
- Contribute new problems following the same structure

---

**Note**: These problems emphasize correctness over optimization. Any solution that passes the requirements is valid, even if it's not the most efficient approach.
