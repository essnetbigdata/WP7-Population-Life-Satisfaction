<b>STEP 1. Preparing the training dataset based on Twitter</b><br/>
1.1.	Get the API keys<br/>
Use your Twitter account or register a new account and get API keys. It is necessary to collect information from Twitter.
After you log in, go to Settings and Privacy and create a new App using Apps pane.<br/>
1.2.	Change the source code of the file WP7_STEP1_collecting_tweets.py by adding the keys, country code and keyword you want to collect<br/>
# !!! put your keys in single quota in the four lines below<br/>
consumer_key = ''<br/>
consumer_secret = ''<br/>
access_token = ''<br/>
access_token_secret = ''<br/>
<br/>
# !!! REPLACE pl WITH YOUR COUNTRY CODE<br/>
language='pl'<br/>
<br/>
# !!! REPLACE THE keyword TO COLLECT INFORMATION BASED ON THE KEYWORD<br/>
keyword=":("<br/>
<br/>
1.3.	Execute the file<br/>
You can execute the file by writing:<br/>
python3 WP7_STEP1_collecting_tweets.py<br/>
If you have problems with Python on your computer, just ask Jacek for help.<br/>
Repeat the step 1.3 with different keywords to create several different files for the next task – identifying tweets. The results will be stored in the files: WP7_keyword_??????.csv.<br/>
1.4.	Manual work – identifying tweets<br/>
Based on your collected CSV files, add additional column named sentiment and try to identify each tweet with the following rules, according to the European Social Survey, Social Cohesion Survey and EU Statistics on Income and Living Conditions (EU-SILC): <br/>
1)	happy<br/>
2)	neutral<br/>
3)	calm<br/>
4)	upset<br/>
5)	depressed<br/>
6)	discouraged<br/>
7)	indeterminate<br/>
You can change the list according to your needs but for comparison purposes it would be better to collect the same list.
Based on this list the final results will be identified by Machine Learning algorithm.<br/>
<br/>
<b>STEP 2. Testing the training dataset</b><br/>
2.1. Combine all CSV files into one<br/>
You can just copy/paste to CSV file to have all sentiments in one CSV sheet.<br/>
No.	Tweet	Sentiment<br/>
1	Wieczorny spacer :) Coś przyjemnego na koniec dnia :D  #spacer #zima #odpoczynek	happy<br/>
2	#spacer w otoczeniu pięknej śnieżnej zimy #odpoczynek 	neutral <br/>
3	Trochę odpoczynku w rodzinnym mieście. #odpoczynek #weekend	neutral <br/>
Save this file as WP7_training_data.csv because it will be used in the next<br/> step.
2.2. Test the dataset with the training data<br/>
The goal of this step is to know the accuracy of your training dataset.<br/>
You have to execute the file like this:<br/>
python3 WP7_STEP2_testing_dataset.py<br/>
Then analyze the results, like this:<br/>
               precision    recall  f1-score   support<br/>
<br/>
        happy       0.62      0.75      0.68        56<br/>
      neutral       0.60      0.71      0.65        34<br/>
         calm       0.43      0.30      0.35        10<br/>
        upset       0.67      0.15      0.25        13<br/>
    depressed       0.59      0.62      0.60        21<br/>
  discouraged       0.59      0.50      0.54        20<br/>
indeterminate       0.00      0.00      0.00         3<br/>
<br/>
  avg / total       0.59      0.60      0.58       157<br/>
<br/>
It means that dataset still need some enhancement for a few keywords.<br/>
<br/>
<b>STEP 3. Collecting and providing the final results</b><br/>
3.1. Get the current tweets from timeline<br/>
You have to execute the third script to collect the current tweets.<br/>
python3 WP7_STEP3_collecting_timeline.py<br/>
Please note that it will be stored in the file:<br/>
WP7_population_datasource.csv<br/>
3.2. Provide the results<br/>
The goal of this point is to use training dataset to classify comments from the file generated in the point 3.1.<br/>
python3 WP7_STEP3_providing_results.py<br/>
