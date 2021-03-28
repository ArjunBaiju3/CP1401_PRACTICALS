"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    import random
    score = (random.randint(0, 101))
    print("Score =", score)
    print(check_rank(score))

def check_rank(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()