class UserDirectoryManager2():
    """The UserDirectoryManager2 keeps track of saved users.

    It manages user information and enables fast queries to look for User by
    either email or age.
    """

    class User():
        """The User class defines an entity with a name, email, age, and origin
        """

        def __init__(self, name, email, age, origin):
            """The constructor."""

            self.name = name
            self.email = email
            self.age = age
            self.origin = origin

        def __repr__(self):  # pragma: no cover
            return f'{self.name},{self.email},{self.age},{self.origin}'

    def __init__(self):
        """The constructor. Initialize a dict of emails:User and a dict
        of ages:[emails].
        """

        self.email_dir = {}  # key: email, val: user obj
        self.age_dir = {}    # key: age, val: list of emails

    def __not_none(self, name, email, age, origin):
        return any([val is None for val in [name, email, age, origin]])

    def __repeated_email(self, email):
        return email in self.email_dir

    def add_record(self, name, email, age, origin):
        """Add a new User to the dictionary.

        It creates a new User object with given data and it is added
        to email dictionary. Then, the email is added to the list of
        emails grouped by the dictionary of age.

        The method do not accept None types and the provided email
        must be unique.

        Args:
            name: not None, unique
            email: not None
            age: not None
            origin: not None

        Raises:
            TypeError

        Return:
            The created User.
        """

        if self.__not_none(name, email, age, origin):
            raise TypeError('All new user values must not be None')

        if self.__repeated_email(email):
            raise TypeError('User email already registered')

        new_user = self.User(name, email, age, origin)
        self.email_dir[email] = new_user

        # Create list of users by age
        self.age_dir.setdefault(age, []).append(email)

        return self.email_dir[email]

    def delete_record_by_email(self, email):
        """Deletes a User in the dictionary by email.

        The User and its email are deleted from the email direcotry and
        the age directory respectively.

        Args:
            email

        Return:
            The deleted User or None if the email is invalid.
        """

        user_deleted = self.email_dir.pop(email, None)

        if user_deleted:
            emails_by_age = self.age_dir.get(user_deleted.age)
            emails_by_age.remove(user_deleted.email)
            if len(emails_by_age) == 0:
                self.age_dir.pop(user_deleted.age)

        return user_deleted

    def search_by_email(self, email):
        """Searches a User in the dictionary by email.

        Args:
            email

        Return:
            The User with the corresponding email or None if
            the User is not found.
        """

        return self.email_dir.get(email, None)

    def search_by_age(self, age):
        """Searches all users with the given age.

        Args:
            age

        Return:
            A list of Users with the corresponding age or empty list if
            Users are not found.
        """

        mails = self.age_dir.get(age, [])
        users = []

        for email in mails:
            user = self.email_dir.get(email)
            users.append(user)

        return users

    def get_all_records(self):
        """Gets all registered Users.

        Return:
            A list of all registered Users.
        """

        return list(self.email_dir.values())
