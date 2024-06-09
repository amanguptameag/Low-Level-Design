from stack_overflow import StackOverflow


if __name__ == "__main__":
    stack_overflow = StackOverflow()

    stack_overflow.add_user("Aman")
    stack_overflow.add_user("Sayta")

    stack_overflow.add_question("Aman", "My Question", ["My Tag"])

    stack_overflow.add_answer("Sayta", "My Question", "my answer")

    feeds = stack_overflow.get_feeds("My Tag")

    print(feeds)
