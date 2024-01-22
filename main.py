from bot_init import bot
from dotenv import load_dotenv
import os

load_dotenv()

def main():
	bot.run(os.environ.get("DISCORD_TOKEN"))

if __name__ == "__main__":
	main()