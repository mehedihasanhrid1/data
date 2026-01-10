STOP_WORDS = {
    "i", "me", "you", "can", "please", "help", "on", "about",
    "the", "a", "an", "is", "am", "are", "to", "for", "with",
    "my", "your", "of", "before", "after", "some", "any"
}


def destination_help():
    return (
        "Destination Suggestions:\n"
        "- Budget: Cox’s Bazar, Nepal, Darjeeling\n"
        "- Nature: Bhutan, Switzerland, Kashmir\n"
        "- City: Dubai, Singapore, Bangkok"
    )

def packing_help():
    return (
        "Packing Checklist:\n"
        "- Documents\n"
        "- Clothes (weather-based)\n"
        "- Toiletries\n"
        "- Medicines\n"
        "- Charger & power bank\n"
        "- Emergency cash"
    )

def budget_help():
    return (
        "Budget Travel Tips:\n"
        "- Travel off-season\n"
        "- Use public transport\n"
        "- Book budget hotels\n"
        "- Avoid tourist traps"
    )

def guideline_help():
    return (
        "Travel Guidelines:\n"
        "- Keep documents secure\n"
        "- Respect local laws\n"
        "- Carry insurance\n"
        "- Stay aware of surroundings"
    )

def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOP_WORDS]
    return tokens

def stem(word):
    for suffix in ["ing", "ed", "s"]:
        if word.endswith(suffix) and len(word) > 4:
            return word[:-len(suffix)]
    return word
