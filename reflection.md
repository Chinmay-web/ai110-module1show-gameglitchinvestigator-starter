# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

**Bug 1: New Game doesn't actually restart the game**
I ran out of attempts, then clicked New Game. I expected a fresh game, but the red "Game over" message stayed and I couldn't guess anymore. The new_game block in app.py resets attempts and the secret, but never resets status back to "playing".

**Bug 2: Score and history carry over into the new game**
After clicking New Game, my score was still -30 and all my old guesses were still in the history. They should have reset to 0 and empty. Same new_game block in app.py.

**Bug 3: Invalid input still uses up an attempt**
I typed "thirty". It said "That is not a number," but it still counted as an attempt and was added to history. In app.py, `attempts += 1` runs before `parse_guess` checks the input.

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|---|---|---|---|---|
| Lost the game, clicked New Game | Fresh game starts | "Game over" message stays, can't guess | none | app.py, `if new_game:` block (status not reset) |
| Clicked New Game with score -30 | Score resets to 0, history clears | Score still -30, old guesses still shown | none | app.py, `if new_game:` block |
| Typed "thirty" | Rejected without using an attempt | Error shown but attempt used and added to history | "That is not a number." | app.py, submit block (`attempts += 1` before `parse_guess`) 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I asked Claude why New Game still showed "Game over." It correctly explained that the new_game block resets attempts and secret but never sets status back to "playing", so the game-over check calls st.stop() on every rerun. I verified this by reading app.py. Its suggested fix sets attempts = 1, but I think that keeps an existing off-by-one bug (a fresh game shows 7 attempts left instead of 8), so I'd reset attempts to 0 instead.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
