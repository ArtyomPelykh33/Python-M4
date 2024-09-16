import re

original_text = r"""homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# format original text
def format_text(text):
    lower_text = text.lower()
    text_splitted_by_rows = lower_text.splitlines()
    text_without_non_breaking_spaces = ''.join(text_splitted_by_rows).replace('\xa0', '')
    text_splitted_by_rows = text_without_non_breaking_spaces.split(". ")
    text_capitalize_first_character = [a.capitalize() for a in text_splitted_by_rows]
    text_original_format = '.\n'.join(text_capitalize_first_character)
    text2 = text_original_format.replace('\n', '\n  ')
    text3 = text2.replace(':', ':\n ')
    return text3

# find last word of each sentence, form a new sentence of them and insert it to existed text
def make_new_sentence(text):
    sent = re.split(r'[.!?]\s*', text)
    last_words = [sent.split()[-1] for sent in sent if sent]
    new_sentence = ''.join(last_words).capitalize() + '.'
    sentences = re.split(r'([.!?]\s*)', text)
    for i in range(len(sentences)):
        if sentences[i].endswith('paragraph'):
            sentences.insert(i + 2, '' + new_sentence + '\n  ')
            break
    updated_text = ''.join(sentences)
    return updated_text

# replace 'iz' with 'is' when it is a mistake
def replace_mistakes(text):
    formatted_text = text.replace(' iz', ' is')
    return formatted_text

# count all spaces in text, including whitespaces
def calculate_all_spaces(text):
    number_of_spaces = text.count(' ')
    return number_of_spaces

final_text = replace_mistakes(make_new_sentence(format_text(original_text)))

print(final_text, "\nNumber of spaces: ", calculate_all_spaces(final_text))

