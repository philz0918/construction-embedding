from collections import Counter, OrderedDict
from matplotlib import pyplot as plt

'''
distribution by
1. weather
2. weather by keyword
3. month
4. month by keyword
5. frequency of words
'''


def get_dist_weather(df) :
    spring_cnt = 0
    summer_cnt =0
    fall_cnt =0
    winter_cnt = 0
    none_cnt = 0
    for i in range(len(df)) :
        if df.loc[i,"weather"] =='spring' :
            spring_cnt +=1
        elif df.loc[i,"weather"] =='summer' :
            summer_cnt +=1
        elif df.loc[i,"weather"] =='fall' :
            fall_cnt +=1
        elif df.loc[i,"weather"] =='winter' :
            winter_cnt +=1
        else :
            none_cnt +=1
    
    fin_set = {}
    fin_set['spring'] = spring_cnt
    fin_set['summer'] = summer_cnt
    fin_set['fall'] = fall_cnt
    fin_set['winter'] = winter_cnt
    fin_set['none'] = none_cnt
    
    return fin_set

def get_dist_weather_keyword(df,key) :
    spring_cnt = 0
    summer_cnt =0
    fall_cnt =0
    winter_cnt = 0
    none_cnt = 0
    for i in range(len(df)) :
        if df.loc[i,"weather"] =='spring' :
            #print(type(df.loc[i,"bodies"]))
            if key in df.loc[i,"bodies"] :
                spring_cnt +=1
        elif df.loc[i,"weather"] =='summer' :
            if key in df.loc[i,"bodies"] :
                summer_cnt +=1
        elif df.loc[i,"weather"] =='fall' :
            if key in df.loc[i,"bodies"] :
                fall_cnt +=1
        elif df.loc[i,"weather"] =='winter' :
            if key in df.loc[i,"bodies"] :
                winter_cnt +=1
        else :
                none_cnt +=0
    
    fin_set_fire = {}
    fin_set_fire['spring'] = spring_cnt
    fin_set_fire['summer'] = summer_cnt
    fin_set_fire['fall'] = fall_cnt
    fin_set_fire['winter'] = winter_cnt
    fin_set_fire['none'] = none_cnt
    
    return fin_set_fire

def get_dist_month(df) :
    jan_cnt = 0
    feb_cnt = 0 
    mar_cnt = 0
    apr_cnt = 0 
    may_cnt = 0 
    jun_cnt = 0
    jul_cnt = 0
    aug_cnt = 0
    sep_cnt = 0
    ocb_cnt = 0
    nov_cnt = 0
    dec_cnt = 0
    none_cnt = 0
    for i in range(len(df)) :
        if df.loc[i,"month"] =='january' :
            #print(type(df.loc[i,"bodies"]))
       
            jan_cnt +=1
        elif df.loc[i,"month"] =='february' :
        
            feb_cnt +=1
        elif df.loc[i,"month"] =='march' :
        
            mar_cnt +=1
        elif df.loc[i,"month"] =='april' :
   
            apr_cnt +=1
        elif df.loc[i,"month"] =='may' :
     
            may_cnt +=1
        elif df.loc[i,"month"] =='june' :
            
            jun_cnt +=1
        elif df.loc[i,"month"] =='july' :
          
            jul_cnt +=1
        elif df.loc[i,"month"] =='august' :
           
            aug_cnt +=1
        elif df.loc[i,"month"] =='september' :
          
            sep_cnt +=1
        elif df.loc[i,"month"] =='october' :
           
            ocb_cnt +=1
        elif df.loc[i,"month"] =='november' :
            
            nov_cnt +=1
        elif df.loc[i,"month"] =='december' :
            
            dec_cnt +=1
        else :
            none_cnt +=1
    
    fin_set_mon = {}
    fin_set_mon['january'] = jan_cnt
    fin_set_mon['february'] = feb_cnt
    fin_set_mon['march'] = mar_cnt
    fin_set_mon['april'] = apr_cnt
    fin_set_mon['may'] = may_cnt
    fin_set_mon['june'] = jun_cnt
    fin_set_mon['july'] = jul_cnt
    fin_set_mon['august'] = aug_cnt
    fin_set_mon['september'] = sep_cnt
    fin_set_mon['octoboer'] = ocb_cnt
    fin_set_mon['november'] = nov_cnt
    fin_set_mon['december'] = dec_cnt
    fin_set_mon['none'] = none_cnt
    
    
    return fin_set_mon

def get_dist_month_keyword(df,key) :
    jan_cnt = 0
    feb_cnt = 0 
    mar_cnt = 0
    apr_cnt = 0 
    may_cnt = 0 
    jun_cnt = 0
    jul_cnt = 0
    aug_cnt = 0
    sep_cnt = 0
    ocb_cnt = 0
    nov_cnt = 0
    dec_cnt = 0
    none_cnt = 0
    for i in range(len(df)) :
        if df.loc[i,"month"] =='january' :
            #print(type(df.loc[i,"bodies"]))
            if key in df.loc[i,"bodies"] :
                jan_cnt +=1
        elif df.loc[i,"month"] =='february' :
            if key in df.loc[i,"bodies"] :
                feb_cnt +=1
        elif df.loc[i,"month"] =='march' :
            if key in df.loc[i,"bodies"] :
                mar_cnt +=1
        elif df.loc[i,"month"] =='april' :
            if key in df.loc[i,"bodies"] :
                apr_cnt +=1
        elif df.loc[i,"month"] =='may' :
            if key in df.loc[i,"bodies"] :
                may_cnt +=1
        elif df.loc[i,"month"] =='june' :
            if key in df.loc[i,"bodies"] :
                jun_cnt +=1
        elif df.loc[i,"month"] =='july' :
            if key in df.loc[i,"bodies"] :
                jul_cnt +=1
        elif df.loc[i,"month"] =='august' :
            if key in df.loc[i,"bodies"] :
                aug_cnt +=1
        elif df.loc[i,"month"] =='september' :
            if key in df.loc[i,"bodies"] :
                sep_cnt +=1
        elif df.loc[i,"month"] =='october' :
            if key in df.loc[i,"bodies"] :
                ocb_cnt +=1
        elif df.loc[i,"month"] =='november' :
            if key in df.loc[i,"bodies"] :
                nov_cnt +=1
        elif df.loc[i,"month"] =='december' :
            if key in df.loc[i,"bodies"] :
                dec_cnt +=1
        else :
                none_cnt +=0
    
    fin_set_mon = {}
    fin_set_mon['january'] = jan_cnt
    fin_set_mon['february'] = feb_cnt
    fin_set_mon['march'] = mar_cnt
    fin_set_mon['april'] = apr_cnt
    fin_set_mon['may'] = may_cnt
    fin_set_mon['june'] = jun_cnt
    fin_set_mon['july'] = jul_cnt
    fin_set_mon['august'] = aug_cnt
    fin_set_mon['september'] = sep_cnt
    fin_set_mon['octoboer'] = ocb_cnt
    fin_set_mon['november'] = nov_cnt
    fin_set_mon['december'] = dec_cnt
    fin_set_mon['none'] = none_cnt
    
    
    return fin_set_mon


def keyword_plotting(sort_dict,keyword) :
    
    def autolabel(rects):

        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    fig, ax = plt.subplots()
    rect1 = ax.bar(list(sort_dict.keys())[:-1],list(sort_dict.values())[:-1],width = 0.5, color ='gray')
    ax.set_ylabel('FREQUENCY', fontsize = 13)
    ax.set_xlabel(keyword, fontsize = 13)
    #ax.set_ylim(0,230)
    
    autolabel(rect1)  
    
    plt.xticks(day_list, rotation = 0)
    fig.tight_layout()
    plt.savefig("Figure/prediction/fire_"+keyword+".jpeg", dpi = 300)
    plt.show()

##tokensentence from dataframe
def frequency(token_sentence) :
    cnt_fire =0 
    cnt_fall =0
    cnt_collapse =0 
    cnt_people = 0
    cnt_building = 0
    for token in token_sentence :
        if 'fire' in token :
            cnt_fire +=1
        if 'collapse' in token :
            cnt_collapse +=1
        if 'fell' in token :
            cnt_fall +=1
        if 'building' in token :
            cnt_building +=1
        if 'people' in token :
            cnt_people +=1
            
    freq_dict = {}
    freq_dict['fire'] = cnt_fire
    freq_dict['fell'] = cnt_fall
    freq_dict['collapse'] = cnt_collapse
    freq_dict['building'] = cnt_building
    freq_dict['people'] = cnt_people
    
    plt.bar(list(freq_dict.keys()),freq_dict.values(),width = 0.5, color ='gray')
    plt.title("Frequency of keywords")
    plt.savefig('frequency_keyword.pdf')
 

if __name__ == "__main__" :
    
    #example of plotting
    '''
    dist_weather = get_dist_weather(df_article)
    keyword_plotting(dist_weather, 'fire')
    '''

