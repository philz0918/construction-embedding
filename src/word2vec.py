from gensim.models import Word2Vec
import networkx as nx
from matplotlib.backends.backend_pdf import PdfPages






# generate similar word with threshold and graph 

key_list = ['fire','fell','collapse','building','people']
def network_gen(key_list,thres,sav_name) :
    set_of_g={}
    for key in key_list :
        
        
        sim_list = model.similar_by_vector(key, topn=100, restrict_vocab=None)
        network = [sim_list[i][0] for i in range(len(sim_list)) if sim_list[i][1] >= thres]
        network_df = [sim_list[i] for i in range(len(sim_list)) if sim_list[i][1] >= thres]
  
        
        set_of_g[key] = network
      
        df_word = pd.DataFrame(network_df, columns= ['Word', 'Similarity'])
        df_word.to_csv('Similar_words_100/'+key+str(thres)+'.csv')
    
    #generate graph
    #print(set_of_g)
    G = nx.Graph(set_of_g)
    nx.write_gml(G, "Network/"+sav_name+".gml")
    
    return "Success!"

if __name__ == "__main__" :
    model = Word2Vec(token_sentence, size = 400, window=5, min_count=200, workers=3, sg=0, iter=5)
    model.save("filename.model")
    '''
    check similarty between 5 keywords (total 10)
    fire - collapse, fire - fell, fire - people, fire - building
    collapse - fell, collapse - people , collapse - building
    fell - people , fell - building
    building - people 
    '''
    sb1 = model.similarity('building','collapse')
    sb2 = model.similarity('building','fire')
    sb3 = model.similarity('building','people')
    sb4 = model.similarity('building','fell')
    sb5 = model.similarity('fire','collapse')
    sb6 = model.similarity('fire','fell')
    sb7 = model.similarity('fire','people')
    sb8 = model.similarity('collapse','fell')
    sb9 = model.similarity('collapse','people')
    sb10 = model.similarity('people','fell')
    '''
    print('building and collapse', model.similarity('building','collapse'))  ## similarity between words
    print('building and fire', model.similarity('building','fire')) 
    print('building and people', model.similarity('building','people')) 
    print('building and fell', model.similarity('building','fell'))
    print('fire and collapse', model.similarity('fire','collapse'))
    print('fire and fell', model.similarity('fire','fell'))
    print('fire and people', model.similarity('fire','people'))
    print('collapse and fell', model.similarity('collapse','fell'))
    print('collpase and people', model.similarity('collapse','people'))
    print('people and fell', model.similarity('people','fell'))
    '''
    sim_between = [('building and collapse' , "%.3f" % sb1),('building and fire',"%.3f" % sb2), 
                ('building and people ',"%.3f" % sb3), 
                ('building and fell',"%.3f" % sb4),('collapse and fell', "%.3f" % sb8), 
                ('collapse and people',"%.3f" % sb9),('fire and collapse',"%.3f" % sb5), 
                ('fire and fell', "%.3f" % sb6), ('fire and people',"%.3f" % sb7),
                ('people and fell', "%.3f" % sb10)]
    df_sim_between = pd.DataFrame(sim_between, columns=['Words', 'Similarity'])
    df_sim_between.to_csv('Figure/sim_between_0521.csv')

    # top 20 data for graph coloring, top 50 data for showing, top 100 data for make network graph

    sim_list_fire = model.similar_by_vector('fire', topn=20, restrict_vocab=None)
    sim_list_fall = model.similar_by_vector('fell', topn=20, restrict_vocab=None)
    sim_list_collapse = model.similar_by_vector('collapse', topn=20, restrict_vocab=None)
    sim_list_building = model.similar_by_vector('building', topn=20, restrict_vocab=None)
    sim_list_people = model.similar_by_vector('people', topn=20, restrict_vocab= None)

    # list of similiar 20 words -> generating color in UMAP
    sim_fire_word = []
    for i in range(len(sim_list_fire)) :
        sim_fire_word.append(sim_list_fire[i][0])
    #print(sim_fire_word)
    sim_fell_word = []
    for i in range(len(sim_list_fall)) :
        sim_fell_word.append(sim_list_fall[i][0])
    #print(sim_fall_word)
    sim_collapse_word =[]
    for i in range(len(sim_list_collapse)):
        sim_collapse_word.append(sim_list_collapse[i][0])
    #print(sim_collapse_word)
    sim_building_word = []
    for i in range(len(sim_list_building)):
        sim_building_word.append(sim_list_building[i][0])
    #print(sim_building_word)
    sim_people_word = []
    for i in range(len(sim_list_people)):
        sim_people_word.append(sim_list_people[i][0])
    #print(sim_people_word)

    keywords = ['fire','fell','collapse','building','people']
    keyword_dict = {}

    for keyword in keywords :
        a = 'sim_%s_word'%(keyword)
        ##local varible same name with a
        
        keyword_dict[keyword] = locals()[a]
        
    df_keyword = pd.DataFrame.from_dict(keyword_dict)
    #df_keyword.to_csv('keyword_simlist.csv')

    fig, ax = plt.subplots(figsize=(12,4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText = df_keyword.values, colLabels = df_keyword.columns, loc = 'center')
    pp = PdfPages("simlist.pdf")
    pp.savefig(fig,bbox_inches = 'tight')


