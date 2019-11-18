# SMS Spam Detection

Uses basic machine learning algorithm to predict whether a message is spam.

## Functions
1. Used write_file() to create new csv file with first row written out
2. Used apend() to pass objects (row[classCol] and/or row[messageCol]) into existing lists (class_list, lot)list, nos_list, dhsw_list, dsl_list)
3. Used predict_spam(text_message) to determine whether or not text_message was likely spam
4. Used get_length(text_message) to determine the number of characters (including spaces) in text_message
5. Used get_number_of_symbols(text_message) to determine the number of symbols in text_message
6. Used does_have_links(text_message) to determine if text_message has links
7. Used does_have_spammy_words(text_message) to determine if text_message had spammy words
8. Used add_features_to_file(new_file, class_list, dsl_list, dhsw_list, lot_list, nos_list, new_file_length) to append new featu
res to csv file

## Data Structure
Used lists to track each text_message's class, does because order matters; each row in sms_spam_detection.csv refers to a different text_message.

## Results
There were 131/5566 incorrect classes in sms_spam_detection.csv after calling predict_spam(text_message). Based on the given dataset, the SMS Spam Detection tool is 97.6% accurate.

I would try to improve this model by testing the algorithm on another dataset to see if it is just as accurate. I would also try to improve does_have_spammy_words(text_message) by adding more possibly spammy words. To account for text messages in different languages, I would want to improve both does_have_spammy_words(text_message) and get_number_of_symbols(text_message) to include other symbols and spammy words frequently used in other languages besides English.

Nevertheless, I learned a good deal about the technicalities of basic machine learning in Python. I learned how to create decision trees, how to open .csv files, how to write .csv files without the use of external libraries, and how to make use of data structures in real-world scenarios.
