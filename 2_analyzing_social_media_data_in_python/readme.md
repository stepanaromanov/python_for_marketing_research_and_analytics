# Description 

I performed sentiment analysis using Python on the Customer Support on Twitter dataset—a comprehensive collection of tweets and responses intended to propel advancements in natural language understanding and conversational models. This endeavor not only contributed to the advancement of sentiment analysis techniques but also provided valuable insights into modern customer support practices and their impact, showcasing my proficiency in working with large-scale, real-world datasets and leveraging Python for insightful analysis.

# Customer Support on Twitter
https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter

# About Dataset

The sample related to SpotifyCares(<60k) tweets was made from original dataset (~2990k unique ids). 
The original dataset was filtered in pandas using operations:

```
import pandas as pd
data = pd.read_csv('twcs.csv')

# Filter by author id (Spotify Cares)
spotify_data = data[data['author_id'] == 'SpotifyCares'].reset_index()

# Get initial tweet id's
# Concatenate all responses in one column
all_responses = pd.concat([spotify_data['response_tweet_id'],spotify_data['in_response_to_tweet_id']]).dropna()

# Split responses to multiple tweets; then explode the data (make a new rows from splited lists) and create a list from it
responses_list = all_responses.str.split(',').explode().to_list()

# Convert all the items to integers
responses_list = [int(x) for x in responses_list if str(x) != 'nan']

# Remove duplicates by creating a set from the list
unique_responses = set(responses_list)

# Get full information about initial tweet id's
support_requests = data[data['tweet_id'].isin(unique_responses)].reset_index()

# Delete replies to themself
support_requests = support_requests[support_requests['author_id'] != 'SpotifyCares']

# export to csv
spotify_data.to_csv('spotify_cares.csv')
support_requests.to_csv('support_requests.csv')
```

Natural language remains the densest encoding of human experience we have, and innovation in NLP has accelerated to power understanding of that data, but the datasets driving this innovation don't match the real language in use today. The Customer Support on Twitter dataset offers a large corpus of modern English (mostly) conversations between consumers and customer support agents on Twitter, and has three important advantages over other conversational text datasets:

### Focused - Consumers contact customer support to have a specific problem solved, and the manifold of problems to be discussed is relatively small, especially compared to unconstrained conversational datasets like the reddit Corpus.
### Natural - Consumers in this dataset come from a much broader segment than those in the Ubuntu Dialogue Corpus and have much more natural and recent use of typed text than the Cornell Movie Dialogs Corpus.
### Succinct - Twitter's brevity causes more natural responses from support agents (rather than scripted), and to-the-point descriptions of problems and solutions. Also, its convenient in allowing for a relatively low message limit size for recurrent nets.

## Inspiration
The size and breadth of this dataset inspires many interesting questions:

### Can we predict company responses? Given the bounded set of subjects handled by each company, the answer seems like yes!
### Do requests get stale? How quickly do the best companies respond, compared to the worst?
### Can we learn high quality dense embeddings or representations of similarity for topical clustering?
### How does tone affect the customer support conversation? Does saying sorry help?
### Can we help companies identify new problems, or ones most affecting their customers?

## Acknowledgements
Dataset built with PointScrape.

## Content
The dataset is a CSV, where each row is a tweet. The different columns are described below. Every conversation included has at least one request from a consumer and at least one response from a company. Which user IDs are company user IDs can be calculated using the inbound field.

## tweet_id
A unique, anonymized ID for the Tweet. Referenced by response_tweet_id and in_response_to_tweet_id.

## author_id
A unique, anonymized user ID. @s in the dataset have been replaced with their associated anonymized user ID.

## inbound
Whether the tweet is "inbound" to a company doing customer support on Twitter. This feature is useful when re-organizing data for training conversational models.

## created_at
Date and time when the tweet was sent.

## text
Tweet content. Sensitive information like phone numbers and email addresses are replaced with mask values like __email__.

## response_tweet_id
IDs of tweets that are responses to this tweet, comma-separated.

## in_response_to_tweet_id
ID of the tweet this tweet is in response to, if any.

## Contributing
Know of other brands the dataset should include? Found something that needs to be fixed? Start a discussion, or email me directly at $FIRSTNAME@$LASTNAME.com!

## Acknowledgements
A huge thank you to my friends who helped bootstrap the list of companies that do customer support on Twitter! There are many rocks that would have been left un-turned were it not for your suggestions!

## Licensing
For commercial applications and use of full dataset, please contact stuart@thoughtvector.io.