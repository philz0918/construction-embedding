from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import os
os.chdir("/Users/macbookpro/Project/Construction_DeepLearning/src")
import collect_data as cd
import crawl as cr

'''
bodies, titlelist, datelistt from collect_data
'''


if __name__ == "__main__" :
    #1. make lower case, regulazation
    l_bodies=[]
    for body in cd.bodies :
        
        body = str(body).lower()
        l_bodies.append(body)

        
    #2. removing stop words, tokenize
    stop_words = set(stopwords.words('english'))

    token_sentence = []
    for words in l_bodies:
        word_tokens= word_tokenize(words)
        filter_sentence = [fw for fw in word_tokens if not fw in stop_words]
        
        for n in range(len(filter_sentence)) :
            if filter_sentence[n] == 'collapsed' :
                filter_sentence[n]  = 'collapse'
            elif filter_sentence[n] == 'buildings':
                filter_sentence[n] = 'building'
        
        ## fall + fell => fall (less frequency of fall just go with fell) , collapsed +collapse => collapse
        #filter_sentence = nltk.pos_tag(filter_sentence)
        token_sentence.append(filter_sentence)


    #check how many words being used

    for i in range(len(token_sentence)) :    
        total_word_count += len(token_sentence[i])


    article_set ={}
    article_set['date'] = cd.datelist
    article_set['title'] = cd.titles
    article_set['bodies'] = token_sentence
    article_set['url'] = cr.lists

    df_article = pd.DataFrame(article_set, columns = ['date','title','bodies', "url"])
    df_article.to_pickle("/Users/macbookpro/Project_construction/Notebook/word2vec/df_articles.pkl")
    df_article_t = df_article.copy()
    
    #add weather, month column

    weather =[]
    month = []
    for i in range(len(df_article)) :
        
        if df_article.loc[i,'date'] is None :
            weather.append('None')
            month.append('None')
        else :
            if df_article.loc[i,"date"][4:6] == '03':
                weather.append('spring')
                month.append('march')
            elif df_article.loc[i,"date"][4:6] == '04' :
                weather.append('spring')
                month.append('april')
            elif df_article.loc[i,"date"][4:6] == '05' :
                weather.append('spring')
                month.append('may')
            elif df_article.loc[i,"date"][4:6] == "06" :
                weather.append('summer')
                month.append('june')
            elif df_article.loc[i,"date"][4:6] == "07" :
                weather.append('summer')
                month.append('july')
            elif df_article.loc[i,"date"][4:6] == "08" :
                weather.append('summer')
                month.append('august')
            elif df_article.loc[i,"date"][4:6] == "09" :
                weather.append('fall')
                month.append('september')
            elif df_article.loc[i,"date"][4:6] == "10" :
                weather.append('fall')
                month.append('october')
            elif df_article.loc[i,"date"][4:6] == "11" :
                weather.append('fall')
                month.append('november')
            elif df_article.loc[i,"date"][4:6] == "12" :
                weather.append('winter')
                month.append('december')
            elif df_article.loc[i,"date"][4:6] == "01" :
                weather.append('winter')
                month.append('january')
            elif df_article.loc[i,"date"][4:6] == "02" :
                weather.append('winter')
                month.append('february')
            else :
                weatehr.append('error')

    df_article.insert(3, "weather", weather)
    df_article.insert(4, "month", month)