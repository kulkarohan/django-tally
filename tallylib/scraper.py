﻿from concurrent.futures import ThreadPoolExecutor as Executor
from requests import Session
from lxml import html
import pandas as pd
import spacy
import scattertext as st

nlp = spacy.load("en_core_web_sm/en_core_web_sm-2.2.5")


def yelpScraper(bid, from_isbn=False):
    '''Takes a url, scrape site for reviews
    and calculates the term frequencies
    sorts and returns the top 10 as a json object
    containing term, highratingscore, poorratingscore.'''

    base_url = "https://www.yelp.com/biz/" # add business id
    api_url = "/review_feed?sort_by=date_desc&start="
    # bid = yelp_url.replace('https://www.yelp.com/biz/','')
    # if '?' in yelp_url:#deletes everything after "?" in url
    #     bid = yelp_url.split('?')[0]

    class Scraper():
        def __init__(self):
            self.data = pd.DataFrame()

        def get_data(self, n, bid=bid):
            with Session() as s:
                with s.get(base_url+bid+api_url+str(n*20)) as resp: #makes an http get request to given url and returns response as json
                    print(base_url+bid+api_url)
                    r = dict(resp.json()) #converts json response into a dictionary
                    _html = html.fromstring(r['review_list']) #loads from dictionary

                    dates = _html.xpath("//div[@class='review-content']/descendant::span[@class='rating-qualifier']/text()")
                    reviews = [el.text for el in _html.xpath("//div[@class='review-content']/p")]
                    ratings = _html.xpath("//div[@class='review-content']/descendant::div[@class='biz-rating__stars']/div/@title")

                    df = pd.DataFrame([dates, reviews, ratings]).T

                    self.data = pd.concat([self.data,df])

        def scrape(self): #makes it faster
            # multithreaded looping
            with Executor(max_workers=40) as e:
                list(e.map(self.get_data, range(10)))

    s = Scraper()
    s.scrape()
    df = s.data # converts scraped data into

    nlp.Defaults.stop_words |= {'will','because','not','friends','amazing','awesome','first','he','check-in','=','= =','male','u','want', 'u want', 'cuz','him',"i've", 'deaf','on', 'her','told','told him','ins', 'check-ins','check-in','check','I', 'i"m', 'i', ' ', 'it', "it's", 'it.','they','coffee','place','they', 'the', 'this','its', 'l','-','they','this','don"t','the ', ' the', 'it', 'i"ve', 'i"m', '!', '1','2','3','4', '5','6','7','8','9','0','/','.',','}

    corpus = st.CorpusFromPandas(df,
                             category_col=2,
                             text_col=1,
                             nlp=nlp).build()

    term_freq_df = corpus.get_term_freq_df()
    term_freq_df['highratingscore'] = corpus.get_scaled_f_scores('5.0 star rating')

    term_freq_df['poorratingscore'] = corpus.get_scaled_f_scores('1.0 star rating')
    dh = term_freq_df.sort_values(by= 'highratingscore', ascending = False)
    dh = dh[['highratingscore', 'poorratingscore']]
    dh = dh.reset_index(drop=False)
    dh = dh.rename(columns={'highratingscore': 'score'})
    dh = dh.drop(columns='poorratingscore')
    positive_df = dh.head(10)
    negative_df = dh.tail(10)
    results = {'positive': [{'term': pos_term, 'score': pos_score} for pos_term, pos_score in
                            zip(positive_df['term'], positive_df['score'])],
               'negative': [{'term': neg_term, 'score': neg_score} for neg_term, neg_score in
                            zip(negative_df['term'], negative_df['score'])]}
    return results