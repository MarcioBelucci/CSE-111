# MB Inventory System

A command-line inventory management system built in Python as the final project for **CSE 111 (Programming with Functions)** at BYU–Pathway Worldwide.

The system manages stock levels for a small set of products, keeps a full audit log of every movement, and is covered by automated tests.

## Features

- **Add stock** — increase the quantity of an existing product
- **View inventory** — list all products with their current quantity
- **Deduct stock** — decrease quantity, with a safeguard against removing more than what's available
- **Reports** — view a chronological log of every add/subtract transaction, with date and time
- **Persistent storage** — inventory and transaction history are saved to CSV files, so data survives between runs

## How it works

The inventory is stored in `inventory.csv` (product code, name, quantity) and loaded into a dictionary at runtime, keyed by product code for fast lookups. Every successful transaction is timestamped and appended to `log.csv`, giving a full audit trail of stock movements.

```
MB Inventory

Please select one of the following options:
1. Add quantity to existing item
2. View the inventory
3. Deduct Inventory
4. Reports
5. Quit
```

## Error handling

The system is built to fail gracefully rather than crash:

- `FileNotFoundError` — missing inventory or log file
- `PermissionError` — file exists but can't be accessed
- `KeyError` — product code not found in inventory
- `ValueError` — invalid (non-numeric) menu input

Each case prints a clear message to the user instead of an unhandled traceback.

## Testing

Core logic is covered by unit tests using `pytest`:

- Adding stock updates quantities correctly
- Subtracting stock succeeds when there's enough quantity
- Subtracting stock is safely rejected when quantity is insufficient
- Reading and writing the inventory CSV preserves data correctly

Run the tests with:

```bash
pytest test_mb_inventory.py -v
```

## Tech stack

- **Python 3** — `csv` and `datetime` from the standard library (no external dependencies)
- **pytest** — automated testing

## Project structure

```
mb_inventory/
├── mb_inventory.py         # main program
├── test_mb_inventory.py    # unit tests
├── inventory.csv           # current stock data
└── log.csv                 # transaction history
```

## Possible next steps

- Add support for creating brand-new products (currently the system only updates existing ones)
- Add input validation for negative quantities
- Move from CLI to a simple GUI or web interface

---

*Built as part of the Software Development program at BYU–Pathway Worldwide.*
