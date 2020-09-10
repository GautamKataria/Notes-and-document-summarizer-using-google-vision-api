import os
import io
from google.cloud import vision
from google.cloud.vision import types
from deepsegment import DeepSegment

import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'google-vision-service-acc-token.json'

client = vision.ImageAnnotatorClient()

folder_path = r'C:\Users\Gautam\Desktop\Meeting summarisation\Images'
image_file = input("enter the file name: ") ### Giving input image
#image_file = 'sample_image2_copy.jpg'
file_path = os.path.join(folder_path, image_file)

with io.open(file_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content = content)
response = client.document_text_detection(image = image)
extracted_text = response.full_text_annotation.text
print(extracted_text)

text123 = extracted_text
segmenter = DeepSegment()
segmented_text=segmenter.segment_long(text123)
#print("length = ", len(text123))
print("\n These are the different sentences we recognized and segmented accordingly \n",segmented_text)
numbersentences = len(segmented_text)
numbersummarization = (numbersentences)//2  ### This is the number of sentences in final summarization
#print(numbersentences,numbersummarization)

finalstring = ' '.join(map(str, segmented_text))
print("\n This is the final paragraph extracted: \n",finalstring)
#print(type(finalstring))

parser = PlaintextParser.from_string(finalstring, Tokenizer('english'))
# print("\n", parser, "\n")
# summarizer = LexRankSummarizer()      ## For lexrank summarizer
# summary = summarizer(parser.document,3)
# print(summary)
# print("\n printing final summarisation")
# for sentence in summary:
#     print(sentence, "\n")


# from sumy.summarizers.luhn import LuhnSummarizer  ## For luhn-summarizer
# luhn_summarizer = LuhnSummarizer()
# l_summary = luhn_summarizer(parser.document,3)
# print("\n printing luhn summarisation")
# for sentence in l_summary:
#     print(sentence, "\n")

## We are currently using Lsa summarizer with stemming for the best results in our case:

from sumy.summarizers.lsa import LsaSummarizer
# lsa_summarizer = LsaSummarizer()
# lsa_summary = lsa_summarizer(parser.document,3)
# print("\n printing lsa summarisation")
# for sentence in lsa_summary:
#     print(sentence, "\n")

from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
summarizer_lsa2 = LsaSummarizer()
summarizer_lsa2 = LsaSummarizer(Stemmer("english"))
summarizer_lsa2.stop_words = get_stop_words("english")

summary2 = summarizer_lsa2(parser.document, numbersummarization)  ## number summarization is the no of sentences of summarization
print("\n printing lsa with stopwords summarisation")
for sentence in summary2:
    print(sentence, "\n")




