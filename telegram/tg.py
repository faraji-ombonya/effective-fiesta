def telegram_handler(notification):
    
    print("------------------ Telegram  Notification -------------------")
    print(f"From: {notification['sender']}")
    print(f"To: {notification['receiver']}")
    print(f"Body: {notification['body']}")
    print("---------------------------------------------------------")
