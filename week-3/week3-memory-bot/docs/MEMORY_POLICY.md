# Memory policy

The model has a limited context window, so a long conversation cannot be sent whole.
Decide what `request_messages()` sends when the history gets long.

- Policy (one sentence, e.g. "the system message plus the last 4 turns"):
  `request_messages()` sends the system message plus the last 6 messages (3 user/assistant exchanges), so at most 7 messages.
- What is dropped first, and why:
  The oldest user and assistant messages are dropped first. The system message is always kept because it sets how the bot behaves, and the newest messages are kept because the latest question is usually about them.
- A question the bot will then get wrong. Write the exact conversation:
  ```text
  you > My name is Ada
  bot > Nice to meet you, Ada.
  you > hello
  bot > Noted. Ask 'What is my name?' to test my memory.
  you > thanks
  bot > Noted. Ask 'What is my name?' to test my memory.
  you > What is my name?
  bot > I do not know your name yet.
  ```
  When the question is sent, there are 7 messages after the system message. Only the last 6 are sent, so `My name is Ada` is cut off. With only one message (`hello`) in between, the bot still answers `Your name is Ada.`
- Implemented or proposed only:
  Implemented in `memory.py` (`RECENT = 6`). Checked by `test_request_keeps_system_message_and_recent_turns`.

## The test that encodes the policy

Copy this into `tests/test_memory.py`, replace the TODOs, and run `python -m pytest`.
It is fine if it is red when you leave; the policy is the deliverable.

```python
def test_request_keeps_system_message_and_recent_turns():
    history = new_history()
    for number in range(10):
        add_turn(history, "user", f"message {number}")
        add_turn(history, "assistant", f"reply {number}")
    sent = request_messages(history)
    assert sent[0]["role"] == "system"
    assert len(sent) <= TODO            # system message + how many recent messages?
    assert sent[-1] == history[-1]      # the newest message is always sent
```
