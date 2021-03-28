"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = float(input("Enter score: "))
    print(check_rank(score))

def check_rank(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()