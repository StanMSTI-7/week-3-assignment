"""Conversation memory: a list of dicts that grows by one message at a time."""

SYSTEM = "You are a concise helpdesk assistant."
RECENT = 6  # messages sent after the system message (3 user/assistant exchanges)


def new_history():
    """Start a conversation. It holds only the system message."""
    return [{"role": "system", "content": SYSTEM}]


def add_turn(history, role, content):
    """Save one message at the end of the history."""
    history.append({"role": role, "content": content})


def request_messages(history):
    """The messages actually sent to the reply backend: the system message plus the last RECENT."""
    return history[:1] + history[1:][-RECENT:]
