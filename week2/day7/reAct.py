import os
from pathlib import Path
from urllib import response
from dotenv import load_dotenv
from groq import Groq
import re
from time import sleep

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key=my_api_key)
model = "qwen/qwen3.8-27b"


# tools means api but we created our own tool/api
def get_product_price(product):
    if product == "iphone 17":
        return 1000
    elif product == "iphone 15":
        return 500
    else:
        return 0


def calculator(expression):
    try:
        return eval(expression)
    except:
        return "calc error!"


tools = {"get_product_price": get_product_price, "calculator": calculator}

system_prompt = """
You are a shopping assistant.

you have these tools:
get_product_price(product)
calculator(expression)
IMPORTANT:
Call tools exactly like these examples:

Action: get_product_price("iphone 17")
Action: calculator("5000-1000")

Never write
get_product_price(product="iphone 17")

Never write
calculatore(xpression="5000-1000")

Follow these rules:

1. Decide what you need to do next.
2. Call ONLY one tool at a time.
3. After writing an Action, STOP immediately.
4. Never guess or invent a tool result.
5. Wait until you receive an observation.
6. Then decide your next action.
7. When the task is complete, give the final answer.

Format:

Thought: what you need to do
Action: tool_name(argument)

when finished: 

Final Answer: your answer
"""


def run_agent(question):

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ]

    for step in range(5):
        print("\n_________")
        print("STEP", step + 1)
        print("-----------")

        response = client.chat.completions.create(
            model=model, messages=messages, temperature=0
        )

        answer = response.choices[0].message.content

        print(answer)

        # Agent has finished
        if "Final Answer:" in answer:
            break

        # find action
        match = re.search(r"Action:\s*(\w+)\((.*?)\)", answer)

        if match:
            tool_name = match.group(1)

            tool_input = match.group(2)

            tool_input = tool_input.strip()

            tool_input = tool_input.strip('"')

            if tool_name in tools:

                tool = tools[tool_name]

                observation = tool(tool_input)
            else:

                observation = "Tool not found"

            print("observation:", observation)

            # add LLM response to memory
            messages.append({"role": "assistant", "content": answer})

            # Give tool result back to llm
            messages.append(
                {"role": "user", "content": "Observation: " + str(observation)}
            )
            sleep(5)


prompt = """
I have 5000 rupees. what is the price of an iphone 17?
and how much money will I have left?
"""

run_agent(prompt)
