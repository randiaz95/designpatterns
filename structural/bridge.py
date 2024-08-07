from abc import ABC, abstractmethod

# A Bridge requires two parts: an abstraction and an implementation.
# The Bridge pattern breaks the abstraction and implementation into separate class hierarchies.
class Message:
    def __init__(self, sender):
        self.sender = sender

    def send(self, recipient, content):
        self.sender.send(recipient, content)

# The abstraction is the interface that the client uses.
# The implementation is the concrete class that the abstraction uses.
class MessageSender(ABC):
    @abstractmethod
    def send(self, recipient, content):
        pass


class InstantMessageSender(MessageSender):
    def send(self, recipient, content):
        print(f"Sending instant message to {recipient}: {content}")


class ScheduledMessageSender(MessageSender):
    def send(self, recipient, content):
        print(f"Message to {recipient} scheduled: {content}")


class TextMessage(Message):
    def send(self, recipient, content):
        print("Sending text message...")
        super().send(recipient, content)


class EmailMessage(Message):
    def send(self, recipient, content):
        print("Sending email message...")
        super().send(recipient, content)


if __name__ == "__main__":
    instant_sender = InstantMessageSender()
    scheduled_sender = ScheduledMessageSender()

    text_message = TextMessage(instant_sender)
    email_message = EmailMessage(scheduled_sender)

    text_message.send("John Doe", "Hello, John! This is an instant text message.")
    email_message.send("Jane Smith", "Hi Jane, your scheduled email message will be sent soon.")