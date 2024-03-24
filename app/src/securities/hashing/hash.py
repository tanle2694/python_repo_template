from passlib.context import CryptContext

from src.config.manager import settings


class HashGenerator:
    def __init__(self):
        self._hash_ctx_layer_1: CryptContext = CryptContext(
            schemes=[settings.HASHING_ALGORITHM_LAYER_1],
            deprecated="auto"
        )

        self._hash_ctx_layer_2: CryptContext = CryptContext(
            schemes=[settings.HASHING_ALGORITHM_LAYER_2],
            deprecated="auto"
        )

        self._hash_ctx_salt: str = settings.HASHING_SALT

    @property
    def _get_hashing_salt(self) -> str:
        return self._hash_ctx_salt

    @property
    def generate_password_salt_hash(self) -> str:
        return self._hash_ctx_layer_1.hash(secret=self._get_hashing_salt)

    def generate_password_hash(self, hash_salt: str, password: str) -> str:
        return self._hash_ctx_layer_2.hash(secret=hash_salt + password)

    def is_password_verified(self, password: str, hashed_password: str) -> bool:
        return self._hash_ctx_layer_2.verify(secret=password, hash=hashed_password)


def get_hash_generator() -> HashGenerator:
    return HashGenerator()


hash_generator: HashGenerator = get_hash_generator()
