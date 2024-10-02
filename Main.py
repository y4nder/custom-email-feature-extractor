import argparse

from EmailContentExtractor import extract_email_contents
from EmailFeatureExtractor import EmailFeatureExtractor

def main(eml_file: str):
    email_contents = extract_email_contents(eml_file_path=eml_file)
    body = str(email_contents["body"])
    print(body)
    
    print("-" * 100)
    print("\nextracting features\n")
    
    extractor = EmailFeatureExtractor(body)
    feature_array = extractor.extract_features()
    
    print(feature_array)
    
    
if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Process an email .eml file for spam detection.')
    parser.add_argument('email_file', type=str, help='The name of the .eml file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Run the main function with the provided email file
    main("testEmails/" + args.email_file)