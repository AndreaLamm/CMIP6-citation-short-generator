#!/usr/bin/env python
import sys
import json
import yaml

# Replace title by place holder
data = yaml.safe_load(json.dumps(json.loads(open(sys.argv[1]).read())))
data['titles'] = ["CMIP6 <institution_id> <source_id> model output"]
 
# Delete DRS subject (will be filled in by the JSON-Generator) and all
#  automated filled attributes
if data.get('subjects') is not None:
	del data['subjects'][0]
if data.get('identifier') is not None:
	del data['identifier']
if data.get('publicationYear') is not None:
	del data['publicationYear']
if data.get('publisher') is not None:
	del data['publisher']
if data.get('descriptions') is not None:
	del data['descriptions']
if data.get('rightsList') is not None:
	del data['rightsList']
if data.get('language') is not None:
	del data['language']
if data.get('formats') is not None:
	del data['formats']
if data.get('dates') is not None:
	del data['dates']
if data.get('resourceType') is not None:
	del data['resourceType']		

print(
    yaml.dump(data, default_flow_style=False,
    )
)
