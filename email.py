class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
info = input()

while info != "Stop":
    sender, reciever, content = info.split()
    email = Email(sender, reciever, content)
    emails.append(email)
    info = input()
send_emails = list(map(int, input().split(", ")))

for x in send_emails:
    emails[x].send()
for emai in emails:
    print(emai.get_info())
