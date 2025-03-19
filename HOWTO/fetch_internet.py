import os
import json
import asyncio
import concurrent.futures
import random
import urllib.request
import urllib.parse
import functools
from set_ids import set_interactions_ids
from dotenv import load_dotenv

load_dotenv(override=True)


# Single HTTP response

with urllib.request.urlopen(os.getenv("URL_TO_FETCH")) as response:
    print(response.read().decode("utf-8"))

# Using Request class

req = urllib.request.Request(os.getenv("URL_TO_FETCH"))
with urllib.request.urlopen(req) as response:
    print(response.read().decode("utf-8"))

# Using headers, but remember that you can use Data such as Parameters too

background_tasks = set()
interaction_ids = []
lines = []


def generate_questions():
    temp_lines = []
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "HOWTO/questions.txt")
    with open(file_path, "r") as f:
        for line in f:
            temp_lines.append(line.strip())
    return temp_lines


question_list = generate_questions()


def get_interaction_id():
    result = None
    headers = {
        "X-APP-VERSION": os.getenv("X_APP_VERSION"),
        "X-API-KEY": os.getenv("X_API_KEY"),
        "Content-Type": "application/json",
    }
    body = {"access_token": ""}

    data = json.dumps(body).encode("utf-8")
    url_interaction = urllib.request.Request(
        os.getenv("URL_INTERACTION"), data=data, headers=headers
    )
    with urllib.request.urlopen(url_interaction) as response:
        result = json.loads(response.read().decode("utf-8"))
        interaction_ids.append(result.get("interaction_id"))
    return result.get("interaction_id")


def ask_chat(interaction_id: str):
    result = None
    headers = {
        "X-APP-VERSION": os.getenv("X_APP_VERSION"),
        "X-API-KEY": os.getenv("X_API_KEY"),
        "Content-Type": "application/json",
    }
    body = {"interaction_id": interaction_id, "question": random.choice(question_list)}

    data = json.dumps(body).encode("utf-8")
    url_interaction = urllib.request.Request(
        os.getenv("URL_CHAT"), data=data, headers=headers
    )
    with urllib.request.urlopen(url_interaction) as response:
        result = json.loads(response.read().decode("utf-8"))
    question = body.get("question")
    answer = result.get("answer")
    log_line = f"Question: {question} - Answer: {answer}\n"
    current_dir = os.getcwd()
    output_file = os.path.join(current_dir, "HOWTO/chat_results.txt")
    with open(output_file, "a") as f:
        f.write(log_line)

    return result.get("answer")


async def main():
    # loop = asyncio.get_running_loop()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     tasks = [loop.run_in_executor(executor, get_interaction_id) for _ in range(100)]
    #     _ = await asyncio.gather(*tasks)

    # loop_chat = asyncio.get_running_loop()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     chat_tasks = [
    #     loop_chat.run_in_executor(executor, functools.partial(ask_chat, interaction))
    #     for interaction in interaction_ids
    # ]
    #     _ = await asyncio.gather(*chat_tasks)

    loop_chat = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        chat_tasks = [
            loop_chat.run_in_executor(
                executor, functools.partial(ask_chat, interaction)
            )
            for interaction in set_interactions_ids
        ]
        _ = await asyncio.gather(*chat_tasks)


asyncio.run(main())
