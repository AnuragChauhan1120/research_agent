from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
import os

load_dotenv()

app = FastAPI()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv( "GROQ_API_KEY")
)

# search_tool = TavilySearchResults(
#     max_results=3,
#     tavily_api_key=os.getenv("TAVILY_API_KEY")
# )
search_tool = TavilySearch(max_results=3)

tools = [search_tool]

agent = create_react_agent(llm, tools)


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {"status": "Research Agent API is running"}


@app.post("/analyze")
def analyze(request: QueryRequest):
    result = agent.invoke({"messages": [{"role": "user", "content": request.query}]})
    return {
        "query": request.query,
        "result": result["messages"][-1].content
    }