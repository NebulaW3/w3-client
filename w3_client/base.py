import abc


class BaseClient(abc.ABC):
    def dummy(self, first_arg: int, second_arg: str) -> bool:
        """
        Testing a dummy function.

        :param first_arg: Some integer.
        :param second_arg: Some string.
        :return: Just a boolean.

        Example:
        >>> from w3_client import ETHClient
        >>> client = ETHClient()
        >>> client.dummy(1, "2")
        True
        """
