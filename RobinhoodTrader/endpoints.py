api = "https://api.robinhood.com/"
nummus = "https://nummus.robinhood.com/"


def login():
    return api + "/oauth2/token/"


def logout():
    return api + "/oauth2/revoke_token/"


def accounts():
    return api + "accounts/"


def user():
    return api + "user/"


def userAdditionalInfo():
    return api + "user/additional_info/"


def userBasicInfo():
    return api + "user/basic_info/"


def userCipQuestions():
    return api + "user/cip_questions/"


def userEmployment():
    return api + "user/employment/"


def userID():
    return api + "user/id/"


def userIdentityMismatch():
    return api + "user/identity_mismatch/"


def userInvestmentProfile():
    return api + "user/investment_profile/"
