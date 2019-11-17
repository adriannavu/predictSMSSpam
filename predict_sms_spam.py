import csv

# returns new csv file with first row written out
def write_file():
    new_file = open("sms_spam_detection.csv", "w+")
    # initialize first row headers
    columns = ["doesHaveLinks", "doesHaveSpammyWords", "LengthOfText", "NumberOfSymbols", "class"]
    i = 0
    while i != len(columns):
        new_file.write(columns[i])
        new_file.write(",")
        i += 1
    new_file.write("\n")
    return new_file

# returns the new csv file with the new features
def add_features_to_file(file, class_list, dhl_list, dhsw_list, lot_list, nos_list, file_length):
    # start from the second row to avoid "v1" and "v2" becoming data points
    i = 1
    while i < file_length:
        file.write(str(dhl_list[i]))
        file.write(",")
        file.write(str(dhsw_list[i]))
        file.write(",")
        file.write(str(lot_list[i]))
        file.write(",")
        file.write(str(nos_list[i]))
        file.write(",")
        file.write(class_list[i])
        file.write("\n")
        i += 1

# returns True if text message has links and False otherwise
def does_have_links(text_message):
    if "http" in text_message or ".com" in text_message or ".co.uk" in text_message or "www" in text_message:
        return True
    else:
        return False

# returns True if text message has spammy words and False otherwise
def does_have_spammy_words(text_message):
    if "congratulations!" in text_message or "Â£" in text_message or "private!" in text_message or "std" in text_message or "FREE" in text_message or "4 info" in text_message or "POBOX" in text_message or "prize" in text_message or "rate call" in text_message or "to opt out" in text_message or "years or over" in text_message or "urgent" in text_message:
        return True
    else:
        return False

# returns the number of characters including spaces in the text message
def get_length(text_message):
    return len(text_message)

# returns the number of symbols in the text message
def get_number_of_symbols(text_message):
    count = 0
    symbols = [',', '.', ';', ':', '<', '>', '?', '/', '[', ']', '{', '}', '\'', '|', '!', '@', '#', '$', '£', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']
    for char in text_message:
        for symbol in symbols:
            if char == symbol:
                count += 1
    return count

# returns "spam" if spam or "ham" if not spam
def predict_spam(text_message):
    dhl = does_have_links(text_message)
    dhsw = does_have_spammy_words(text_message)
    nos = get_number_of_symbols(text_message)
    lot = get_length(text_message)
    if dhsw == False and lot <= 99 and dhl == False:
        return "ham"
    elif dhsw == False and lot <= 99 and dhl == True and nos <= 4:
        return "ham"
    elif dhsw == False and lot <= 99 and dhl == True and nos > 4:
        return "spam"
    elif dhsw == False and lot > 99 and dhl == False and lot <= 131:
        return "ham"
    elif dhsw == False and dhl == False and 131 < lot <= 160 and nos <= 8:
        return "ham"
    elif dhsw == False and dhl == False and 131 < lot <= 160 and 8 < nos <= 9:
        return "spam"
    elif dhsw == False and dhl == False and 131 < lot <= 160 and 9 < nos <= 14:
        return "ham"
    elif dhsw == False and dhl == False and nos <= 14 and 160 < lot <= 164:
        return "spam"
    elif dhsw == False and dhl == False and nos <= 14 and lot > 164:
        return "ham"
    elif dhsw == False and dhl == False and nos > 14 and lot > 131:
        return "ham"
    elif dhsw == False and dhl == True and lot > 99:
        return "spam"
    else:
        return "spam"

def main():
    classCol = 0
    messageCol = 1
    with open('spam.csv', encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        class_list = []
        dhl_list = []
        dhsw_list = []
        lot_list = []
        nos_list = []
        new_file = write_file()
        new_file_length = 0
        for row in csv_reader:
            # used to create weka decision tree
            class_list.append(row[classCol])
            # use to predict spam
            class_list.append(predict_spam(row[messageCol]))
            dhl_list.append(does_have_links(row[messageCol]))
            dhsw_list.append(does_have_spammy_words(row[messageCol]))
            lot_list.append(get_length(row[messageCol]))
            nos_list.append(get_number_of_symbols(row[messageCol]))
            new_file_length += 1
        add_features_to_file(new_file, class_list, dhl_list, dhsw_list, lot_list, nos_list, new_file_length)

main()
