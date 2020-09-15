# Notes-and-document-summarizer-using-google-vision-api

## The following repository hosts code for a notes/document summarizer using NLP

### requirements:
##### Install sumy, deepsegment
##### setup google-vision api : [example here](https://www.youtube.com/watch?v=wfyDiLMGqDM)

### Setup:
#### Change the path of google vision api json file to your own path
#### Change folder path where your image is saved

### Working:

#### 1) Run the extract_test.py file
#### 2) Give it the name of the image
#### 3) The program extracts text from the image(it can be a printed text or even handwritten text)
#### 4) It will then orgnaise it into a coherent paragraph
#### 5) The program summarizes the text through NLP by using Lsa summarizer in conjunction with stopwords and stemming.
#### 6) Finally, it displays the summarization at the end. (the length of summarization is half of the number of sentences detected)

### Improvements:
We can add some image preprocessing so that it is easier for the google-vision api to detect text correctly but in general it does the job quite well even without it.
