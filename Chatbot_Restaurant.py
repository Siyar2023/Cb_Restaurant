print("🌟 Welcome to Sunset Restaurant Assistant 🍽️")
print("Ask me about location, menu, prices, ordering, delivery, contact or kids menu.\n")

print("Type 'exit' to close the chatbot.\n")

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

while True:
    msg = input("You: ").lower()

    if msg == "exit":
        print("Bot: Goodbye! 🍽️ See you soon.")
        break

    # 👋 Greetings
    elif any(word in msg for word in ["hello", "hi", "hey"]):
        print("Bot: 🌟 Hello! Welcome to Sunset Restaurant. How can I help you?")

    # 📍 Location
    elif any(word in msg for word in ["where", "location", "address"]):
        print("Bot:", info["location"])

    # 🕒 Hours
    elif any(word in msg for word in ["open", "hours", "time"]):
        print("Bot:", info["hours"])

    # 👨‍👩‍👧‍👦 KIDS MENU (VIKTIGT: före menu)
    elif any(word in msg for word in ["kids menu", "children menu", "kids", "children", "child"]):
        print("Bot:", info["kids"])

    # 🍕 Pizza price (specifik först)
    elif "pizza" in msg and any(word in msg for word in ["price", "cost", "how much"]):
        print("Bot:", info["pizza_price"])

    # 🍕 Pizza
    elif "pizza" in msg:
        print("Bot:", info["pizza"])

    # 🍝 Pasta
    elif "pasta" in msg:
        print("Bot:", info["pasta"])

    # 🍔 Burgers
    elif any(word in msg for word in ["burger", "grill", "steak"]):
        print("Bot:", info["burgers"])

    # 💰 Prices
    elif any(word in msg for word in ["price", "cost", "expensive", "how much"]):
        print("Bot:", info["prices"])

    # 🍽️ Menu (efter kids!)
    elif any(word in msg for word in ["menu", "food", "eat", "serve"]):
        print("Bot:", info["menu"])

    # 🛒 Order
    elif any(word in msg for word in ["order", "buy", "takeaway"]):
        print("Bot:", info["order"])

    # 🚗 Delivery
    elif any(word in msg for word in ["delivery", "deliver"]):
        print("Bot:", info["delivery"])

    # 📞 Contact
    elif any(word in msg for word in ["phone", "number", "contact"]):
        print("Bot:", info["phone"])

    # ⭐ Recommendation
    elif any(word in msg for word in ["recommend", "best", "popular"]):
        print("Bot:", info["recommend"])

    # 🥗 Vegetarian
    elif any(word in msg for word in ["vegetarian", "vegan"]):
        print("Bot:", info["vegetarian"])

    # 🙏 Thanks
    elif any(word in msg for word in ["thanks", "thank you", "thx"]):
        print("Bot: 😊 You're welcome! Let me know if you need anything else.")

    # ❓ Fallback
    else:
        print("Bot: 🤔 I didn't fully understand that.")
        print("Bot: Try asking about menu, location, prices, ordering or kids menu.")