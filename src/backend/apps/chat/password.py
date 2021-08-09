class PasswordManager():
    """Hash and verify user passwords using passlib """

    def __init__(self, app):
        """
        Create a passlib CryptContext.
        """

        self.app = app
        self.user_manager = app.user_manager

        # Create a passlib CryptContext
        self.password_crypt_context = CryptContext(schemes=["bcrypt"])


    def hash_password(self, password):
        """Hash plaintext ``password`` using the ``password_hash`` specified in the constructor.
        """
        # Use passlib's CryptContext to hash a password
        password_hash = self.password_crypt_context.hash(password)

        return password_hash


    def verify_password(self, password, password_hash):
        """Verify plaintext ``password`` against ``hashed password``.
        """
        return self.password_crypt_context.verify(password, password_hash)

