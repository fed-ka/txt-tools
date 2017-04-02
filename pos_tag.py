# -- pos tagger by fedor k.
# -- must have nltk installed. you must download the "full" POS-taggers from Stanford found here http://nlp.stanford.edu/software/tagger.shtml (should be 124MB). After you download, extract into your working directory, so that the folder "stanford-postagger-full-2015-12-09" is visible.
# -- to change the language, you must change the "model" variable, seen below. Use "english-bidirectional-distsim.tagger" for English, "french.tagger" for French, and "german-dewac.tagger" for German. Look at the models folder, there are options for other languages as well.


from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
import os
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


#working directory on desktop
# these must be linked exactly. you can put the full path name
jar = './stanford-postagger-full-2015-12-09/stanford-postagger.jar'
# the "model" below must be linked to the language .tagger file that you wan tto use
model = './stanford-postagger-full-2015-12-09/models/french.tagger'
tagger = StanfordPOSTagger(model, jar)

# define input and output folders. these can be named anything as long as they correspond to the directories that you're working on.
files_input = "./All_NPOS/"
files_output = "./All_POS/"

def returntags( string ):
    text = tagger.tag(word_tokenize( string.decode('utf-8') ))
    POS = [pos for pos, pos in text]
    pos_line =' '.join(str(p) for p in POS)
    #print pos_line
    return pos_line;

for filename in os.listdir(files_input):
    if filename.endswith(".txt"):
        with open((files_input + filename), "r") as infile:
            print filename
            for line in infile:
                tagged = returntags(line).decode().encode('utf-8')
                print tagged
                w = codecs.open(files_output + filename, "a", encoding='utf-8', errors="ignore")
                w.write(tagged + "\n")
