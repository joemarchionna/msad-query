import os
import json
import pathlib


def loadUnittestParameters(fn="wkdir/unittest/parameters.json") -> dict:
    if not os.path.exists(fn):
        pathlib.Path(os.path.dirname(fn)).mkdir(parents=True, exist_ok=True)
        dcfg = {
            "domainController": "<domain controller name>",
            "domainUser": "<some domain username>",
            "domainGroup": "<some domain group>",
        }
        with open(fn, "w") as fw:
            json.dump(dcfg, fw, indent=4)
        return dcfg
    with open(fn) as fr:
        return json.load(fr)


def emptyList(*args) -> list:
    return []


def emptyDict(*args) -> dict:
    return {}
