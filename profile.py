import create_page
import head
"""creates 5 celebrities profile objects, intialising these objects with
full name, birthdate and poster link."""
hany = ("Hany Salama", "19900831", "https://scontent-cai1-1.xx.fbcdn.net/v/t1.0-9/10348271_696664510387783_5463587020847519050_n.jpg?_nc_cat=106&_nc_ht=scontent-cai1-1.xx&oh=818b86469b274e33d2f5a320a97f5c16&oe=5C4C317A", "You might think you’re not good enough, but you’ll surprise yourself if you keep trying.  Your past does not determine who you are. Your past prepares you for who you are capable of becoming.")
adele = ("Adele Laurie", "19880505", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Adele_2016.jpg/800px-Adele_2016.jpg", "There’s only one of you, so why would you want to look like everyone else? Why would you want to have the same hairstyle as everyone else and have the same opinions as everybody else?")
emma = ("Emma Watson", "19900415", "https://upload.wikimedia.org/wikipedia/commons/7/7f/Emma_Watson_2013.jpg", "I like books that aren't just lovely but that have memories in themselves. Just like playing a song, picking up a book again that has memories can take you back to another place or another time.")
helmy = ("Ahmed Helmy", "19691118", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Ahmed_Helmy_conf2018.jpg/800px-Ahmed_Helmy_conf2018.jpg", "kolna makhlo2en mn torab mfesh torab markat wallahy!")
jennifer =  ("Jennifer Lawrence", "19900815", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Jennifer_Lawrence_SDCC_2015_X-Men.jpg/800px-Jennifer_Lawrence_SDCC_2015_X-Men.jpg", "I never think it's right to chew gum in front of other people, but a lot of times I'll come in for a meeting chewing gum and I'll forget I'm chewing it. Then you don't want to swallow it because it stays in your system for seven years or something, so I've asked to throw it away. I've started to wonder if that's why I didn't get certain movies.")
anniston = ("Jennifer Aniston", "19690211", "https://upload.wikimedia.org/wikipedia/commons/1/16/JenniferAnistonHWoFFeb2012.jpg", "The greater your capacity to love, the greater your capacity to feel the pain.")
profiles = [hany, adele, jennifer, helmy, emma, anniston]

# Store the profile object in a list called users
users = profiles
i = 0
for profile in profiles:
    users[i] = head.User(profile[0], profile[1], profile[2], profile[3])
    i += 1
# Open the movie website in the user's browser, featuring the movies above.
create_page.create_profile_page(users)
# print function to test the program in terminal
def main():
    for user in users:
        print("{} age is {} , url = {}".format(user.name, user.age(), user.poster))
if __name__ == "__main__":
    main()
