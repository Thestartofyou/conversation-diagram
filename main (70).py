import networkx as nx
import matplotlib.pyplot as plt

# Define the conversation as a list of messages
conversation = [
    {"sender": "Alice", "text": "Hi Bob, how are you?"},
    {"sender": "Bob", "text": "I'm doing well, thanks for asking. How about you?"},
    {"sender": "Alice", "text": "I'm doing pretty good too."},
    {"sender": "Bob", "text": "That's great to hear!"},
    {"sender": "Alice", "text": "So, I wanted to talk to you about something."},
    {"sender": "Bob", "text": "Sure, go ahead."},
    {"sender": "Alice", "text": "Well, I noticed that you've been canceling our plans a lot lately."},
    {"sender": "Bob", "text": "Yeah, I'm sorry about that. Work has been really busy."},
    {"sender": "Alice", "text": "I understand that, but it's been happening a lot. I feel like you don't prioritize our friendship anymore."},
    {"sender": "Bob", "text": "I'm really sorry, Alice. You're right, I haven't been making as much time for our friendship as I should be. I'll try to do better."},
    {"sender": "Alice", "text": "Thanks, Bob. I appreciate it."},
    {"sender": "Bob", "text": "Of course. You're a great friend, and I don't want to lose that."},
    {"sender": "Alice", "text": "Neither do I."},
]

# Create a directed graph to represent the conversation
G = nx.DiGraph()

# Add each message as a node in the graph
for i, message in enumerate(conversation):
    G.add_node(i, text=message["text"], sender=message["sender"])

# Add edges between the nodes to represent the flow of the conversation
for i in range(len(conversation) - 1):
    G.add_edge(i, i + 1)

# Set the position of each node in the graph
pos = {i: (0, i) for i in range(len(conversation))}

# Draw the graph
nx.draw_networkx(G, pos=pos, labels={i: conversation[i]["sender"] + ": " + conversation[i]["text"] for i in range(len(conversation))})
plt.show()

# Prompt the user to rate the conversation
rating = input("How would you rate this conversation on a scale of 1-10? ")

# Print the rating
print("You rated the conversation a", rating)

