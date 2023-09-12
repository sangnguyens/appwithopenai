#!/usr/bin/env python3

"""
An openai api key is required to use this script.
This uses an advanced GPT-3 model and I also used AI via Codeium to write this command-line interface.
"""

import openai
import os
import click


def submit_question(question):
    """This submits a question to the OpenAI API"""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = question

    result = openai.Completion.create(
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        model="text-davinci-003",
    )["choices"][0]["text"].strip("\n"P)

    return result


@click.command()
@click.argument("question")
def main(question: str="What is the capital of France?"):
    """This is the main function that you ask the OpenAI a question to get an answer
    Example: ./questionAnswerCLI.py "What is the capital of France?"

    """
    print(submit_question(question))


if __name__ == "__main__":
    main()
