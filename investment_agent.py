from agents.analysis_chain import analyze_stock

def run_investment_assistant(ticker: str):
    print(f"\n🔍 Analyzing {ticker}...\n")

    result = analyze_stock(ticker)

    print(f"\n📊 Investment Analysis for {ticker}:\n")
    print(result)
    print("\n" + "="*50 + "\n")
