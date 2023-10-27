def sms_handler(notification):
    
    print("------------------ SMS Notification -------------------")
    print(f"From: {notification['sender']}")
    print(f"To: {notification['receiver']}")
    print(f"Body: {notification['body']}")
    print("---------------------------------------------------------")
