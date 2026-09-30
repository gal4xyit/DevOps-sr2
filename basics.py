def print_text(text):
    print(text)


print_text("Hello!")

def print_case_info(text):
    if text.isupper():
        print("Усі літери великі")
    elif text.islower():
        print("Усі літери малі")
    elif text.lower() != text.upper():
        print("Регістр літер змішаний")
    else:
        print("У рядку немає літер із регістром")


print_case_info("HELLO")
print_case_info("hello")
print_case_info("Hello")
print_case_info("123!")

word = "smogtether"

uppercase_letters = list(map(lambda letter: letter.upper(), word))

print(uppercase_letters)

def parity_generator():
    while True:
        yield "Парне"
        yield "Непарне"


labels = parity_generator()

for _ in range(6):
    print(next(labels))