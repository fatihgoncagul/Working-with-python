class User:

    def __init__(self, user_id, username):
        #  every time we create user this init gets triggered
        # parameters must be provided when user object is created,
        # but we can give default values
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")

print(user_1.id)
print(user_1.followers)
user_2 = User("007", "Bond")
print("------------")
print(user_1.following)
print(user_2.followers)

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)
