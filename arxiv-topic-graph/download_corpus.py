from preprocessing import flat_unique
import arxiv
import os
import time


# Returns the object id
def custom_slugify(obj):
    return obj.get('id').split('/')[-1]


def pdf_download(path='data/arxiv_metadata.json'):
    """Download all papers from metadata file."""
    qfin = flat_unique(path)
    pdfs = os.listdir('data/pdfs/')
    for paper in qfin:
        t0 = time.time()
        filename = '%s.pdf' % custom_slugify(paper)
        if filename not in pdfs:
            arxiv.download(paper, slugify=custom_slugify, dirpath='./data/pdfs/')
            print('Downloaded {}'.format(filename))
            
            # Arxiv API compliance
            elapsed = time.time() - t0
            if elapsed < 3:
                print('Sleeping {} seconds.'.format(elapsed))
                time.sleep(elapsed)
        else:
            print('Filename {} exists. Skipping.'.format(filename))
            
            
if __name__ == '__main__':
    pdf_download()