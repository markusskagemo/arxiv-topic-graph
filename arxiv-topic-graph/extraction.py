from gensim.models import LdaModel, LdaMulticore

def placeholder():
    # Set training parameters.
    num_topics = 40
    chunksize = 50 # size of the doc looked at every pass
    passes = 5 # number of passes through documents
    iterations = 10
    eval_every = 1  # Don't evaluate model perplexity, takes too much time.

    # Make a index to word dictionary.
    temp = dictionary[0]  # This is only to "load" the dictionary.
    id2word = dictionary.id2token

    # Run multicore LDA model
    %time model = LdaMulticore(corpus=corpus, id2word=id2word, chunksize=chunksize, \
                               num_topics=num_topics, passes=passes, iterations=iterations)
    
    import pyLDAvis.gensim
    pyLDAvis.enable_notebook()

    import warnings
    warnings.filterwarnings("ignore", category=DeprecationWarning) 

    pyLDAvis.gensim.prepare(model, corpus, dictionary)