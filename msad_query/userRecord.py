class RECORD_FIELDS(object):
    ENABLED = "enabled"
    FIRST_NAME = "givenName"
    LAST_NAME = "surname"
    FULL_NAME = "name"
    TYPE = "objectClass"
    ACCOUNT_NAME = "samAccountName"
    PRINCIPAL_NAME = "userPrincipalName"
    DISTINGUISHED_NAME = "distinguishedName"
    GUID = "objectGUID"
    SECURITY_ID = "sID"


def parseRecord(resultTxt: str) -> dict:
    """
    returns a dict from multi-line text
    """
    r = {}
    lines = resultTxt.split("\n")
    for rl in lines:
        if rl:
            # split the values
            kv = rl.split(" : ")
            # make the key into camel case
            kf = kv[0][0].lower() + kv[0].strip()[1:]
            # add the key/value to the dict
            r[kf] = kv[1].strip()
    # normalize values
    if RECORD_FIELDS.ENABLED in r:
        r[RECORD_FIELDS.ENABLED] = r[RECORD_FIELDS.ENABLED] == "True"
    if (RECORD_FIELDS.PRINCIPAL_NAME in r) and not r[RECORD_FIELDS.PRINCIPAL_NAME].islower():
        r[RECORD_FIELDS.PRINCIPAL_NAME] = r[RECORD_FIELDS.PRINCIPAL_NAME].lower()
    return r
