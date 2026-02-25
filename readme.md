# msad-query - Microsoft Active Directory Query

Simple wrapper to perform Windows Powershell-based AD User Querys

## Usage

Use any of the three methods provided to get domain records returned:

* getUser
* getAllUsers
* getGroupUsers

````python
from msad_query import getUser
import json

record = getUser(accountId="jdoe", domainServer="<your domain server name>")

print(json.dumps(record, indent=4))
````

Response record:

````json
{
    "distinguishedName": "CN=John Doe,OU=Users,OU=Company,DC=corp,DC=local",
    "enabled": true,
    "givenName": "John",
    "name": "John Doe",
    "objectClass": "user",
    "objectGUID": "54c6640e-a597-45ad-974e-170d53afbb1a",
    "samAccountName": "jdoe",
    "sID": "S-1-5-21-3691830899-5239577749-90497688-2222",
    "surname": "Doe",
    "userPrincipalName": "jdoe@company.com"
}
````

The response for the other methods are lists of the same format.

## Installation

### Prerequisites

The machine running this is assumed to be a Windows machine. The Windows Feature 'RSAT-AD-PowerShell' must 
be installed. This can be installed from within Powershell with the following command:

````powershell
    Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
````

### Using In Projects

Installation:

````bash
    pip install msad-query
````

### Cloning For Development

Set up a virtual environment. Once an environment is set up, activate it and add dependencies with the following:

````bash
    pip install -r requirements/dev.txt
````

The dev.txt file includes:

* BLACK, a code formatter, see notes at the bottom of this file for details
* setuptools, which provides the support for the building of the package

To run tests:

````bash
    python -m unittest discover -s tests/
````

### Code Formatting

Code formatting is done using BLACK. BLACK allows almost no customization to how code is formatted with the exception of line length, which has been set to 119 characters.

Use the following to bulk format files:


````bash
    black . -l 144
````

### Creating A New Release

Please do the following when making a new release, most are documented above:

1. Run tests
1. Code format
1. Be sure to update the change log and _metadata.json with version and notes
1. git add, commit, and push changes
1. run the following code to generate a wheel:

````bash
    python -m build
````
