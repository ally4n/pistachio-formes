import pandas as pd
import re
def clean_sentence(sentence):
    output_str = re.sub(r'[-,.&=?_<>|}#^;:£$½%*+/@]+', ' ', sentence).strip()
    output_str = re.sub(r'\s+', ' ', output_str)
    output_str = output_str.lower()
    return output_str