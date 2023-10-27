def email_handler(notification):
    
    print("------------------ Email Notification -------------------")
    print(f"From: {notification['sender']}")
    print(f"To: {notification['receiver']}")
    print(f"Body: {notification['body']}")
    print("---------------------------------------------------------")
