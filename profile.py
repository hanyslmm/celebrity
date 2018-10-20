import head
hany = ("Hany Salama", "19900831", "https://scontent-cai1-1.xx.fbcdn.net/v/t1.0-9/40914288_1871203486267207_6454440147638288384_o.jpg?_nc_cat=103&_nc_ht=scontent-cai1-1.xx&oh=f7d4daaa013b74b1c2180645823dfd24&oe=5C57EA9F")
emma = ("Emma Watson", "19900415", "https://en.wikipedia.org/wiki/Emma_Watson#/media/File:Emma_Watson_2013.jpg")
helmy = ("Ahmed Helmy", "19691118", "https://en.wikipedia.org/wiki/Ahmed_Helmy#/media/File:Ahmed_Helmy_conf2018.jpg")
jennifer =  ("Jennifer Lawrence", "19900815", "https://en.wikipedia.org/wiki/Jennifer_Lawrence#/media/File:Jennifer_Lawrence_SDCC_2015_X-Men.jpg")
anniston = ("Jennifer Aniston", "19690211", "https://upload.wikimedia.org/wikipedia/commons/1/16/JenniferAnistonHWoFFeb2012.jpg")
profiles = [hany, emma, helmy, jennifer, anniston]
users = profiles
i = 0
for profile in profiles:
    users[i] = head.User(profile[0], profile[1])
    i += 1
def main():
    for user in users:
        print("{} age is {}".format(user.first_name, user.age()))
if __name__ == "__main__":
    main()
