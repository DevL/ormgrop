from unittest.mock import patch
from src.ormgrop.debug import measure


def describe_measure():
    def _simple_function(arg_1, arg_2, kwarg_1=None, kwarg_2=None):
        return {"arg_1": arg_1, "arg_2": arg_2, "kwarg_1": kwarg_1, "kwarg_2": kwarg_2}

    def test_logging_mesurements():
        logger = FakeLogger()
        with patch("src.ormgrop.debug.take_time", side_effect=[179246391423, 179246392065]):
            measured = measure(logger.log)(_simple_function)
            result = measured(1, 2, kwarg_1=3, kwarg_2=4)

            assert result == {"arg_1": 1, "arg_2": 2, "kwarg_1": 3, "kwarg_2": 4}
            assert logger.messages == ["[MEASURE] Called '_simple_function' for 642 nanoseconds."]


class FakeLogger:
    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)
