from RobinhoodTrader import RobinhoodTrader


def test_investmentProfile(robinhoodTrader: RobinhoodTrader):
    investmentProfile = robinhoodTrader.getInvestmentProfile()

    assert type(investmentProfile).__name__ == "dict"
    assert "user" in investmentProfile.keys()
