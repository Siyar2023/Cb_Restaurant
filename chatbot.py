print("🤖 Barcelona Chatbot startad! 🔵🔴")
print("Du kan fråga mig om Barcelona.")
print("Exempel på frågor:")
print("- stad")
print("- väder")
print("- turism")
print("- fotboll / FC Barcelona")
print("- Camp Nou")
print("\nSkriv 'exit' för att avsluta\n")

barcelona_info = {
    "stad": "Barcelona är en stor stad i Spanien och huvudstad i Katalonien.",
    "väder": "Barcelona har medelhavsklimat med varma somrar och milda vintrar.",
    "turism": "Populära platser är Sagrada Familia, Park Güell och La Rambla.",
    "fotboll": "FC Barcelona spelar på Camp Nou och är en av världens största klubbar.",
    "camp nou": "Camp Nou är FC Barcelonas hemmaarena och en av Europas största arenor."
}

while True:
    msg = input("\nDu: ").lower()

    if msg == "exit":
        print("Bot: Hej då! Visca Barça 🔵🔴")
        break

    elif "hej" in msg:
        print("Bot: Hej! Fråga mig om Barcelona 😊")

    elif "stad" in msg:
        print("Bot:", barcelona_info["stad"])

    elif "väder" in msg:
        print("Bot:", barcelona_info["väder"])

    elif "turism" in msg or "resa" in msg:
        print("Bot:", barcelona_info["turism"])

    elif "fotboll" in msg or "barça" in msg:
        print("Bot:", barcelona_info["fotboll"])

    elif "camp nou" in msg:
        print("Bot:", barcelona_info["camp nou"])

    else:
        print("Bot: Jag förstår inte riktigt 🤔 Försök fråga om stad, väder, turism eller fotboll.")