import openai
from abc import ABC,abstractmethod
from loguru import logger
import os
from dotenv import load_dotenv

load_dotenv()

class AgentBase(ABC):
    def __init__(self,name,max_retries=2,verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_openai(self,messages,temperature =0.7,max_tokens=150):
        retries =0
        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}] Sending message to OpenAI")
                    for msg in messages:
                        logger.debug(f"{msg['role']}: {msg['content']}")
                response = openai.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                reply = response.choices[0].message
                if self.verbose:
                    logger.info(f"[{self.name}] Received Response: {reply}")
                return reply
            except Exception as e:
                retries +=1
                logger.error(f"[{self.name}] Error during OpenAI call: {e}. Retry {retries}/{self.max_retries}")
        raise Exception(f"[{self.name}] failed to get response fron OpenAI after {retries} retries")
