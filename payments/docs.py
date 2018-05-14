PAYMENTS_DOCS = """
Account details.

Example GET response:
```
{
    "id": 1,
    "from_account": "bob123",
    "to_account": "alice456",
    "amount": "10.00",
    "from_account_detail": {
        "id": "bob123",
        "owner": "bob",
        "balance": "90.00",
        "currency": "PHP"
    },
    "to_account_detail": {
        "id": "alice456",
        "owner": "alice",
        "balance": "10.01",
        "currency": "PHP"
    }
}
```
"""
