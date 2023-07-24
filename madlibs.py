def spiderman_madlib():
    # Get user input for various parts of the madlib story
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    noun4 = input("Noun: ")
    noun5 = input("Noun: ")
    noun6 = input("Noun: ")
    verb = input("Verb: ")
    verb_past = input("Verb (past tense): ")
    verb_past2 = input("Verb (past tense): ")
    spider_verb = input("Verb (related to spiders): ")
    place = input("Place: ")

    # Construct the madlib story using the user-provided words
    madlib = f"Swinging through the {place} as {adj1} as a spider, {noun1}, also known as Spider-Man, \
uses his {adj2} {noun2} to {verb} crime and protect the innocent. With his {adj3} spider-like senses, he can \
detect danger from miles away, making him the {adj4} defender of {place}.\n\
In one of his recent adventures, Spider-Man faced off against his arch-nemesis, {noun3}, a {noun4} \
scientist turned evil. The {noun3}'s sinister plan involved using a powerful {noun5} to take control of \
the city. As the city's safety hung in the balance, Spider-Man swung into action, {spider_verb} the walls \
of buildings, and {verb_past} with incredible acrobatics.\n\
The final showdown took place atop a towering {noun6}, and after an intense battle, Spider-Man \
{verb_past2} the {noun3}, foiling his evil scheme and saving the day once again.\n\
With great power comes great responsibility, and Spider-Man continues to be the {adj4} hero that inspires us all."

    # Display the completed madlib story to the user
    print(madlib)

if __name__ == '__main__':
    # Execute the spiderman_madlib function when the script is run
    spiderman_madlib()
