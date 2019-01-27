"""Get 8k most recent papers from for each category of q-fin Arxiv and save. Fix imports"""
from .papers import get_qfin
import json


def main(path='arxiv_metadata.json'):
    qfin = get_qfin()
    with open(path, 'w') as out:
        json.dump(qfin, out)
    
    
if __name__ == '__main__':
    main()
