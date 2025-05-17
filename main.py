from agents.investment_agent import run_investment_assistant

def main():
    print("🧠 Welcome to AI Investment Assistant 📊")
    print("Type a stock ticker (e.g., AAPL, TSLA) or 'exit' to quit.\n")

    while True:
        ticker = input("Enter stock ticker: ").strip().upper()
        if ticker.lower() == 'exit':
            print("Goodbye! 👋")
            break
        
        if ticker:
            try:
                run_investment_assistant(ticker)
            except Exception as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
