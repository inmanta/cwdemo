"""
    Inmanta clearwater plugins

    :copyright: 2017 Inmanta NV
    :contact: code@inmanta.com
"""

from inmanta.plugins import plugin, Context
import requests


@plugin
def instances(url: "string", vnf_name: "string") -> "number":
    try:
        r = requests.get(url)
        data = r.json()
        if data is not None and "series" in data and data["series"] is not None and len(data["series"]) > 0:
            for serie in data["series"]:
                if "vnf" in serie["tags"] and vnf_name == serie["tags"]["vnf"]:
                    keys = serie["columns"]
                    values = serie["values"][-1]

                    d = dict(zip(keys, values))

                    return d["scale"]
    except (requests.exceptions.ConnectionError):
        pass
    return 0