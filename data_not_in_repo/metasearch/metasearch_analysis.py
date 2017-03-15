# coding: utf-8
# get our data from openneu.ro
#get_ipython().system('git clone https://github.com/OpenNeuroLab/metasearch.git')
from pathlib import Path
metasearch_dir = Path('data_not_in_repo/metasearch/')
data_exists = metasearch_dir.exists()
in_repro_course = Path.cwd().name == 'repro_course'
if data_exists and in_repro_course:
    print('data has been downloaded')
else:
    assert(False)
