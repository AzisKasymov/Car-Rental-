class User:
    def __init__(self, user_id, name, email, password, is_admin):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = bool(is_admin)

    def __repr__(self):
        return (
            f"User(id={self.id}, name='{self.name}', email='{self.email}', "
            f"is_admin={self.is_admin})"
        )
