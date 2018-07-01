def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be of type boolean")
    health = "is healthy" if is_healthy else "is not healthy"
    return f"{food.capitalize()} {health}."


def nap(num_hours):
    if num_hours < 3:
        return f"I'm feeling refreshed after my {num_hours} hour nap."
    else:
        return f"Crap, I didn't mean to sleep {num_hours} hours."
