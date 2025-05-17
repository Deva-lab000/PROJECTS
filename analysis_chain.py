from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Initialize Ollama LLM
llm = OllamaLLM(model="deepseek-r1", temperature=0.3)

# Define prompt template
prompt = PromptTemplate.from_template(
    """
    You are an AI financial analyst.
    Analyze the stock performance of {ticker} based on recent trends, financials, and market news.
    Provide a brief summary and suggest whether it's a Buy, Hold, or Sell.
    """
)

# Create chain using pipe syntax
analysis_chain = prompt | llm

# Function to analyze stock
def analyze_stock(ticker: str) -> str:
    result = analysis_chain.invoke({"ticker": ticker})
    return result
