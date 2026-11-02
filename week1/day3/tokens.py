import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"
role = "user"

# 3 prompts
prompt1 = "Hi!"
prompt2 = "Explain time travel in Detail"
prompt3 = "Write a 1000 word essay on Machine Learning"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {"role": role, "content": prompt}
    messages = [message]
    response = client.chat.completions.create(
        model=model, messages=messages, max_tokens=50
    )
    usage = response.usage
    print(
        f"Prompt: {prompt} -->yours token: {usage.prompt_tokens} completion_token: {usage.completion_tokens} total token:{usage.prompt_tokens + usage.completion_tokens} Finish Reason: {response.choices[0].finish_reason}"
    )

# message_system = {
#     "role": "system",
#     "content": "you are a brand manager who suggests name for my food company. name should be in one word. suggest 1 name only",
# }

# message = {"role": role, "content": prompt}

# # first pass message system
# messages = [message_system, message]

# # temperature by default is 0 meaning safe -> {0,1,2}
# response = client.chat.completions.create(model=model, messages=messages, temperature=2)
# print(response.choices[0].message.content)
