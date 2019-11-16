import csv
import itertools

# def write_out_file():
#     new_file = open("new_spam.csv", "w+")
#     headers = ["doesHaveLinks", "doesHaveSpammyWords", "LengthOfText", "NumberOfSymbols", "class", "message"]
#     i = 0
#     while i != len(headers):
#         new_file.write(headers[i])
#         new_file.write(",")
#         i += 1

def does_have_links(text_message):
    if "http" in text_message or ".com" in text_message or ".co.uk" in text_message:
        return True
    else:
        return False

def does_have_spammy_words(text_message):
    if "congratulations!" in text_message or "Â£" in text_message or "private!" in text_message or "std" in text_message or "FREE" in text_message or "4 info" in text_message or "POBOX" in text_message or "prize" in text_message or "rate call" in text_message or "to opt out" in text_message or "years or over" in text_message or "urgent" in text_message:
        return True
    else:
        return False

def get_length_of_text(text_message):
    return len(text_message)

def get_number_of_symbols(text_message):
    if text_message.isalnum():
        return False
    else:
        return True

def predict_spam(text_message):
    dhl = does_have_links(text_message)
    dhsw = does_have_spammy_words(text_message)
    if dhl == True or dhsw == True:
        return "spam"
    else:
        return "ham"

def main():
    CLASS_COLUMN = 0
    TEXT_MESSAGE = 1
    doesHaveLinks = 2
    doesHaveSpammyWords = 3
    LengthOfText = 4
    NumberOfSymbols = 5

    with open('spam1.csv', encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=','
        message_list = []
        class_list = []
        length_of_text_list = []
        number_of_symboles_list = []
        # for each text message
        for row in csv_reader:
            #returns "spam" if spam or "ham" if not spam
            predict_spam(row[TEXT_MESSAGE])
            #returns the text length in the text message
            get_length_of_text(row[TEXT_MESSAGE])
	        #returns the number of symbols in the text message
            get_number_of_symbols(row[TEXT_MESSAGE])
            #write new csv file
            # write_out_file()
            new_file = open("new_spam.csv", "w+")
            headers = ["doesHaveLinks", "doesHaveSpammyWords", "LengthOfText", "NumberOfSymbols", "class", "message"]
            i = 0
            while i != len(headers):
                new_file.write(headers[i])
                new_file.write(",")
                i += 1
            #append the features above to the new csv file
            new_file.write(predict_spam(row[TEXT_MESSAGE]))



main()
