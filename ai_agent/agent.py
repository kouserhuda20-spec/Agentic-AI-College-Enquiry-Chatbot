
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    ToolMessage
)

from .tools import tools


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env", override=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()


# ==========================================
# REGISTER AI TOOLS
# ==========================================

tool_map = {tool.name: tool for tool in tools}


# ==========================================
# AI SYSTEM INSTRUCTIONS
# ==========================================

SYSTEM_PROMPT = """
You are an Agentic AI College Admissions Assistant
specialized in Bengaluru engineering colleges.

YOUR RESPONSIBILITIES:
1. Answer college-related questions.
2. Explain courses and engineering branches.
3. Provide admission fee information.
4. Explain KCET and COMEDK cutoffs.
5. Explain placement packages.
6. Compare two colleges.
7. Retrieve additional knowledge using RAG.

IMPORTANT RULES:

- Always use database tools for college-specific information.
- Use compare_colleges for comparison requests.
- Use get_college_info for individual college information.
- Use RAG when additional document-based knowledge is needed.
- Never invent fees, cutoffs, placement figures or admission details.
- If information is unavailable, clearly say Not Available.
- Keep answers clear, friendly and concise.
- Use tables for college comparisons.
- Do not make unnecessary tool calls.
"""


# ==========================================
# INITIALIZE GROQ MODEL ONCE
# ==========================================

_llm_with_tools = None


def get_llm():

    global _llm_with_tools

    if _llm_with_tools is None:

        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing from .env")

        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            groq_api_key=GROQ_API_KEY,
            temperature=0
        )

        _llm_with_tools = llm.bind_tools(tools)

    return _llm_with_tools


# ==========================================
# AGENTIC AI QUERY FUNCTION
# ==========================================

def query_agent(user_message: str) -> str:

    if not GROQ_API_KEY:
        return "Backend Error: Please configure GROQ_API_KEY in your .env file."

    if not user_message or not user_message.strip():
        return "Please enter a valid question."

    try:

        llm_with_tools = get_llm()

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_message.strip())
        ]

        # Limit unnecessary agent iterations
        max_iterations = 3

        for iteration in range(max_iterations):

            response = llm_with_tools.invoke(messages)

            # Return final AI response
            if not response.tool_calls:

                answer = response.content

                if isinstance(answer, str):
                    return answer.strip()

                return str(answer)

            messages.append(response)

            # Execute selected tools
            for tool_call in response.tool_calls:

                tool_name = tool_call["name"]
                tool_args = tool_call.get("args", {})
                tool_id = tool_call["id"]

                selected_tool = tool_map.get(tool_name)

                if selected_tool is None:
                    result = f"Unknown tool: {tool_name}"

                else:
                    try:
                        result = selected_tool.invoke(tool_args)

                    except Exception as tool_error:
                        print(
                            f"Tool Error ({tool_name}):",
                            str(tool_error)
                        )

                        result = (
                            "The requested information could not "
                            "be retrieved from this tool."
                        )

                messages.append(
                    ToolMessage(
                        content=str(result),
                        tool_call_id=tool_id
                    )
                )

        # One final response after tool execution
        final_response = llm_with_tools.invoke(messages)

        if final_response.tool_calls:
            return (
                "I found some information but could not complete "
                "the answer. Please try a more specific question."
            )

        return str(final_response.content).strip()

    except Exception as e:

        print("Agent Error:", str(e))

        return (
            "Sorry, I encountered an error while processing "
            "your question. Please try again."
        )
