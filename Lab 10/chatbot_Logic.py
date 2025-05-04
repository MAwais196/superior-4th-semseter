def process_message(message):
    if not message or not isinstance(message, str):
        return "Could you please repeat your question?"
    
    message = message.lower()
    
    # Simple keyword matching
    if any(w in message for w in ["hi", "hello", "hey"]):
        return "Hello! How can I help with your university admission questions?"
    elif "requirement" in message:
        return "Our general requirements include: High school diploma, minimum GPA of 3.0."
    elif "deadline" in message:
        return "The application deadline is January 15th for Fall admission."
    elif "program" in message:
        return "We offer programs in Engineering, Business, and Arts."
    else:
        return "I'm not sure I understand. Could you ask about admission requirements, deadlines, or programs?"