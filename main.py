def Check_answer(user_guess,answer_guess):
    if user_guess < answer_guess:
        print("jawaban anda terlalu rendah")
    elif user_guess > answer_guess:
        print("jawaban anda terlalu tinggi")
    elif user_guess == answer_guess:
        print(f"jawaban anda benar, karena computer memilih angka{angka_acak}")

def Set_Difficulty():
    level = input("kamu mau milih easy atau hard?:").lower()
    global turns
    if level == "easy":
        return easy
    elif level == "hard":
        return hard


import random
print("Selamat datang di Guess The Number")
print("tebak aku memikirkan angka berapa dari 1-100!!!")
tebak = input("tebak angka berapa dari 1-100")
angka_acak = random.randint (1,100)

#step3
turns = Set_Difficulty()
easy  = 10
hard  = 5
print(f"Sisa kesempatan menebakmu:{turns}")



















































