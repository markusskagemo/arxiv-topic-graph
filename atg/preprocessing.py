import argparse
import logging
import six
import sys
import pdfminer.settings
pdfminer.settings.STRICT = False
import pdfminer.high_level
import pdfminer.layout
from pdfminer.image import ImageWriter


def extract_text(files=[], outfile='-',
            _py2_no_more_posargs=None,  
            no_laparams=False, all_texts=None, detect_vertical=None, # LAParams
            word_margin=None, char_margin=None, line_margin=None, boxes_flow=None, # LAParams
            output_type='text', codec='utf-8', strip_control=False,
            maxpages=0, page_numbers=None, password="", scale=1.0, rotation=0,
            layoutmode='normal', output_dir=None, debug=False,
            disable_caching=False, **other):
    """Converts PDF text content (though not images containing text) to plain text, html, xml or "tags".
    From pdfminer.six (https://github.com/pdfminer/pdfminer.six)
    """
    if _py2_no_more_posargs is not None:
        raise ValueError("Too many positional arguments passed.")
    if not files:
        raise ValueError("Must provide files to work upon!")

    # If any LAParams group arguments were passed, create an LAParams object and
    # populate with given args. Otherwise, set it to None.
    if not no_laparams:
        laparams = pdfminer.layout.LAParams()
        for param in ("all_texts", "detect_vertical", "word_margin", "char_margin", "line_margin", "boxes_flow"):
            paramv = locals().get(param, None)
            if paramv is not None:
                setattr(laparams, param, paramv)
    else:
        laparams = None

    imagewriter = None
    if output_dir:
        imagewriter = ImageWriter(output_dir)

    if output_type == "text" and outfile != "-":
        for override, alttype in ((".htm", "html"), (".html", "html"), (".xml", "xml"), (".tag", "tag")):
            if outfile.endswith(override):
                output_type = alttype

    if outfile == "-":
        outfp = sys.stdout
        if outfp.encoding is not None:
            codec = 'utf-8'
    else:
        outfp = open(outfile, "wb")


    for fname in files:
        with open(fname, "rb") as fp:
            pdfminer.high_level.extract_text_to_fp(fp, **locals())
    return outfp


import json


def flat_unique(path='data/arxiv_metadata.json'):
    with open(path) as f:
        paper_meta = json.load(f)

    all_papers = []
    ids = []
    for field, papers in paper_meta.items():
        for paper in papers:
            all_papers.append(paper)
            # Store Arxiv ID
            ids.append(paper['id'])

    # Truth map for unique list
    # Way to deal with unhashable dicts issue
    filled_ids = {id_: False for id_ in ids}
    all_unique_papers = []
    for paper in all_papers:
        if not filled_ids[paper['id']]:
            all_unique_papers.append(paper)
            filled_ids[paper['id']] = True
            
    return all_unique_papers