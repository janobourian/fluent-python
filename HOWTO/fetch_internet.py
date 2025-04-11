import os
import json
import asyncio
import concurrent.futures
import random
import urllib.request
import urllib.parse
import functools
from dotenv import load_dotenv
import time

load_dotenv(override=True)

set_interactions_ids = [
    "4e9436eb-9718-4b45-b199-b8153906a153",
    "82d5869a-e3c1-48dc-842b-08a2a37bd755",
    "d45fc4a5-a525-4c09-9351-a483065c84f6",
    "cea1f55f-95e9-449e-86a9-399d1a5245e4",
    "6e13eb7e-8074-4f48-8108-9bff5d33a1c3",
    "c6e44083-33a4-4049-b2bb-10f4d4243290",
    "5282654a-a69f-4e14-9670-325d270441dc",
    "05292c59-cae3-41a6-a5bc-f7862d68897c",
    "4e9436eb-9718-4b45-b199-b8153906a153",
    "15282c5a-ce30-4f28-b236-ef27458e8c18"
]


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


def generate_questions(file:str):
    temp_lines = []
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file)
    with open(file_path, "r") as f:
        for line in f:
            temp_lines.append(line.strip())
    return temp_lines


question_list = generate_questions("HOWTO/questions.txt")


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
    start_time = time.time()
    result = None
    headers = {
        "X-APP-VERSION": os.getenv("X_APP_VERSION"),
        "X-API-KEY": os.getenv("X_API_KEY"),
        "Content-Type": "application/json",
    }
    body = {"interaction_id": interaction_id, "question": random.choice(question_list)}

    data = json.dumps(body).encode("utf-8")
    url_interaction = urllib.request.Request(
        os.getenv("URL_SOFIA"), data=data, headers=headers
    )
    with urllib.request.urlopen(url_interaction) as response:
        result = json.loads(response.read().decode("utf-8"))
    question = body.get("question")
    answer = result.get("answer")
    log_line = (
        f"Interaction_id: {interaction_id} - Question: {question} - Answer: {answer}\n"
    )
    current_dir = os.getcwd()
    output_file = os.path.join(current_dir, "HOWTO/chat_results.txt")
    with open(output_file, "a") as f:
        f.write(log_line)
        
    print(f"****************: {time.time() - start_time}")

    return result.get("answer")

questions_chatbot = generate_questions("HOWTO/questions_chatbot.txt")
print("questions_chatbot", questions_chatbot)

def ask_chatbot_promotores(interaction_id: str):
    start_time = time.time()
    result = None
    body = {"interaction_id": interaction_id, "question": random.choice(questions_chatbot)}

    data = json.dumps(body).encode("utf-8")
    headers = {
        "Authorization": "43d975e4-3d3a-4534-a980-66eaf5e4e1d2",
        "Content-Type": "application/json",
    }
    print("data", data)
    print("URL_CHATBOT_PROMOTORES", os.getenv("URL_CHATBOT_PROMOTORES"))
    url_interaction = urllib.request.Request(
        os.getenv("URL_CHATBOT_PROMOTORES"), data=data, headers=headers
    )
    with urllib.request.urlopen(url_interaction) as response:
        result = json.loads(response.read().decode("utf-8"))
    question = body.get("question")
    answer = result.get("answer")
    log_line = (
        f"Interaction_id: {interaction_id} - Question: {question} - Answer: {answer}\n"
    )
    current_dir = os.getcwd()
    output_file = os.path.join(current_dir, "HOWTO/chatbot_results.txt")
    with open(output_file, "a") as f:
        f.write(log_line)
        
    print(f"****************: {time.time() - start_time}")

    return result.get("answer")

def ask_chat_lite(interaction_id: str):
    start_time = time.time()
    result = None
    headers = {
        "X-APP-VERSION": os.getenv("X_APP_VERSION"),
        "X-API-KEY": os.getenv("X_API_KEY"),
        "Content-Type": "application/json",
    }
    body = {"interaction_id": interaction_id, "question": random.choice(question_list)}

    data = json.dumps(body).encode("utf-8")
    url_interaction = urllib.request.Request(
        os.getenv("URL_LITE"), data=data, headers=headers
    )
    with urllib.request.urlopen(url_interaction) as response:
        result = json.loads(response.read().decode("utf-8"))
    question = body.get("question")
    answer = result.get("answer")
    log_line = (
        f"Interaction_id: {interaction_id} - Question: {question} - Answer: {answer}\n"
    )
    current_dir = os.getcwd()
    output_file = os.path.join(current_dir, "HOWTO/lite_results.txt")
    with open(output_file, "a") as f:
        f.write(log_line)
    
    print(f"****************: {time.time() - start_time}")

    return result.get("answer")

async def main():
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        tasks = [loop.run_in_executor(executor, get_interaction_id) for _ in range(5)]
        _ = await asyncio.gather(*tasks)

    loop_chat = asyncio.get_running_loop()

    print(interaction_ids)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        chat_tasks = [
            loop_chat.run_in_executor(
                executor, functools.partial(ask_chat_lite, interaction)
            )
            for interaction in interaction_ids
        ]
        _ = await asyncio.gather(*chat_tasks)

    # loop_chat = asyncio.get_running_loop()
    # with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    #     chat_tasks = [
    #         loop_chat.run_in_executor(
    #             executor, functools.partial(ask_chatbot_promotores, interaction)
    #         )
    #         for interaction in set_interactions_ids
    #     ]
    #     _ = await asyncio.gather(*chat_tasks)


asyncio.run(main())
