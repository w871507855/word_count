# endcoding: utf-8
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')

def count(request):
    user_word = request.GET['text']
    total_count = len(user_word)
    word_dict = {}

    for word in user_word:
        if word not in word_dict:
            word_dict[word] =1
        else:
            word_dict[word] +=1

    worddict = sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request, 'count.html',{'count':total_count,'word':user_word,'w_dict':word_dict,'w':worddict})