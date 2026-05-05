🗺️ State Guessing Game

A Python game where you guess states and see them appear on a map.
This project uses pandas for data handling and turtle for visual display.

🎮 Features
Guess states and see them appear on the map
Score tracking (e.g. 10/50 States Correct)
Type "Exit" to end the game early
Generates a CSV file of missed states
Prevents duplicate guesses
Safe input handling (no crashes on Cancel)

🧠 What I Learned
Working with CSV data using pandas
Reading data from files
Filtering rows
Extracting specific values

▶️ How to Run
Install Python
Install pandas
Run: main.py

🔮 Future Improvements
🌍 Add support for other countries (Nigeria version coming 👀)

🧠 List Comprehension — Understanding new_item

new_item is simply what you want inside your final list.

💡 Key Idea

Think about the result first, not the syntax.

🧠 Example

If you want:

missing_states = ["Texas", "Ohio", ...]

Then:

👉🏾 new_item = state

🎯 Code

[state for state in all_states if state not in guessed_states]

✅ Simple Rule
No change → new_item = item
Change needed → new_item = modified item
🚀 Takeaway

Focus on what you want in the list — that defines new_item.