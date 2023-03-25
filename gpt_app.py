import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    print("####\n覚えたい単語を入力すると例文といつ使われるかの情報が出てきます")
    text = str(input())
    if len(text) >1:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                      {"role": "user", "content": 'generate two different example sentence from this word {} and is this word formal or not?'.format(text)}
                      ]
        )
        return print(response.choices[0]['message']['content'])
    else:
        return print("tell me correct word")
main()