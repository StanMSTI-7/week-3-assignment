# History trace

Predict first, then check with `/show`. One row per line typed.

| Input | Predicted `history` after this line | Observed with `/show` | Match? |
|---|---|---|---|
| `My name is Ada` | `Hello Ada` | `Nice to meet you, Ada.`  | `not a match` |
| `What is my name?` | `your name is Ada` |`I do not know your name yet.` | `not a match`|`
| `/show` | `chat history` | `chat history`|`Match`  |
| `/reset` |`clear history` | `Conversation Reset`| `match`|

- What `/show` prints is the **stored** list. What `reply()` receives is the **sent** list. Are they the same? How did you check?


- The one line that explains the incident:
1. FAILED tests/test_memory.py::test_backend_receives_the_whole_history - AssertionError: assert [{'role': 'as...t you, Ada.'}] == [{'role': 'sy...t you, Ada.'}]
2. FAILED tests/test_memory.py::test_bot_recalls_a_name_from_an_earlier_turn - AssertionError: assert 'I do not know your name yet.' == 'Your name is Ada.'
3. FAILED tests/test_memory.py::test_command_with_trailing_space_still_works - assert 5 == 3
4. FAILED tests/test_memory.py::test_reset_keeps_the_system_message - AssertionError: assert [] == [{'role': 'sy... assistant.'}]