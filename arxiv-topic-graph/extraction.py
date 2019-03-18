import os
import preprocessing
from gensim import corpora
from gensim.models.doc2vec import TaggedDocument


def texts_corpus(textdir='data/texts/'):
    """Create a preprocessed corpus for doc2vec training.
    
    Parameters:
        textdir: str
            Path of text files
    Returns:
        corpus: list of gensim.models.doc2vec.TaggedDocument objects
            Tagged by arxiv ID
    """
    files = os.listdir(textdir)
    corpus = []
    for i, file in enumerate(files):
        if '.txt' not in file:
            continue
        with open(textdir + file) as f:
            t = f.read()
            corpus.append(
                TaggedDocument(
                    words=preprocessing.doc_preprocessor(t, lemmatize=False),
                    tags=[file.strip('.txt')])
            )
            
    return corpus


if __name__ == '__main__':
    train_corpus = texts_corpus()

    model = gensim.models.doc2vec.Doc2Vec(vector_size=100, min_count=2, epochs=100)
    model.build_vocab(train_corpus)
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)
    
    model.save('data/doc2vec.model')
    