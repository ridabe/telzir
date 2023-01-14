def calculate_without_plan(time, price):
    result = price * float(time)
    return result


def calculate_surplus(time, plan):
    result = int(time) - int(plan)
    return result


def calculate_indemnity(price):
    result = price * 1.10
    return result

def calculate_with_plan(surplusMin, indemnityPrice):
    result = indemnityPrice * float(surplusMin)
    return result
