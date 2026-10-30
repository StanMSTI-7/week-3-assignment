# History trace

Predict first, then check with `/show`. One row per line typed.

| Input | Predicted `history` after this line | Observed with `/show` | Match? |
|---|---|---|---|
| `My name is Ada` | `[system, user "My name is Ada", assistant "Nice to meet you, Ada."]` (3 dicts) | `[system, user "My name is Ada", assistant "Nice to meet you, Ada."]` (3 dicts) | Yes |
| `What is my name?` | 5 dicts: the 3 above + `user "What is my name?"`, `assistant "Your name is Ada."` | 5 dicts: the 3 above + `user "What is my name?"`, `assistant "I do not know your name yet."` | No: the name is stored but the reply says it is not known |
| `/show` | Unchanged, still 5 dicts (`/show` only prints) | Unchanged, 5 dicts | Yes |
| `/reset` | `[system]` (1 dict, a fresh conversation) | `[]`: `/show` afterwards prints nothing, even the system message is gone | No (this is Issue 3) |

- What `/show` prints is the **stored** list. What `reply()` receives is the **sent** list. Are they the same? How did you check?
  No. When `What is my name?` is sent, the stored list has 4 dicts (system, user, assistant, user), but `request_messages(history)` returns only `[{"role": "user", "content": "What is my name?"}]`. We checked by calling `request_messages()` on the stored history in a Python shell, and with the red test `test_backend_receives_the_whole_history`, whose diff shows the sent list is 1 item while the stored list is 3. `find_name()` never sees `My name is Ada`, so `reply()` answers `I do not know your name yet.`
- The one line that explains the incident:
  `memory.py` line 18: `return history[-1:]`. It sends only the last message to `reply()` instead of the whole history.
