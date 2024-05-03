def is_valid_input(value):
    try:
        float(value)
        return True
    except:
        return False

def prompt_input(message, error_message):
    while True:
        user_input = input(message)
        if is_valid_input(user_input):
            return float(user_input)
        else:
            print(error_message)