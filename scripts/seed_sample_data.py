from app.db.fake_db import POLICIES, CUSTOMER_HISTORY, VENDOR_HISTORY

def main() -> None:
    print("Loaded sample in-memory datasets:")
    print(f"Policies: {len(POLICIES)}")
    print(f"Customers: {len(CUSTOMER_HISTORY)}")
    print(f"Vendors: {len(VENDOR_HISTORY)}")

if __name__ == "__main__":
    main()
