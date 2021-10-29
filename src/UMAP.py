from umap import UMAP
from gensim.models import Word2Vec
'''
From word2vec.py...
model, sim_*_word 

'''
if __name__ == "__main__" :
    #UMAP
    model = Word2Vec.model.load("path")

    reducer = UMAP(n_neighbors =5, min_dist =0.1, n_components = 2, verbose = True)
    X = model[model.wv.vocab]
    #list of word
    X_l = list(model.wv.vocab)

    #Embedding to 2 dimension
    cluster_embedding = reducer.fit_transform(X)
    #get coordination
    df = pd.DataFrame(cluster_embedding)


    fig = plt.figure()
    fig.set_size_inches(50,30)
    ax = fig.add_subplot(1,1,1)

    ax.scatter(df[0],df[1])

    for i, txt in enumerate(X_l):
        
        if txt == 'fire' :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]), color = 'red', fontsize=30)
        elif txt in sim_fire_word :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]), color ='red', fontsize=8)
            
        elif txt =='fell' :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]),color='green', fontsize=30)
            
        elif txt in sim_fell_word :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]), color ='green', fontsize=8)  
            
        elif txt =='collapse' :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]), color = 'blue', fontsize=30)
        elif txt in sim_collapse_word :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]), color ='blue', fontsize=8)
        
        elif txt =='building' :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]), color ='orange', fontsize=30)
        elif txt in sim_building_word :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]), color ='orange', fontsize=8)

        elif txt =='people' :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]),color = 'purple', fontsize=30)
        elif txt in sim_people_word :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]), color ='purple', fontsize=8)
        else :
            ax.annotate(txt, (df.loc[i][0],df.loc[i][1]), fontsize=8)

    plt.title ("Word Embdding results with UMAP", fontsize = 20)
    plt.savefig('fire_word2vec_0521_best_fell.pdf')