import csv
import itertools

# returns new csv file with first row written out
def write_file():
    new_file = open("new_spam.csv", "w")
    # initialize first row headers
    columns = ["class", "doesHaveLinks", "doesHaveSpammyWords", "LengthOfText", "NumberOfSymbols", "message"]
    i = 0
    while i != len(columns):
        new_file.write(columns[i])
        new_file.write(",")
        i += 1
    new_file.write("\n")
    return new_file

# returns the new csv file with the new features
def add_features_to_file(file, class_list, message_list, dsl_list, dhsw_list, lot_list, nos_list, file_length):
    # if message contains comma, replace it with ~
    for message in message_list:
        message.replace(",", "~")
    # start from the second row to avoid "v1" and "v2" becoming data points
    i = 1
    while i < file_length:
        file.write(class_list[i])
        file.write(",")
        file.write(str(dsl_list[i]))
        file.write(",")
        file.write(str(dhsw_list[i]))
        file.write(",")
        file.write(str(lot_list[i]))
        file.write(",")
        file.write(str(nos_list[i]))
        file.write(",")
        file.write(str(message_list[i]))
        file.write("\n")
        i += 1
    # if message contains ~, replace it with comma
    for char in file:
        char.replace("~", ",")

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

# returns the text length in the text message
def get_length(text_message):
    return len(text_message)

# returns the number of symbols in the text message
def get_number_of_symbols(text_message):
    if text_message.isalnum():
        return False
    else:
        return True

# returns "spam" if spam or "ham" if not spam
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
    with open('spam.csv', encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        message_list = []
        class_list = []
        dsl_list = []
        dhsw_list = []
        lot_list = []
        nos_list = []
        new_file = write_file()
        in_file_length = 0
        for row in csv_reader:
            class_list.append(predict_spam(row[messageCol]))
            lot_list.append(get_length(row[messageCol]))
            nos_list.append(get_number_of_symbols(row[messageCol]))
            dhsw_list.append(does_have_links(row[messageCol]))
            dsl_list.append(does_have_spammy_words(row[messageCol]))
            message_list.append(row[messageCol])
            in_file_length += 1
        add_features_to_file(new_file, class_list, message_list, dsl_list, dhsw_list, lot_list, nos_list, in_file_length)

main()
