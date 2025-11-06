def exit_function():
    total = 0
    count = 0
    for i in range(10):
        count += 1
        total += i
        if total > 5:
            return f"The count {count} and the total is {total}."
print(exit_function())
