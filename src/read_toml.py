import tomli  # python 3.9
from pprint import pprint

with open('./data/config.toml', 'rb') as f:
    data = tomli.load(f)

pprint(data, sort_dicts=False)
