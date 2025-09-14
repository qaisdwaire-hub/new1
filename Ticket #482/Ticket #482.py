user_name = input("Name? ").strip()
mood = input("Payment method? (card/cash): ").strip().lower()
if mood == "card":
 print("Processing...")
else:
 message = "Cash accepted"
