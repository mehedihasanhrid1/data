import re
import json
import random
from difflib import SequenceMatcher
from collections import defaultdict
from colorama import Fore, Style, init

init(autoreset=True)

# =========================================================
# DATA
# =========================================================

DATA = {
    "bot": {
        "name": "TravelBot",
        "followup": "Need more travel assistance?"
    },

    "synonyms": {
        "cheap": "budget",
        "affordable": "budget",
        "lowcost": "budget",
        "vacation": "travel",
        "trip": "travel",
        "journey": "travel",
        "tour": "travel"
    },

    "intents": [

        {
            "tag": "greeting",
            "patterns": [
                "hello",
                "hi",
                "hey",
                "good morning",
                "good evening"
            ],
            "responses": [
                "Hello! Welcome to TravelBot.",
                "Hi! How can I assist your travel plans?",
                "Greetings traveler!"
            ]
        },

        {
            "tag": "destination",
            "patterns": [
                "recommend destination",
                "where should i travel",
                "suggest a place",
                "travel destination",
                "best place to visit"
            ],
            "responses": [
                "Sure! Let me find destinations for you."
            ]
        },

        {
            "tag": "packing",
            "patterns": [
                "packing",
                "packing checklist",
                "what should i pack",
                "travel bag",
                "luggage"
            ],
            "responses": [
                "Sure! I can help with packing."
            ]
        },

        {
            "tag": "safety",
            "patterns": [
                "travel safety",
                "safe travel",
                "safety tips",
                "solo safety"
            ],
            "responses": [
                "Here are important travel safety tips."
            ]
        },

        {
            "tag": "yes",
            "patterns": [
                "yes",
                "yeah",
                "sure",
                "okay",
                "ok"
            ],
            "responses": []
        },

        {
            "tag": "no",
            "patterns": [
                "no",
                "not now",
                "nope"
            ],
            "responses": [
                "Alright."
            ]
        },

        {
            "tag": "exit",
            "patterns": [
                "bye",
                "quit",
                "exit",
                "thanks"
            ],
            "responses": [
                "Thank you for using TravelBot. Safe journey!"
            ]
        }
    ],

    "destinations": [

        {
            "name": "Cox's Bazar",
            "country": "Bangladesh",
            "budget": "low",
            "type": ["beach", "family", "nature"],
            "rating": 4.5,
            "best_time": "November to February",
            "safety": "high",
            "activities": [
                "Sea beach",
                "Boat rides",
                "Sea food"
            ]
        },

        {
            "name": "Pokhara",
            "country": "Nepal",
            "budget": "medium",
            "type": ["mountain", "solo", "nature"],
            "rating": 4.7,
            "best_time": "September to November",
            "safety": "medium",
            "activities": [
                "Paragliding",
                "Boating",
                "Hiking"
            ]
        },

        {
            "name": "Singapore",
            "country": "Singapore",
            "budget": "high",
            "type": ["city", "shopping", "family"],
            "rating": 4.8,
            "best_time": "February to April",
            "safety": "high",
            "activities": [
                "Universal Studios",
                "Marina Bay Sands",
                "Gardens by the Bay"
            ]
        }
    ],

    "packing": {

        "beach": [
            "Sunscreen",
            "Sunglasses",
            "Light clothes",
            "Sandals"
        ],

        "mountain": [
            "Jacket",
            "Boots",
            "Gloves",
            "Thermal wear"
        ],

        "city": [
            "Casual clothes",
            "Power bank",
            "Travel documents",
            "Comfortable shoes"
        ]
    },

    "safety_tips": [
        "Keep emergency contacts",
        "Carry travel insurance",
        "Avoid isolated areas at night",
        "Protect your important documents",
        "Keep backup cash"
    ]
}

# =========================================================
# GLOBALS
# =========================================================

BOT = DATA["bot"]
INTENTS = DATA["intents"]
DESTINATIONS = DATA["destinations"]
PACKING = DATA["packing"]
SAFETY = DATA["safety_tips"]
SYNONYMS = DATA["synonyms"]

STOP_WORDS = {
    "i", "me", "you", "my", "your",
    "the", "a", "an", "is", "am",
    "are", "to", "for", "with",
    "please", "help"
}

INTERESTS = {
    "beach",
    "mountain",
    "city",
    "nature",
    "shopping",
    "family",
    "solo"
}

BUDGET_MAP = {
    "budget": "low",
    "luxury": "high"
}

# =========================================================
# SESSION MEMORY
# =========================================================

class SessionMemory:

    def __init__(self):

        self.context = {
            "last_intent": None,
            "awaiting": None
        }

        self.profile = defaultdict(lambda: None)

        self.history = []

    def remember(self, user, bot):

        self.history.append({
            "user": user,
            "bot": bot
        })

        if len(self.history) > 20:
            self.history.pop(0)

MEMORY = SessionMemory()

# =========================================================
# NLP UTILITIES
# =========================================================

def clean_text(text):

    text = re.sub(r"[^a-z\s]", "", text.lower())

    return [
        SYNONYMS.get(word, word)
        for word in text.split()
        if word not in STOP_WORDS
    ]

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

# =========================================================
# INTENT ENGINE
# =========================================================

class IntentEngine:

    @staticmethod
    def detect(user_input):

        tokens = clean_text(user_input)

        best_match = None
        best_score = 0

        for intent in INTENTS:

            score = 0

            for pattern in intent["patterns"]:

                pattern_tokens = clean_text(pattern)

                score += sum(
                    3 if t == p else 1
                    for t in tokens
                    for p in pattern_tokens
                    if similarity(t, p) > 0.75
                )

            if score > best_score:
                best_score = score
                best_match = intent

        return best_match

# =========================================================
# PROFILE ENGINE
# =========================================================

class ProfileEngine:

    @staticmethod
    def update(user_input):

        text = user_input.lower()

        for key, value in BUDGET_MAP.items():
            if key in text:
                MEMORY.profile["budget"] = value

        for interest in INTERESTS:
            if interest in text:
                MEMORY.profile["interest"] = interest

# =========================================================
# RESPONSE ENGINE
# =========================================================

class ResponseEngine:

    @staticmethod
    def print_bot(message):

        print(
            Fore.GREEN +
            Style.BRIGHT +
            f"TravelBot: {message}"
        )

    @staticmethod
    def show_destinations():

        interest = MEMORY.profile["interest"]
        budget = MEMORY.profile["budget"]

        matches = [

            d for d in DESTINATIONS

            if (
                (not interest or interest in d["type"]) and
                (not budget or budget == d["budget"])
            )
        ]

        matches.sort(
            key=lambda x: x["rating"],
            reverse=True
        )

        if not matches:
            ResponseEngine.print_bot(
                "No matching destinations found."
            )
            return

        print(Fore.CYAN + Style.BRIGHT)

        for i, d in enumerate(matches, 1):

            print(f"\n{i}. {d['name']} ({d['country']})")
            print(f"   Rating: {d['rating']}/5")
            print(f"   Budget: {d['budget'].title()}")
            print(f"   Safety: {d['safety'].title()}")
            print(f"   Best Time: {d['best_time']}")

            print("   Activities:")

            for activity in d["activities"]:
                print(f"    • {activity}")

    @staticmethod
    def show_packing():

        interest = MEMORY.profile["interest"]

        if interest in PACKING:

            print(Fore.CYAN + Style.BRIGHT)

            print(
                f"\nPacking Checklist for "
                f"{interest.title()} Travel:\n"
            )

            for item in PACKING[interest]:
                print(f"• {item}")

            return

        MEMORY.context["awaiting"] = "packing_interest"

        ResponseEngine.print_bot(
            "What type of travel are you planning? "
            "beach, mountain, or city?"
        )

    @staticmethod
    def show_safety():

        print(Fore.CYAN + Style.BRIGHT)

        print("\nTravel Safety Tips:\n")

        for tip in SAFETY:
            print(f"• {tip}")

# =========================================================
# CONVERSATION ENGINE
# =========================================================

class ConversationEngine:

    @staticmethod
    def handle_followup(user_input):

        awaiting = MEMORY.context["awaiting"]

        if awaiting == "packing_interest":

            ProfileEngine.update(user_input)

            if MEMORY.profile["interest"] in PACKING:

                MEMORY.context["awaiting"] = None

                ResponseEngine.show_packing()

                return True

        return False

    @staticmethod
    def process(user_input):

        ProfileEngine.update(user_input)

        if ConversationEngine.handle_followup(user_input):
            return

        intent = IntentEngine.detect(user_input)

        if not intent:

            ResponseEngine.print_bot(
                "Sorry, I didn't understand."
            )
            return

        tag = intent["tag"]

        MEMORY.context["last_intent"] = tag

        if intent["responses"]:

            ResponseEngine.print_bot(
                random.choice(intent["responses"])
            )

        ACTIONS = {

            "destination": ResponseEngine.show_destinations,
            "packing": ResponseEngine.show_packing,
            "safety": ResponseEngine.show_safety
        }

        if tag in ACTIONS:
            ACTIONS[tag]()

        elif tag == "yes":

            last = MEMORY.context["last_intent"]

            if last == "destination":
                ResponseEngine.show_destinations()

            elif last == "packing":
                ResponseEngine.show_packing()

        elif tag == "exit":
            exit()

        print(
            Fore.CYAN +
            f"\nTravelBot: {BOT['followup']}"
        )
