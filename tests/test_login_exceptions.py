from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.exceptions import LoginError
import pytest


def test_login_not_console_exceptions(monkeypatch):
    trader = RobinhoodTrader()

    monkeypatch.setattr(trader.session, "session_is_console", False)

    with pytest.raises(
        ValueError,
        match="This method is not being called in an interactive console. Must pass a non-null tuple of credentials.",
    ):
        trader.login((None, None), use_config=False)

    with pytest.raises(
        LoginError,
        match="Unable to log in. Check your credentials or authentication code and try again.",
    ):
        trader.login(("user", "pass"), use_config=False)


def test_login_console_exceptions(use_my_config, monkeypatch):
    trader = RobinhoodTrader()

    with pytest.raises(
        LoginError,
        match="Unable to log in. Check your credentials or authentication code and try again.",
    ):
        trader.login(("user", "pass"))

