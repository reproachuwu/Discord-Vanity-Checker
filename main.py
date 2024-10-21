import aiohttp
import asyncio
import datetime
import random
from nltk.corpus import words
from nltk.probability import FreqDist
from collections import deque

# Input User Token
Authorization = "YOUR_USER_TOKEN"

# Input Webhook URL to Notify
Notify = "WEBHOOK_URL"

# Set to True to use tokens, False to run without tokens
token_mode = False  

# Lets you choose if you want to input the vanity url or not
selection_mode = False  

API_ENDPOINT = "https://discord.com/api/v9/invites/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

if token_mode:
    HEADERS["Authorization"] = Authorization

async def notify(message, is_available):
    embed = {
        "title": "Vanity URL Check Result 🔍",
        "color": 0x00ff00 if is_available else 0xff0000,
        "fields": [
            {
                "name": "Status",
                "value": f"{'✅ Available' if is_available else '❌ Taken'}",
                "inline": False
            },
            {
                "name": "Vanity URL",
                "value": f"`{message}`",
                "inline": False
            }
        ],
        "footer": {
            "text": "reproachuwu on github | Vanity URL Checker"
        },
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    
    payload = {
        "embeds": [embed]
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(Notify, json=payload) as response:
            return response.status

async def check_vanity(vanity_code, session):
    async with session.get(API_ENDPOINT + vanity_code, headers=HEADERS) as response:
        if response.status == 404:
            print(f"The vanity URL '{vanity_code}' is available to claim!")
            await notify(f"The vanity URL '{vanity_code}' is available to claim! | Coded By Rep", True)
            try:
                with open('results.txt', 'a') as f:
                    f.write(f"{vanity_code}\n")
                print(f"Successfully wrote '{vanity_code}' to results.txt")
            except IOError as e:
                print(f"Error writing to file: {e}")
        elif response.status == 200:
            print(f"The vanity URL '{vanity_code}' is already taken.")
            await notify(f"The vanity URL '{vanity_code}' is already taken. | Coded By Rep", False)
        else:
            print(f"An error occurred. Status code: {response.status}")

async def main():
    # Get the most common words
    all_words = words.words()
    freq_dist = FreqDist(word.lower() for word in all_words if 3 <= len(word) <= 5)
    common_words = [word for word, _ in freq_dist.most_common(1000)]

    request_times = deque(maxlen=50)

    async with aiohttp.ClientSession() as session:
        while True:
            if selection_mode:
                vanity_code = input("Enter the vanity URL to check (or 'quit' to exit): ").strip()
                if vanity_code.lower() == 'quit':
                    break
            else:
                vanity_code = random.choice(common_words)

            print(f"Checking vanity code: {vanity_code}")

            # Rate limiting
            now = datetime.datetime.now()
            if len(request_times) == 50:
                oldest_request = request_times[0]
                if (now - oldest_request).total_seconds() < 1:
                    await asyncio.sleep(1 - (now - oldest_request).total_seconds())

            await check_vanity(vanity_code, session)
            request_times.append(datetime.datetime.now())

            if selection_mode:
                continue_check = input("Do you want to check another vanity URL? (y/n): ").strip().lower()
                if continue_check != 'y':
                    break

if __name__ == "__main__":
    # Mode Choose
    mode_choice = input("Choose mode (1 for automatic, 2 for manual input): ").strip()
    selection_mode = (mode_choice == '2')
    
    asyncio.run(main())


# Please note we are not checking Banned URLs or Unavailable URLs and will flag them as available
# This may be fixed in the future if i have time