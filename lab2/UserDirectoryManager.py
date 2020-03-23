class UserDirectoryManager():
    """The UserDirectoryManager keeps track of saved users.

    It manages user information and it can load and save them from txt files.
    """

    class User():
        """The User class defines an entity with a
        name, address, phone, and email.
        """

        def __init__(self, name, address, phone, email):
            self.name = name
            self.address = address
            self.phone = phone
            self.email = email

        def __str__(self):  # pragma: no cover
            return f'{self.name},{self.address},{self.phone},{self.email}'

        def __repr__(self):  # pragma: no cover
            return f'{self.name},{self.address},{self.phone},{self.email}'

    def __init__(self):
        """The constructor. Initialize a dict of emails:User
        """
        self.email_dir = {}

    def get_data(self):
        """Gets all registered Users.

        Return:
            A list of all registered Users.
        """

        return list(self.email_dir.values())

    def create_record(self, name, address, phone, email):
        """Add a new User to the dictionary.

        It creates a new User object with given data and it is added
        to email dictionary.

        The method do not accept None type as name and the provided email
        must be unique.

        Args:
            name: not None, unique
            email
            age
            origin

        Raises:
            TypeError

        Return:
            The created User.
        """

        if name is None:
            raise TypeError('name must not be none')

        if email in self.email_dir:
            raise TypeError('User email already registered')

        new_user = self.User(name, address, phone, email)
        self.email_dir[email] = new_user

        return new_user

    def save_to_file(self, file_path='users_out.txt'):
        """Save data into a txt file in the specified path.

        Args:
            file_path: the path and filename, default name is users_out.txt

        Raises:
            IOError
        """

        with open(file_path, "w") as fp:
            for _, user in self.email_dir.items():
                fp.write(str(user) + '\n')

    def load_from_file(self, file_path='users_out.txt'):
        """Load data from a file in the specified path.

        Args:
            file_path: the path and filename of data to load

        Raises:
            IOError
        """

        with open(file_path, "r") as fp:
            for line in fp:
                values = [data.rstrip('\n') for data in line.split(',')]
                self.create_record(*values)

    def search_by_email(self, email):
        """Searches a User in the dictionary by email.

        Args:
            email

        Return:
            The User with the corresponding email or None if
            the User is not found.
        """

        return self.email_dir.get(email, None)
