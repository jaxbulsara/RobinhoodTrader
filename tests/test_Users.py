from RobinhoodTrader import RobinhoodTrader
from RobinhoodTrader.datatypes import (
    User,
    UserBasicInfo,
    UserAdditionalInfo,
    UserCipQuestions,
    UserEmployment,
    Page,
    UserInvestmentProfile,
)


def test_get_user(trader):
    trader: RobinhoodTrader

    user = trader.get_user()

    expected_attributes = [
        "created_at",
        "email",
        "email_verified",
        "first_name",
        "id",
        "id_info",
        "last_name",
        "origin",
        "profile_name",
        "url",
        "username",
    ]

    assert type(user) == User

    for attribute in expected_attributes:
        assert hasattr(user, attribute)


def test_get_user_basic_info(trader):
    trader: RobinhoodTrader

    data = trader.get_user_basic_info()

    expected_attributes = [
        "address",
        "citizenship",
        "city",
        "country_of_residence",
        "date_of_birth",
        "marital_status",
        "number_dependents",
        "phone_number",
        "signup_as_rhs",
        "state",
        "tax_id_ssn",
        "updated_at",
        "user",
        "zipcode",
    ]

    assert type(data) == UserBasicInfo

    for attribute in expected_attributes:
        assert hasattr(data, attribute)


def test_get_user_additional_info(trader):
    trader: RobinhoodTrader

    data = trader.get_user_additional_info()

    expected_attributes = [
        "agreed_to_rhs",
        "agreed_to_rhs_margin",
        "control_person",
        "control_person_security_symbol",
        "object_to_disclosure",
        "security_affiliated_address",
        "security_affiliated_address_subject",
        "security_affiliated_employee",
        "security_affiliated_firm_name",
        "security_affiliated_firm_relationship",
        "security_affiliated_person_name",
        "security_affiliated_requires_duplicates",
        "stock_loan_consent_status",
        "sweep_consent",
        "updated_at",
        "user",
    ]

    assert type(data) == UserAdditionalInfo

    for attribute in expected_attributes:
        assert hasattr(data, attribute)


def test_get_user_cip_questions(trader):
    trader: RobinhoodTrader

    data = trader.get_user_cip_questions()

    expected_attributes = []

    assert type(data) == UserCipQuestions

    for attribute in expected_attributes:
        assert hasattr(data, attribute)


def test_get_user_employment(trader):
    trader: RobinhoodTrader

    data = trader.get_user_employment()

    expected_attributes = [
        "employer_address",
        "employer_city",
        "employer_name",
        "employer_state",
        "employer_zipcode",
        "employment_status",
        "occupation",
        "updated_at",
        "user",
        "years_employed",
    ]

    assert type(data) == UserEmployment

    for attribute in expected_attributes:
        assert hasattr(data, attribute)


def test_get_user_identity_mismatch(trader):
    trader: RobinhoodTrader

    data = trader.get_user_identity_mismatch()
    assert type(data) == Page


def test_get_user_investment_profile(trader):
    trader: RobinhoodTrader

    data = trader.get_user_investment_profile()

    expected_attributes = [
        "annual_income",
        "interested_in_options",
        "investment_experience",
        "investment_experience_collected",
        "investment_objective",
        "liquid_net_worth",
        "liquidity_needs",
        "option_trading_experience",
        "professional_trader",
        "risk_tolerance",
        "source_of_funds",
        "suitability_verified",
        "tax_bracket",
        "time_horizon",
        "total_net_worth",
        "understand_option_spreads",
        "updated_at",
        "user",
    ]

    assert type(data) == UserInvestmentProfile

    for attribute in expected_attributes:
        assert hasattr(data, attribute)

