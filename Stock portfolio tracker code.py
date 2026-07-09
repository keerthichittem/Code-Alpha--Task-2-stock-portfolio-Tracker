# ============================================================
#  Stock Portfolio Tracker
#  Task 2 - Python Developer Internship
# ============================================================

import csv
import os
from datetime import datetime

# ---------- Hardcoded stock price dictionary ----------
STOCK_PRICES = {
    "AAPL":  182.50,   # Apple Inc.
    "TSLA":  248.75,   # Tesla Inc.
    "GOOGL": 175.30,   # Alphabet Inc.
    "MSFT":  415.60,   # Microsoft Corp.
    "AMZN":  192.45,   # Amazon.com Inc.
    "NVDA":  875.20,   # NVIDIA Corp.
    "META":  520.10,   # Meta Platforms
    "NFLX":  645.80,   # Netflix Inc.
    "RELIANCE": 2950.00,  # Reliance Industries (NSE)
    "TCS":   3780.00,  # Tata Consultancy Services (NSE)
    "INFY":   1580.00, # Infosys Ltd (NSE)
    "WIPRO":   480.00, # Wipro Ltd (NSE)
}

# -------------------------------------------------------
def display_banner():
    print("=" * 55)
    print("       📈  STOCK PORTFOLIO TRACKER  📈")
    print("=" * 55)

def display_available_stocks():
    print("\n📋 Available Stocks & Current Prices:")
    print("-" * 40)
    print(f"  {'Ticker':<10} {'Company / Stock':<25} {'Price (₹/$)':>10}")
    print("-" * 40)
    labels = {
        "AAPL": "Apple Inc.", "TSLA": "Tesla Inc.",
        "GOOGL": "Alphabet Inc.", "MSFT": "Microsoft Corp.",
        "AMZN": "Amazon.com Inc.", "NVDA": "NVIDIA Corp.",
        "META": "Meta Platforms", "NFLX": "Netflix Inc.",
        "RELIANCE": "Reliance Industries", "TCS": "TCS",
        "INFY": "Infosys Ltd", "WIPRO": "Wipro Ltd",
    }
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker:<10} {labels.get(ticker, ticker):<25} {price:>10,.2f}")
    print("-" * 40)

def get_user_portfolio():
    """Prompt user to input stock ticker + quantity pairs."""
    portfolio = {}
    print("\n📥 Enter your stock holdings.")
    print("   Type 'done' when finished.\n")

    while True:
        ticker = input("  Stock ticker (e.g. AAPL) : ").strip().upper()
        if ticker == "DONE":
            break
        if ticker not in STOCK_PRICES:
            print(f"  ⚠️  '{ticker}' not found. Choose from: {', '.join(STOCK_PRICES)}\n")
            continue
        try:
            qty = int(input(f"  Quantity of {ticker}       : ").strip())
            if qty <= 0:
                print("  ⚠️  Quantity must be a positive integer.\n")
                continue
        except ValueError:
            print("  ⚠️  Please enter a valid whole number.\n")
            continue

        if ticker in portfolio:
            portfolio[ticker] += qty
            print(f"  ✅ Updated {ticker}: total {portfolio[ticker]} shares.\n")
        else:
            portfolio[ticker] = qty
            print(f"  ✅ Added {ticker} x{qty}.\n")

    return portfolio

def calculate_portfolio(portfolio):
    """Returns a list of (ticker, qty, price, value) tuples + grand total."""
    rows = []
    total = 0.0
    for ticker, qty in portfolio.items():
        price = STOCK_PRICES[ticker]
        value = price * qty
        total += value
        rows.append((ticker, qty, price, value))
    return rows, total

def display_summary(rows, total):
    print("\n" + "=" * 55)
    print("          💼  PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"  {'Ticker':<8} {'Qty':>6}  {'Price':>10}  {'Value':>12}")
    print("-" * 55)
    for ticker, qty, price, value in rows:
        print(f"  {ticker:<8} {qty:>6}  {price:>10,.2f}  {value:>12,.2f}")
    print("-" * 55)
    print(f"  {'TOTAL INVESTMENT':>36}  {total:>12,.2f}")
    print("=" * 55)

def save_to_txt(rows, total, filename):
    """Save portfolio summary to a .txt file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w") as f:
        f.write("=" * 55 + "\n")
        f.write("        STOCK PORTFOLIO TRACKER - REPORT\n")
        f.write(f"  Generated : {timestamp}\n")
        f.write("=" * 55 + "\n\n")
        f.write(f"  {'Ticker':<8} {'Qty':>6}  {'Price':>10}  {'Value':>12}\n")
        f.write("-" * 55 + "\n")
        for ticker, qty, price, value in rows:
            f.write(f"  {ticker:<8} {qty:>6}  {price:>10,.2f}  {value:>12,.2f}\n")
        f.write("-" * 55 + "\n")
        f.write(f"  {'TOTAL INVESTMENT':>36}  {total:>12,.2f}\n")
        f.write("=" * 55 + "\n")
    print(f"\n  ✅ Report saved → {filename}")

def save_to_csv(rows, total, filename):
    """Save portfolio summary to a .csv file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Generated", timestamp])
        writer.writerow([])
        writer.writerow(["Ticker", "Quantity", "Price", "Total Value"])
        for ticker, qty, price, value in rows:
            writer.writerow([ticker, qty, f"{price:.2f}", f"{value:.2f}"])
        writer.writerow([])
        writer.writerow(["", "", "TOTAL", f"{total:.2f}"])
    print(f"  ✅ CSV saved     → {filename}")

# -------------------------------------------------------
def main():
    display_banner()
    display_available_stocks()

    portfolio = get_user_portfolio()

    if not portfolio:
        print("\n  ℹ️  No stocks entered. Exiting.\n")
        return

    rows, total = calculate_portfolio(portfolio)
    display_summary(rows, total)

    # --- Optional: save results ---
    print("\n💾 Save results?")
    print("   [1] Save as .txt")
    print("   [2] Save as .csv")
    print("   [3] Save both")
    print("   [4] Skip / Exit")

    choice = input("\n  Your choice (1/2/3/4): ").strip()
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = f"portfolio_{timestamp_str}"

    if choice in ("1", "3"):
        save_to_txt(rows, total, base + ".txt")
    if choice in ("2", "3"):
        save_to_csv(rows, total, base + ".csv")

    print("\n  👋 Thank you for using Stock Portfolio Tracker!\n")

# -------------------------------------------------------
if __name__ == "__main__":
    main()
