def whatsapp_handler(notification):
    
    print("------------------ Whatsapp Notification -------------------")
    print(f"From: {notification['sender']}")
    print(f"To: {notification['receiver']}")
    print(f"Body: {notification['body']}")
    print("---------------------------------------------------------")
