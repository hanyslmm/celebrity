import create_page
import head
"""creates 5 celebrities profile objects, intialising these objects with
full name, birthdate and poster link."""
hany = ("Hany Salama", "19900831", "https://scontent-cai1-1.xx.fbcdn.net/v/t1.0-9/40914288_1871203486267207_6454440147638288384_o.jpg?_nc_cat=103&_nc_ht=scontent-cai1-1.xx&oh=f7d4daaa013b74b1c2180645823dfd24&oe=5C57EA9F")
emma = ("Emma Watson", "19900415", "https://upload.wikimedia.org/wikipedia/commons/7/7f/Emma_Watson_2013.jpg")
helmy = ("Ahmed Helmy", "19691118", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Ahmed_Helmy_conf2018.jpg/800px-Ahmed_Helmy_conf2018.jpg")
jennifer =  ("Jennifer Lawrence", "19900815", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Jennifer_Lawrence_SDCC_2015_X-Men.jpg/800px-Jennifer_Lawrence_SDCC_2015_X-Men.jpg")
anniston = ("Jennifer Aniston", "19690211", "https://upload.wikimedia.org/wikipedia/commons/1/16/JenniferAnistonHWoFFeb2012.jpg")
profiles = [hany, emma, helmy, jennifer, anniston]

# Store the profile object in a list called users
users = profiles
i = 0
for profile in profiles:
    users[i] = head.User(profile[0], profile[1], profile[2])
    i += 1
# Open the movie website in the user's browser, featuring the movies above.
create_page.create_profile_page(users)
# print function to test the program in terminal
def main():
    for user in users:
        print("{} age is {} , url = {}".format(user.name, user.age(), user.poster))
if __name__ == "__main__":
    main()
