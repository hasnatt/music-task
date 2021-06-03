import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation, TruncatedSVD
from pyLDAvis import prepare, save_html, show
from pyLDAvis import sklearn as sklearn_lda
import pyLDAvis
import random

class LdaController:
    def __init__(self,no_topics):
        self.no_topics = no_topics
        self.execute_lda()


    def read_csv(self):
        datasets = pd.read_csv(r'lyric_words.csv')
        datasets = datasets.head(6000)
        return datasets.dropna()

    def latent_dirichlet(self,data_frame):   
        count_vect = CountVectorizer(max_df=0.9, min_df=2) 
        doc_term_matrix = count_vect.fit_transform(data_frame['lyrics_bow'].values.astype('U'))

        LDA = LatentDirichletAllocation(n_components=self.no_topics, learning_decay = 0.7, random_state=16)
        LDA = LDA.fit(doc_term_matrix)

        for i in range(10):
            random_id = random.randint(0, len(count_vect.get_feature_names()))
            # print(count_vect.get_feature_names()[random_id])

        first_topic = LDA.components_[0]
        top_topic_words = first_topic.argsort()[-10:]
        # for i in top_topic_words:
        # print(count_vect.get_feature_names()[i])

        for i, topic in enumerate(LDA.components_):
            print(f'Top 10 words for LDA topic #{i}:')
            print([count_vect.get_feature_names()[i]
                for i in topic.argsort()[-10:]])
            print('\n')

        topic_values = LDA.transform(doc_term_matrix)
        topic_values.shape
        data_frame['topic'] = topic_values.argmax(axis=1)

        vis_lda(LDA, doc_term_matrix, count_vect)



    def execute_lda(self):
        data_frame = self.read_csv()
        self.latent_dirichlet(data_frame)
        data_frame.to_csv('lda.csv', sep=',', encoding='utf-8',columns=['id', 'artist','song', 'topic', ], index=False)

def vis_lda(LDA, doc_term_matrix, count_vect):
    model_vis_data = sklearn_lda.prepare(LDA, doc_term_matrix, count_vect, sort_topics=False)
    pyLDAvis.save_html(model_vis_data, '../templates/lda_output.html')
