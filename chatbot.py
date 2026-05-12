print("Hello! Welcome! 👋")
print("You can ask me everything about Sunset Restaurant, such as:")
print("- our opening hours")
print("- where we are located")
print("- our dishes like pizza, grill and pasta")
print("- how to place an order")
print("- food prices and much more info\n")

print("Type 'exit' to close the chatbot.\n")

restaurant_info = {
    "opening hours": "Sunset Restaurant is open every day from 10:00 AM to 10:00 PM.",
    "location": "We are located in the city center, near the main square.",
    "pizza": "We serve many types of pizza, including Margherita, Pepperoni, and BBQ Chicken.",
    "pasta": "Our pasta dishes include Carbonara, Bolognese, and Alfredo.",
    "grill": "We offer grilled dishes like burgers, steak, and grilled chicken.",
    "order": "You can place an order by visiting our restaurant or calling us directly.",
    "prices": "Our meals range from $8 to $25 depending on the dish."
}

while True:
    msg = input("You: ").lower()

    if msg == "exit":
        print("Bot: Goodbye! Have a nice day 🍽️")
        break

    elif "opening" in msg or "hours" in msg:
        print("Bot:", restaurant_info["opening hours"])

    elif "where" in msg or "location" in msg or "place" in msg:
        print("Bot:", restaurant_info["location"])

    elif "pizza" in msg:
        print("Bot:", restaurant_info["pizza"])

    elif "pasta" in msg:
        print("Bot:", restaurant_info["pasta"])

    elif "grill" in msg or "burger" in msg:
        print("Bot:", restaurant_info["grill"])

    elif "order" in msg:
        print("Bot:", restaurant_info["order"])

    elif "price" in msg:
        print("Bot:", restaurant_info["prices"])

    else:
        print("Bot: Please ask something about our restaurant 🍽️")