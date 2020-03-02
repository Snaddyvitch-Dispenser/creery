from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
default_prefix = "CREA"
known_chains = {
    "CREARY": {
        "chain_id": "0" * int(256 / 4),
        "min_version": '0.0.0',
        "prefix": "CREA",
        "chain_assets": [
            {"asset": "@@000000013", "symbol": "CBD", "precision": 3, "id": 0},
            {"asset": "@@000000021", "symbol": "CREA", "precision": 3, "id": 1},
            {"asset": "@@000000037", "symbol": "VESTS", "precision": 6, "id": 2},
            {"asset": "@@000000005", "symbol": "CGY", "precision": 5, "id": 3},
        ],
    },
}
