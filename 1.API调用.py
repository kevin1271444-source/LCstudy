from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('ARK_API_KEY')
base_url = os.getenv('ARK_BASE_URL')
client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

# 创建一个对话请求
response = client.chat.completions.create(
    model="deepseek-v3-2-251201",
    messages=[
        {"role": "system", "content": "你是python专家，不要说废话"},
        {"role": "assistant", "content": ""},
        {"role": "user", "content": "上海的天气怎么样？"},
        ]
)

print(response.choices[0].message.content)