import datetime
class User:
    """A member of FriendFace. For now we are
     only storing their name and birthdayself.
     But soon we will store an uncomfortable
     amount of user information."""
    def __init__(self, full_name, birthday, poster, quote):
        self.name = full_name
        self.birthday = birthday # yyyymmdd
        self.poster = poster # picture link
        self.quote = quote
        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    def age(self):
        """Return the age of the user in years."""
        tod_y = datetime.datetime.now().year
        tod_m = datetime.datetime.now().month
        tod_d = datetime.datetime.now().day
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd) # Date of birthday
        tod = datetime.date(tod_y, tod_m, tod_d) # Date of today
        age_in_days = (tod - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)
def main():
    help(User)
if __name__ == "__main__":
    main()
