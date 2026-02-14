# session-12
A simple Number Guessing Game built with Python where players try to guess a randomly generated number with limited attempts based on difficulty level.
# 🎯 Guess The Number Game (Python)

## 📖 Overview

This is a simple Number Guessing Game built using Python.

The computer randomly selects a number between 1 and 100.  
The player must guess the number within a limited number of attempts based on the selected difficulty level.

---

## 🎮 Game Features

- Random number generation (1–100)
- Two difficulty levels:
  - Easy → 10 attempts
  - Hard → 5 attempts
- Feedback system:
  - Too high
  - Too low
  - Correct answer
- Win / Lose condition system
- Clean and simple game loop

---

## 🧠 Concepts Used

- Functions
- While loops
- Conditional statements
- Random module
- User input handling
- Game logic management

---

## ⚙️ How the Game Works

1. The computer randomly generates a number between 1 and 100.
2. The player selects a difficulty level.
3. The player guesses the number.
4. The game gives feedback:
   - If the guess is too high
   - If the guess is too low
   - If the guess is correct
5. The game ends when:
   - The player guesses correctly
   - The player runs out of attempts

---

## 💻 Full Code

```python
import random


def check_answer(user_guess, answer_guess):
    if user_guess < answer_guess:
        print("Jawaban anda terlalu rendah.")
        return False
    elif user_guess > answer_guess:
        print("Jawaban anda terlalu tinggi.")
        return False
    else:
        print(f"Jawaban anda benar! Angka yang dipilih adalah {answer_guess}")
        return True


def set_difficulty():
    level = input("Kamu mau pilih 'easy' atau 'hard'?: ").lower()
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Pilihan tidak valid, otomatis pilih easy.")
        return 10


print("🎯 Selamat datang di Guess The Number!")
print("Aku sedang memikirkan angka dari 1 sampai 100.")

angka_acak = random.randint(1, 100)
turns = set_difficulty()

game_over = False

while turns > 0 and not game_over:
    print(f"\nSisa kesempatan menebakmu: {turns}")
    guess = int(input("Tebak angkanya: "))

    is_correct = check_answer(guess, angka_acak)

    if is_correct:
        game_over = True
    else:
        turns -= 1

if turns == 0 and not game_over:
    print(f"\nKesempatan habis! Kamu kalah 😢")
    print(f"Angka yang benar adalah {angka_acak}")
```

---

## 🛠 Requirements

- Python 3.x

---

## 👤 Author

Andrian Wijaya

---

## 📜 License

This project is created for learning and educational purposes.
