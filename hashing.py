from passlib.context import CryptContext

pxd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class hash():
    @staticmethod
    def bcrypt(password: str):
        return pxd_cxt.hash(password)

    @staticmethod
    def verify(plain_password, hashed_password):
        return pxd_cxt.verify(plain_password, hashed_password)


