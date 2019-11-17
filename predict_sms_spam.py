import csv
import itertools

def write_out_file():
    new_file = open("new_spam.csv", "w+")
    columns = ["class", "message", "doesHaveLinks", "doesHaveSpammyWords", "LengthOfText", "NumberOfSymbols"]
    i = 0
    while i != len(columns):
        new_file.write(columns[i])
        new_file.write(",")
        i += 1
    new_file.write("\n")
    return new_file

def add_features_to_file(file, class_list, message_list, dsl_list, dhsw_list, lot_list, nos_list):
    with open("new_spam.csv", encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        file.write(class_list)

def does_have_links(text_message):
    if "http" in text_message or ".com" in text_message or ".co.uk" in text_message or "www" in text_message:
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
    classCol = 0
    messageCol = 1
    with open('spam_test.csv', encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        message_list = []
        class_list = []
        dsl_list = []
        dhsw_list = []
        lot_list = []
        nos_list = []
        #write out file
        new_file = write_out_file()
        # for each text message
        for row in csv_reader:
            #returns "spam" if spam or "ham" if not spam
            class_list.append(predict_spam(row[messageCol]))
            #returns the text length in the text message
            lot_list.append(get_length_of_text(row[messageCol]))
	        #returns the number of symbols in the text message
            nos_list.append(get_number_of_symbols(row[messageCol]))
            dhsw_list.append(does_have_links(row[messageCol]))
            dsl_list.append(does_have_spammy_words(row[messageCol]))
            message_list.append(row[messageCol])
        #write_out_file() and append the features above to the new csv file
        add_features_to_file(new_file, class_list, message_list, dsl_list, dhsw_list, lot_list, nos_list)




main()
