class TextUtils():

    def count_words(self,data):
        words=data.split(" ")
        return len(words)

    def words_frequency(self,data):
        data_list=data.split(" ")
        words_set=set(data_list)
        elements_list=[]
        for i in words_set:
            data_dict={}
            data_dict['key']=i
            data_dict['count']=data_list.count(i)
            elements_list.append(data_dict)
        return elements_list

