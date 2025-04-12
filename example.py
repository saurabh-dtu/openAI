import openai
import asyncio

async def get_response_from_openai(prompt: str):
    """Fetch response from OpenAI's language model."""
    response = openai.chat.completions.create(
        model="gpt-4",  # Use the most suitable model for your task
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

async def main():
    spanish_agent = {
        "name": "Spanish agent",
        "instructions": "You only speak Spanish."
    }

    english_agent = {
        "name": "English agent",
        "instructions": "You only speak English."
    }

    triage_agent = {
        "name": "Triage agent",
        "instructions": "Handoff to the appropriate agent based on the language of the request.",
        "handoffs": [spanish_agent, english_agent]
    }

    # Assume input is a language-agnostic string
    input_text = "Hola, ¿cómo estás?"

    if "¿" in input_text or "¡" in input_text:  # Simple check for Spanish input
        agent = spanish_agent
        prompt = f"Act as a {agent['name']} and respond in Spanish. {input_text}"
    else:
        agent = english_agent
        prompt = f"Act as a {agent['name']} and respond in English. {input_text}"

    # Get the response asynchronously
    result = await get_response_from_openai(prompt)
    print(f"Response from {agent['name']}: {result}")

if __name__ == "__main__":
    asyncio.run(main())
