class UserDirectoryManager():
    class User():
        def __init__(self, name, email, age, origin):
            self.name = name
            self.email = email
            self.age = age
            self.origin = origin
        
        def __repr__(self):
            return f'{self.name},{self.email},{self.age},{self.origin}'

    def __init__(self):
        self.email_dir = {} # key: email, val: user obj
        self.age_dir = {} # key: age, val: list of emails

    def __not_none(self, name, email, age, origin):
        return any( [val is None for val in [name, email, age, origin]] )

    def __repeated_email(self, email):
        return email in self.email_dir

    def add_record(self, name, email, age, origin):
        if self.__not_none(name, email, age, origin):
            raise Exception('All new user values must not be None')

        if self.__repeated_email(email):
            raise Exception('User email already registered')
        
        new_user = self.User(name, email, age, origin)
        self.email_dir[email] = new_user
        
        # Create list of users by age
        self.age_dir.setdefault(age, []).append(email)

    def delete_record(self, email):
        user_deleted = self.email_dir.pop(email, None)

        if user_deleted:
            emails_by_age = self.age_dir.get(user_deleted.age)
            emails_by_age.remove(user_deleted.email)

        return user_deleted


    def search_by_email(self, email):
        return self.email_dir.get(email, None)

    def search_by_age(self, age):
        mails = self.age_dir.get(age, [])
        users = []

        for email in mails:
            user = self.email_dir.get(email)
            users.append(user)

        return users

    def get_all_records(self):
        return list(self.email_dir.values())
