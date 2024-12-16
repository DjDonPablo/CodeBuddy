import asyncio
import aiohttp
import json
import os

from pydantic import BaseModel
from prompts import get_prompt


class PromptRequest(BaseModel):
    prompt: str
    files: dict[str, str]


class CompletionRequest(BaseModel):
    context_before: str
    context_after: str


predict_session = None
predict_generator = None
autocomplete_session = None
autocomplete_generator = None


def get_url():
    if os.environ.get("OLLAMA_SERVER_URL"):
        return os.environ.get("OLLAMA_SERVER_URL") + "/api/generate"
    else:
        return "http://localhost:11434/api/generate"


async def predict(prompt: str, files: dict[str, str]):
    global predict_session
    global predict_generator

    if predict_generator:
        await predict_generator.aclose()
        print("Previous prediction task cancelled")

    if not predict_session:
        predict_session = aiohttp.ClientSession()

    model = "qwen2.5-coder:3b"
    body = {"model": model, "prompt": get_prompt(prompt=prompt, files=files)}

    async def fetch():
        async with predict_session.post(get_url(), json=body) as resp:
            async for line in resp.content:
                if line:
                    yield json.loads(line.decode("utf-8"))["response"]

    predict_generator = fetch()
    try:
        async for response in predict_generator:
            yield response
    except:  # noqa: E722
        print("Prediction task cancelled")


async def autocomplete(before_cursor: str, after_cursor: str):
    global autocomplete_session
    global autocomplete_generator

    if autocomplete_generator:
        autocomplete_generator.aclose()
        print("Previous autocomplete task cancelled")

    if not autocomplete_session:
        autocomplete_session = aiohttp.ClientSession()

    model = "qwen2.5-coder:3b-base"
    prompt = f"<|fim_prefix|>'{before_cursor}<|fim_suffix|>{after_cursor}<|fim_middle|>"
    body = {"model": model, "prompt": prompt}

    async def fetch():
        async with autocomplete_session.post(get_url(), json=body) as resp:
            async for line in resp.content:
                if line:
                    print(line)
                    yield json.loads(line.decode("utf-8"))["response"]

    autocomplete_generator = fetch()
    middle_passed = False
    try:
        async for response in autocomplete_generator:
            if middle_passed:
                print(response)
                yield response
            if "<|fim_middle|>" in response:
                middle_passed = True
    except asyncio.CancelledError:
        print("Autocomplete task was cancelled")
