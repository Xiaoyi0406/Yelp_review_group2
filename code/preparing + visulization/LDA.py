#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df =  pd.read_csv('/Users/kzhao46/Dropbox/628-2/data/s1.csv',delimiter=',')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


# In[ ]:


n_features = 1000


# In[ ]:


tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                max_features=n_features,
                                stop_words='english',
                                max_df = 0.5,
                                min_df = 10)
tf = tf_vectorizer.fit_transform(df.text)


# In[ ]:


from sklearn.decomposition import LatentDirichletAllocation


# In[ ]:


n_topics = 10
lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=50,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)


# In[ ]:


lda.fit(tf)


# In[ ]:


LatentDirichletAllocation(batch_size=128, doc_topic_prior=None,
             evaluate_every=-1, learning_decay=0.7,
             learning_method='online', learning_offset=50.0,
             max_doc_update_iter=100, max_iter=50, mean_change_tol=0.001,
             n_jobs=1, n_topics=5, perp_tol=0.1, random_state=0,
             topic_word_prior=None, total_samples=1000000.0, verbose=0)


# In[ ]:


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


# In[ ]:


n_top_words = 10


# In[ ]:


tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)


# In[ ]:


import pyLDAvis
import pyLDAvis.sklearn
pyLDAvis.enable_notebook()
pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)


# In[ ]:


data = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
pyLDAvis.show(data)


# In[ ]:




