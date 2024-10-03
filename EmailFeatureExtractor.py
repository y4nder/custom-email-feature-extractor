import numpy as np
import re
from collections import Counter

class EmailFeatureExtractor:
    def __init__(self, email_text: str):
        self.email_text = email_text
        self.total_words = 0
        self.total_chars = len(email_text)
        self.word_freq = {
            'word_freq_make': 0, 'word_freq_address': 0, 'word_freq_all': 0,
            'word_freq_3d': 0, 'word_freq_our': 0, 'word_freq_over': 0,
            'word_freq_remove': 0, 'word_freq_internet': 0, 'word_freq_order': 0,
            'word_freq_mail': 0, 'word_freq_receive': 0, 'word_freq_will': 0,
            'word_freq_people': 0, 'word_freq_report': 0, 'word_freq_addresses': 0,
            'word_freq_free': 0, 'word_freq_business': 0, 'word_freq_email': 0,
            'word_freq_you': 0, 'word_freq_credit': 0, 'word_freq_your': 0,
            'word_freq_font': 0, 'word_freq_000': 0, 'word_freq_money': 0,
            'word_freq_hp': 0, 'word_freq_hpl': 0, 'word_freq_george': 0,
            'word_freq_650': 0, 'word_freq_lab': 0, 'word_freq_labs': 0,
            'word_freq_telnet': 0, 'word_freq_857': 0, 'word_freq_data': 0,
            'word_freq_415': 0, 'word_freq_85': 0, 'word_freq_technology': 0,
            'word_freq_1999': 0, 'word_freq_parts': 0, 'word_freq_pm': 0,
            'word_freq_direct': 0, 'word_freq_cs': 0, 'word_freq_meeting': 0,
            'word_freq_original': 0, 'word_freq_project': 0, 'word_freq_re': 0,
            'word_freq_edu': 0, 'word_freq_table': 0, 'word_freq_conference': 0,
        }
        self.char_freq = {
            'char_freq_;': 0, 'char_freq_(': 0, 'char_freq_[': 0,
            'char_freq_!': 0, 'char_freq_$': 0, 'char_freq_#': 0
        }
        self.capital_run_length_average = 0
        self.capital_run_length_longest = 0
        self.capital_run_length_total = 0

    def calculate_word_frequencies(self):
        # Tokenize the email text
        words = re.findall(r'\b\w+\b', self.email_text.lower())
        self.total_words = len(words)
        
        # Count frequencies
        word_counts = Counter(words)
        
        for word in self.word_freq.keys():
            word_name = word.split('_')[-1]
            self.word_freq[word] = 100 * word_counts[word_name] / self.total_words if self.total_words > 0 else 0

    def calculate_char_frequencies(self):
        for char in self.char_freq.keys():
            char_name = char.split('_')[-1]
            self.char_freq[char] = 100 * self.email_text.count(char_name) / self.total_chars if self.total_chars > 0 else 0

    def calculate_capital_run_lengths(self):
        capital_lengths = [len(seq) for seq in re.findall(r'[A-Z]+', self.email_text)]
        if capital_lengths:
            self.capital_run_length_average = np.mean(capital_lengths)
            self.capital_run_length_longest = max(capital_lengths)
            self.capital_run_length_total = sum(capital_lengths)
        else:
            self.capital_run_length_average = 0
            self.capital_run_length_longest = 0
            self.capital_run_length_total = 0

    def extract_features(self):
        self.calculate_word_frequencies()
        self.calculate_char_frequencies()
        self.calculate_capital_run_lengths()
        
        # Print feature values
        print("Word Frequencies:")
        for word, freq in self.word_freq.items():
            print(f"{word}: {freq:.2f}")
        
        print("\nCharacter Frequencies:")
        for char, freq in self.char_freq.items():
            print(f"{char}: {freq:.2f}")
        
        print("\nCapital Run Lengths:")
        print(f"Average: {self.capital_run_length_average:.2f}")
        print(f"Longest: {self.capital_run_length_longest:.2f}")
        print(f"Total: {self.capital_run_length_total:.2f}")

        
        features = [
            *self.word_freq.values(),
            *self.char_freq.values(),
            self.capital_run_length_average,
            self.capital_run_length_longest,
            self.capital_run_length_total
        ]
        
        return features

# Example usage
if __name__ == "__main__":
    # Read email text from a file
    # with open('email.txt', 'r') as file:
    #     email_text = file.read()

    extractor = EmailFeatureExtractor(email_text="The address for our upcoming meeting to discuss the email project will be sent directly to your business mail, and you can receive the data report by 3 p.m. on the 415 technology conference table.")
    feature_array = extractor.extract_features()
    
    print("Feature array for prediction:", feature_array)
