from msad_query.msadqExceptions import MSADQueryException
from msad_query.userRecord import parseRecord
from msad_query.psCmd import runPS


def _parseResult(resultTxt: str) -> list[dict]:
    records = []
    rcdText = resultTxt.split("\n\n")
    for rTxt in rcdText:
        rcd = parseRecord(rTxt)
        if rcd:
            records.append(rcd)
    return records


def raiseCmdExcptn(errMsg: str):
    raise MSADQueryException(errMsg)


def getAllUsers(domainServer: str, onError=raiseCmdExcptn) -> list[dict]:
    """
    returns a list of dict where each user info is a dict, or an empty list if no users are present\n
    domainServer: str, the host name / address of the domain controller\n
    onError: callable, method to call if the command fails, the error message is passed as the parameter
    """
    success, txt = runPS("Get-ADUser -Filter * -Server {}".format(domainServer))
    if success:
        return _parseResult(txt)
    return onError(txt)


def getGroupUsers(groupName: str, domainServer: str, onError=raiseCmdExcptn) -> list[dict]:
    """
    returns a list of dict where each user info is a dict, or an empty list if the group name is not found or no users are present\n
    groupName: str, the group name to search for, ie: 'Administrators' or 'Informatics' etc\n
    domainServer: str, the host name / address of the domain controller\n
    onError: callable, method to call if the command fails, the error message is passed as the parameter
    """
    success, txt = runPS("Get-ADGroupMember -Identity {} -Server {}".format(groupName, domainServer))
    if success:
        return _parseResult(txt)
    return onError(txt)


def getUser(accountId: str, domainServer: str, onError=raiseCmdExcptn) -> dict:
    """
    returns the user info as a dict or None\n
    accountId: str, the accountName, security id, GUID, or distiguished name of the account to search for, any are acceptable\n
    domainServer: str, the host name / address of the domain controller\n
    onError: callable, method to call if the command fails, the error message is passed as the parameter
    """
    success, txt = runPS("Get-ADUser -Identity {} -Server {}".format(accountId, domainServer))
    if success:
        return parseRecord(txt)
    return onError(txt)
