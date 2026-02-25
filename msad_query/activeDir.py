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
    """
    raises a MSADQueryException

    Args:
        errMsg (str): error message encountered

    Raises:
        MSADQueryException: General Package Exception
    """
    raise MSADQueryException(errMsg)


def getAllUsers(domainServer: str, onError=raiseCmdExcptn) -> list[dict]:
    """
    returns a list of dict where each user info is a dict, or an empty list if no users are present

    Args:
        domainServer (str): the host name / address of the domain controller
        onError (callable, optional): method to call if the command fails, the error message is passed as the parameter. Defaults to raiseCmdExcptn which raises a MSADQueryException

    Returns:
        list[dict]: a list of dict objects, each representing a user with keys MSAD_USER_FIELDS

    Raises:
        MSADQueryException: General Package Exception, Can Be Changed By Providing An Alternative callable Method To OnError
    """
    success, txt = runPS("Get-ADUser -Filter * -Server {}".format(domainServer))
    if success:
        return _parseResult(txt)
    return onError(txt)


def getGroupUsers(groupName: str, domainServer: str, onError=raiseCmdExcptn) -> list[dict]:
    """
    returns a list of dict where each user info is a dict, or an empty list if the group name is not found or no users are present

    Args:
        groupName (str): the group name to search for, ie: 'Administrators' or 'Users' etc
        domainServer (str): the host name / address of the domain controller
        onError (callable, optional): method to call if the command fails, the error message is passed as the parameter. Defaults to raiseCmdExcptn which raises a MSADQueryException

    Returns:
        list[dict]: a list of dict objects, each representing a user with keys MSAD_USER_FIELDS

    Raises:
        MSADQueryException: General Package Exception, Can Be Changed By Providing An Alternative callable Method To OnError
    """
    success, txt = runPS("Get-ADGroupMember -Identity {} -Server {}".format(groupName, domainServer))
    if success:
        return _parseResult(txt)
    return onError(txt)


def getUser(accountId: str, domainServer: str, onError=raiseCmdExcptn) -> dict:
    """
    returns the user info as a dict or None

    Args:
        accountId (str):  the accountName, security id, GUID, or distiguished name of the account to search for, any are acceptable
        domainServer (str): the host name / address of the domain controller
        onError (callable, optional):method to call if the command fails, the error message is passed as the parameter. Defaults to raiseCmdExcptn which raises a MSADQueryException

    Returns:
        dict: a dict object representing a user with keys MSAD_USER_FIELDS

    Raises:
        MSADQueryException: General Package Exception, Can Be Changed By Providing An Alternative callable Method To OnError
    """
    success, txt = runPS("Get-ADUser -Identity {} -Server {}".format(accountId, domainServer))
    if success:
        return parseRecord(txt)
    return onError(txt)
