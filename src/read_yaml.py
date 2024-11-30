import yaml
from pprint import pprint

with open('./data/config.yaml', 'r', encoding='utf-8') as stream:
    try:
        config: dict = yaml.safe_load(stream)
        pprint(config, sort_dicts=False)
        # pprint(config['text'])
        # pprint(config['text_1'])
        # pprint(config['text_2'])
    except yaml.YAMLError as exc:
        print(exc)

