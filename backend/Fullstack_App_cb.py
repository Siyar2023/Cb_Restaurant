# 📦 Restaurant knowledge base
info = {
    "location": "📍 We are located in the city center near the main square.",
    "hours": "🕒 We are open every day from 10:00 AM to 10:00 PM.",
    "menu": "🍽️ We serve pizza, pasta, burgers, steak, salads and drinks.",
    "pizza": "🍕 Pizza: Margherita, Pepperoni, BBQ Chicken, Vegetarian.",
    "pizza_price": "🍕 Pizza costs around $10 - $15 depending on type.",
    "pasta": "🍝 Pasta: Carbonara, Bolognese, Alfredo.",
    "burgers": "🍔 Burgers: Classic, Chicken, Cheese burger.",
    "prices": "💰 Prices range from $8 to $25 depending on dish.",
    "order": "🛒 You can order in restaurant, takeaway or by phone.",
    "delivery": "🚗 We offer delivery in selected areas (30-45 min).",
    "phone": "📞 Customer service: 0011223344",
    "recommend": "⭐ We recommend BBQ Chicken pizza and Carbonara pasta.",
    "vegetarian": "🥗 We have vegetarian and vegan options.",
    "kids": "👨‍👩‍👧‍👦 Kids menu includes mini pizza, chicken nuggets, pasta and juice."
}

# 🤖 Chatbot function
def chatbot_response(msg):

    msg = msg.lower()

    if any(word in msg for word in ["hello", "hi", "hey"]):
        return "🌟 Hello! Welcome to Sunset Restaurant. How can I help you?"

    elif any(word in msg for word in ["where", "location", "address"]):
        return info["location"]

    elif any(word in msg for word in ["open", "hours", "time"]):
        return info["hours"]

    elif any(word in msg for word in ["kids menu", "children menu", "kids", "children", "child"]):
        return info["kids"]

    elif "pizza" in msg and any(word in msg for word in ["price", "cost", "how much"]):
        return info["pizza_price"]

    elif "pizza" in msg:
        return info["pizza"]

    elif "pasta" in msg:
        return info["pasta"]

    elif any(word in msg for word in ["burger", "grill", "steak"]):
        return info["burgers"]

    elif any(word in msg for word in ["price", "cost", "expensive", "how much"]):
        return info["prices"]

    elif any(word in msg for word in ["menu", "food", "eat", "serve"]):
        return info["menu"]

    elif any(word in msg for word in ["order", "buy", "takeaway"]):
        return info["order"]

    elif any(word in msg for word in ["delivery", "deliver"]):
        return info["delivery"]

    elif any(word in msg for word in ["phone", "number", "contact"]):
        return info["phone"]

    elif any(word in msg for word in ["recommend", "best", "popular"]):
        return info["recommend"]

    elif any(word in msg for word in ["vegetarian", "vegan"]):
        return info["vegetarian"]

    elif any(word in msg for word in ["thanks", "thank you", "thx"]):
        return "😊 You're welcome! Let me know if you need anything else."

    else:
        return "🤔 I didn't fully understand that. Try asking about menu, location, prices, ordering or kids menu."