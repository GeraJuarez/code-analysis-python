class UserDirectoryManager():
    class User():
        def __init__(self, name, address, phone, email):
            self.name = name
            self.address = address
            self.phone = phone
            self.email = email
        
        def __str__(self):
            return f'{self.name},{self.address},{self.phone},{self.email}'

        def __repr__(self):
            return f'{self.name},{self.address},{self.phone},{self.email}'

    def __init__(self):
        self.email_dir = {}
        self.name_dir = {}

    def get_data(self):
        return list(self.email_dir.values())

    def create_record(self, name, address, phone, email):
        if email in self.email_dir:
            raise Exception('User email already registered')
        
        new_user = self.User(name, address, phone, email)
        self.email_dir[email] = new_user
        
        self.name_dir.setdefault(name, []).append(email)

    def save_to_file(self, file_path='users_out.txt'):
        with open(file_path, "w") as fp:
            for _, user in self.email_dir.items():
                fp.write(str(user) + '\n')

    def load_from_file(self, file_path='users_out.txt'):
        with open(file_path, "r") as fp:
            for line in fp:
                values =  [ data.rstrip('\n') for data in line.split(',') ]
                self.create_record(*values)

    def search_by_email(self, email):
        return self.email_dir.get(email, None)

    def search_by_name(self, name):
        emails = self.name_dir.get(name, '')
        return emails
