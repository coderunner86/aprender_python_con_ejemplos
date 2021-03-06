# Here are all the installs and imports you will need for your word cloud script and uploader widget
#Este es un proyecto final del curso "Crash course on Python" de Google en copursera: https://www.coursera.org/learn/python-crash-course
#es desarrollado en Jupyter Notebook
"""!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload
"""
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
file_contents=open("void.txt") #Se debe subir un archivo txt de cualquier libro de tu preferencia
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    #En mi caso por ser de habla hispana he usado el cuento "vacío" de Andres Caicedo, escritor caleño (Colombia)
    punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["El", "a", "los" "la" "si", "es", "ella", "de", "y", "o", "una", "como", "yo" , "mi", \
     "nosotros", "nuestro", "nuestra", "usted", "su", "suyo", "él", "ella", "ellos", \
     "qué", "cuál", "quién", "esto", "eso", "soy", "son", "fue", "fueron", "se", "han sido", "siendo", \
     "Tener", "tiene", "tenía", "hacer", "sí", "pero", "por", "con", "de", "aquí", "cuando ", "donde", "como", \
     "todos", "cualquiera", "ambos", "cada uno", "pocos", "más", "algunos", "tales", "no", "ni", "también", "muy", "pueden ", "será sólo"]
    
    # LEARNER CODE START HERE
    #Este es el codigo pedido por el proyecto para plotear la nube de palabras
    result={}
    a =file_contents.split()
    for words in a:
        if words in uninteresting_words:
            pass
        else:
            for letter in words:
                if letter in punctuations:
                    letter.replace(punctuations, "")
            if words not in result.keys():
                result[words] = 0
            else:
                result[words]+=1

    #wordcloud
    cloud = wordcloud.WordCloud(width=900,height=500, max_words=1628,relative_scaling=1,normalize_plurals=False)
    cloud.generate_from_frequencies(result)
    return cloud.to_array()

    # Display your wordcloud image
#Aquí graficamos la nube de palabras
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()