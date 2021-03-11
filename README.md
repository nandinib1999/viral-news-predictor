# viral-news-predictor

![img](https://beconnected.esafety.gov.au/pluginfile.php/52815/mod_resource/content/12/fake-news-hero-img.jpg)

### About Project
There are countless sources of fake news nowadays and continue to spread false information 24/7. It is difficult to classify whether a news is fake or genuine. We need intelligent systems to identify the hidden patterns in the fake news and help us in stopping the spreading the misinformation. Many political parties and extremist groups also spread fake news during the elections or riots to create a bias within the citizens. According to sources, during Lok Sabha elections 2019, fake news was shared over two million times on social media.

### Libraries
1. BeautifulSoup
2. Tensorflow 2.x
3. Keras
4. wordcloud
5. nltk
6. sklearn

### Data
I scraped the news articles from NYTimes and NewsPunch for real & fake news using BeautifulSoup 4. 

![img](https://i.imgur.com/tWrmuSt.png)
<small>Word Cloud of Fake News</small>

![img](https://i.imgur.com/VTrPY63.png)
<small>Word Cloud of Real News</small>

### Approach
I trained two different models for the task of detecting fake news:
1. Simple DNN sequential model with TF-IDF
2. Model using LSTM with Glove Embeddings

### Evaluation
For the performane evaluation, we considered "accuracy" as the metric.
- Model 1: Accuracy: 0.899
- Model 2: Accuracy: 0.993 
