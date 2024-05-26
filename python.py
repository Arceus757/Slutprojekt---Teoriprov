# Slutprojekt 
from colours import bcolors

# Lista med frågor om Tom och Jerry
questions = (bcolors.DEFAULT + "Who is the main antagonist in Tom and Jerry?:",
            bcolors.DEFAULT +"What is the primary setting for most Tom and Jerry episodes?:",
            bcolors.DEFAULT +"Which character is known for his cleverness and ability to outsmart Tom?:",
            bcolors.DEFAULT +"What is the typical outcome of Tom's attempts to catch Jerry?:",
            bcolors.DEFAULT +"Who is Tom's owner and often scolds him for his failures?:",
            bcolors.DEFAULT +"What type of animal is Jerry?:",
            bcolors.DEFAULT +"Which character is known for being bigger and often protects Jerry from Tom's attacks?:",
            bcolors.DEFAULT +"What is the primary method Tom uses to try to catch Jerry?:" )

# Alternativ för varje fråga
options = (("A. Spike", "B. Jerry", "C. Tom", "D. Butch"), 
            ("A. A farm", "B. A city", "C. A forest", "D. A desert"),
            ("A. Spike", "B. Jerry", "C. Tom", "D. Butch"),
            ("A. He catches Jerry", "B. He fails", "C. He gets hurt", "D. He gets rewarded"),
            ("A. Spike", "B. Jerry", "C. Tom", "D. Butch"),
            ("A. Mouse", "B. Cat", "C. Dog", "D. Bird"),
            ("A. Spike", "B. Jerry", "C. Tom", "D. Butch"),
            ("A. Traps", "B. His claws", "C. His teeth", "D. His speed"))



answers = ("C", "B", "B", "B", "C", "A", "A", "A") # Korrekta svar för varje fråga
quesses = [] # Lista för användarens gissningar
score = 0 # Variabel för poäng
questions_num = 0  # Variabel för att hålla koll på vilken fråga som är aktuell

# Loopar igenom varje fråga
for question in questions:
    print(":+:-:+:-" * 8) # Skriver ut en rad med plus-tecken för att separera frågorna 
    print(question)
    for option in options[questions_num]:
        print(option)

    guess = input ("Enter (A, B, C, D):" + bcolors.CYAN).upper()  # Tar in användarens gissning och konverterar till versaler
    quesses.append(guess)
    if guess == answers[questions_num]: # Om gissningen är korrekt ökar poängen och skriver ut "Correct!"
        score += 1
        print(bcolors.GREEN + "Correct!")
    else: # Annars om gissningen är felaktig, skriver ut "Incorrect!" 
        print(bcolors.RED + "Incorrect! The correct answer is: ", answers[questions_num])
    questions_num += 1


print(bcolors.DEFAULT + ":+:-:+:-" * 5) 
print(bcolors.YELLOW + "              RESULTS           ")
print(bcolors.DEFAULT + ":+:-:+:-" * 5)


print(bcolors.CYAN + " answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print(" answers: ", end="")
for guess in quesses:
    print(answer, end="")
print()

# Beräknar poängen som en procentandel och skriver ut den 
score = int(score / len(questions) * 100)
print(f" Your score is: {score}%")