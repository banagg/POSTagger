# POSTagger

## About
1. A part-of-speech tagger made during a college project in 2019.
2. The program tries to assign part-of-speech labels (sense labels) to the words in a given sentence. Since same words can be used for different meanings in different contexts it is important to know that which word refers to which context for a given sentence.
3. An API has been made for the process which can be called after running the ***wsgi.py*** file. The input is also paramterised for English, Detailed English and Hindi.

## Working
1. Data was collected from the **Brown** corpus for English and the **Indian** corpus for Hindi.
2. A preprocessing file ***NLTKTrainer.py*** was then run to get the different models to get the frequency counts for different kinds of patterns.
3. The processed file (made in accordance with the rules for HMM) was then run using a Hidden Markov Model (functioning checked from the web) to get the desired predictions for POS for the words in the given sentence.
4. The API **GET /v1/pos-tag?lc=&q=** takes in two paramters as input. The language code (lc) depicting the different languages (in this case three values *En*, *Hi* and *EnDetailed*) and the query (q) depicts the sentence which needs to broken down into the required POS.
5. The results are then presented in form of a list where each word is mapped along with its POS.
