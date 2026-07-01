# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. **Launch the app.** Run `python -m streamlit run app.py` and open the page in your browser. You'll see the "🎮 Game Glitch Investigator" title and a "Make a guess" section.
2. **Pick a difficulty.** In the sidebar, choose Easy (1–20), Normal (1–100), or Hard (1–50). The sidebar shows the current range and how many attempts you're allowed.
3. **Peek at the secret (optional).** Expand "Developer Debug Info" to see the secret number, your attempt count, and score — handy for confirming the game now behaves correctly.
4. **Enter a guess.** Type a number in the "Enter your guess:" box and click "Submit Guess 🚀".
5. **Read the hint.** With "Show hint" checked, the game tells you "📈 Go HIGHER!" or "📉 Go LOWER!" — and these are now correct on every attempt, including even-numbered ones (the string/number comparison bug is fixed).
6. **Keep guessing.** Follow the hints toward the secret. Your attempts-left counter ticks down and your score updates after each guess.
7. **Win the game.** Guess the secret exactly and the game shows balloons 🎉, reveals the secret, and displays your final score. The secret stays fixed across submissions (no more resetting on every click).
8. **Start over.** Click "New Game 🔁" to reset the secret, attempts, and board for another round.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
