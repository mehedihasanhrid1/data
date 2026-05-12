DATA = {
    "bot": {
        "name": "TravelBot",
        "language": "en",
        "followup": "Would you like more travel help?"
    },

    "synonyms": {
        "cheap": "budget",
        "affordable": "budget",
        "lowcost": "budget",
        "secure": "safe",
        "tour": "travel",
        "trip": "travel",
        "vacation": "travel",
        "journey": "travel"
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
                "Hi there! How can I help with your travel plans?",
                "Greetings traveler!"
            ]
        },

        {
            "tag": "budget",
            "patterns": [
                "cheap travel",
                "budget trip",
                "low cost destination",
                "affordable place",
                "budget travel"
            ],
            "responses": [
                "I can suggest some excellent budget-friendly destinations."
            ]
        },

        {
            "tag": "destination",
            "patterns": [
                "recommend destination",
                "best place to visit",
                "where should i travel",
                "travel destination",
                "suggest a place"
            ],
            "responses": [
                "Here are some destinations you may like:"
            ]
        },

        {
            "tag": "packing",
            "patterns": [
                "packing",
                "what should i pack",
                "travel bag",
                "luggage",
                "packing checklist"
            ],
            "responses": [
                "Here is your packing checklist."
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
            "tag": "exit",
            "patterns": [
                "bye",
                "exit",
                "quit",
                "thanks"
            ],
            "responses": [
                "Thank you for using TravelBot. Have a safe journey!"
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
            "activities": [
                "Sea beach",
                "Boat rides",
                "Sea food"
            ],
            "safety": "high"
        },

        {
            "name": "Dubai",
            "country": "UAE",
            "budget": "high",
            "type": ["luxury", "shopping", "city"],
            "rating": 4.9,
            "best_time": "December to March",
            "activities": [
                "Burj Khalifa",
                "Desert Safari",
                "Luxury Shopping"
            ],
            "safety": "high"
        },

        {
            "name": "Pokhara",
            "country": "Nepal",
            "budget": "medium",
            "type": ["mountain", "nature", "solo"],
            "rating": 4.7,
            "best_time": "September to November",
            "activities": [
                "Hiking",
                "Boating",
                "Paragliding"
            ],
            "safety": "medium"
        },

        {
            "name": "Singapore",
            "country": "Singapore",
            "budget": "high",
            "type": ["city", "family", "shopping"],
            "rating": 4.8,
            "best_time": "February to April",
            "activities": [
                "Universal Studios",
                "Marina Bay Sands",
                "Gardens by the Bay"
            ],
            "safety": "high"
        },

        {
            "name": "Bhutan",
            "country": "Bhutan",
            "budget": "medium",
            "type": ["nature", "mountain", "peaceful"],
            "rating": 4.6,
            "best_time": "March to May",
            "activities": [
                "Monastery Visit",
                "Mountain Trekking",
                "Photography"
            ],
            "safety": "high"
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
        "Secure your important documents",
        "Keep backup cash"
    ]
}

BOT = DATA["bot"]
INTENTS = DATA["intents"]
DESTINATIONS = DATA["destinations"]
PACKING = DATA["packing"]
SAFETY = DATA["safety_tips"]
SYNONYMS = DATA["synonyms"]

STOP_WORDS = {
    "i", "me", "you", "please", "help",
    "the", "a", "an", "is", "am", "are",
    "to", "for", "with", "my", "your",
    "of", "some", "any"
}
