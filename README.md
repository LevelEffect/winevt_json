# winevt_json
## Convert Microsoft Windows system events from native format to a JSON object


### Install:
```
pip install winevt_json
```

### Usage:
```
import winevt_json
import json

evt_json = winevt_json.evtx_to_json("sample_log.evtx")

with open("output.json", "a+") as out_f:

    # ident=4 is for pretty formatting, not required
    out_f.writelines(json.dumps(evt_json, indent=4))
```
