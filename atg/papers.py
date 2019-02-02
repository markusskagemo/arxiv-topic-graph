import arxiv
import time


def large_query(**kwargs):
    """Partitions large Arxiv query.
    
    Parameters:
        **kwargs: dict
            Same parameters as arxiv.query() (https://github.com/lukasschwab/arxiv.py)
            search_query: string
                Ex: "cat:q-fin.CP AND all:portfolio optimization"
                All q-fin cats: ['CP', 'EC', 'GN', 'MF', 'PM', 'PR', 'RM', 'ST', 'TR']
                    https://arxiv.org/archive/q-fin
            id_list: list of strings
            start: int
                Don't pass, handled by function
            max_results: int
            sort_by: string
            sort_order: string
    Returns:
        results: list
    """ 
    results = []
    for s in range(0, kwargs['max_results'], 2000): # 2000 is query max
        aq = arxiv.query(**kwargs, start=s)
        if len(aq):
            results.extend(aq)
        # Add 3 sec request delay for Arxiv API compliance
        time.sleep(3)
    
    return results


def get_qfin(paper_search='', 
             max_results=8000,
             sort_by='lastUpdatedDate', 
             cats=['CP', 'EC', 'GN', 'MF', 'PM', 'PR', 'RM', 'ST', 'TR']):
    """Query Arxiv quantitative finance. Ad-hoc hardcoded.
    
    Parameters:
        paper_search: string
    """
    kw = {'max_results': max_results, 'sort_by': sort_by}
    total_results = {}
    for category in cats:
        if len(paper_search):
            kw['search_query'] = '{} AND cat:q-fin.{}'.format(paper_search, category)
        else:
            kw['search_query'] = 'cat:q-fin.{}'.format(category)
        total_results[category] = large_query(**kw)
    
    return total_results


import json


def get_metadata(path='data/arxiv_metadata.json'):
    """Get 8k most recent papers from for each category of q-fin Arxiv"""
    qfin = get_qfin()
    json.dumps(qfin, path)
    
    
def pdf_download(path='data/arxiv_metadata.json'):
    """Download all """
    from preprocessing import flat_unique
    
    qfin = flat_unique(path)
    for paper in qfin:
        arxiv.download(paper, '{}.txt'.format(paper['id'].split("/")[0]))