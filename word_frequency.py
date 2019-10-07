import string
import operator

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    word_count_dict = {}
    with open(file) as opened_file:
        line = opened_file.readline()
        while line:
            line = line.lower()
            table = str.maketrans({key: None for key in string.punctuation})
            line = line.translate(table)
            split_line = line.split()
            for word in split_line:
                if word in STOP_WORDS:
                    continue
                elif word in word_count_dict.keys():
                    word_count_dict[word] += 1
                elif word not in word_count_dict.keys():
                    word_count_dict[word] = 1
            line = opened_file.readline()
    sorted_word_tup = sorted(word_count_dict.items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_word_tup:
        word = item[0]
        ocur = item[1]
        ast = ''
        for _ in range(ocur):
            ast = ast + '*'
        print (f"{word} | {ocur} {ast}")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
