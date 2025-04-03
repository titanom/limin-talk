from limin import ModelConfiguration
from limin_talk import Character, talk

user_character = Character(
    system_prompt="You are a helpful assistant who only speaks English.",
    model_configuration=ModelConfiguration(model="gpt-4o"),
)

assistant_character = Character(
    system_prompt="You are a helpful assistant who only speaks German.",
    model_configuration=ModelConfiguration(model="gpt-4o"),
)


async def main():
    conversation = await talk(user_character, assistant_character, 3)
    print(conversation.to_pretty_string())


if __name__ == "__main__":
    import asyncio
    import dotenv

    dotenv.load_dotenv()

    asyncio.run(main())
