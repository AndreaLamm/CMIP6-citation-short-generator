#!/usr/bin/env python
import sys
import json
import yaml

# Replace title by place holder
data = yaml.safe_load(json.dumps(json.loads(open(sys.argv[1]).read())))
data['titles'] = ["CMIP6 <institution_id> <source_id> <experiment_id> model output"]
 
# Delete DRS subject (will be filled in by the JSON-Generator)
del data['subjects'][0]
del data['identifier']
del data['publicationYear']
del data['publisher']
del data['descriptions']
del data['rightsList']
del data['language']
del data['formats']
del data['dates']
del data['resourceType']		

print(
    yaml.dump(data, default_flow_style=False,
    )
)
