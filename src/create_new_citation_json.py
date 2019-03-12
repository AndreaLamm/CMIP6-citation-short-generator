from os.path import join, dirname, abspath
from os import system

from cmip6_data_citation_generator import generate_jsons

here = dirname(abspath(__file__))

######################################################################
## Fill in your Directories, JSON-Templates, Output directories!!   ##
## For (source_id and/or experiment_id) OR (Input4MIPs)

# Make decision: Citation for input4mips or CMIP6 source_id and/or experiment_id
source  = 0  # set to 1 to make citation for the source_id, otherwise set to 0   
exp     = 0  # set to 1 to make citation for the experiment_id, otherwise set to 0 
in4mips = 1  # set to 1 to make citation for Input4MIPs data, otherwise set to 0 

# Directory structure for JSON templates and generated JSON output 
#  (changes not necessary)
template_dir = join(here, "..", "input_templates")
output_dir   = join(here, "..", "output_json")

# Directory structure for input data (CMIP6 DRS conform) 
input_dir         = join(here, "..", "CMIP6_output_data", "CMIP6output_like")
input_dir_in4mips = join(here, "..", "CMIP6_output_data", "input4MIPs_like")

# JSON templates
json_template_source  = join(template_dir, "test_source.json")
json_template_exp     = join(template_dir, "test_experiment.json")
json_template_in4mips = join(template_dir, "test_in4mips.json")

######################################################################



regexp = ".*"  # i.e. all files
keep = True

# Source_id citation
if source == 1:
	granular = "source"
	drs = "CMIP6output_"+granular 
	yaml_source = json_template_source +'.yaml'
	command=('python3 convert_json_to_yaml/convert_json2yaml_'+granular+'.py '+json_template_source+' > '+ yaml_source)
	make_yaml = system(command)
	generate_jsons(
		input_dir,
    		yaml_source,
    		drs,
    		output_dir,
    		regexp=regexp,
    		keep=keep)


# Experiment_id citation
if exp == 1:
	granular = "exp"
	drs = "CMIP6output_"+granular 
	yaml_exp = json_template_exp +'.yaml'
	command=('python3 convert_json_to_yaml/convert_json2yaml_'+granular+'.py '+json_template_exp+' > '+ yaml_exp)
	make_yaml = system(command)
	generate_jsons(
		input_dir,
    		yaml_exp,
    		drs,
    		output_dir,
    		regexp=regexp,
    		keep=keep)
	

# Input4MIPs citation
if in4mips == 1:
	drs = "CMIP6input4MIPs" 
	yaml_in4mips = json_template_in4mips +'.yaml'
	command=('python3 convert_json_to_yaml/convert_json2yaml_in4mips.py '+json_template_in4mips+' > '+ yaml_in4mips)
	make_yaml = system(command)
	generate_jsons(
		input_dir_in4mips,
    		yaml_in4mips,
    		drs,
    		output_dir,
    		regexp=regexp,
    		keep=keep)



