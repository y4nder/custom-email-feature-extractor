import argparse
from pathlib import Path

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
    
def newMain():
    directoryPath = Path('testEmailsTextForm')
    listOfFeatures = []
    for file_path in directoryPath.iterdir():
        if file_path.is_file():
            print(f"reading file: {file_path.name}")
            with file_path.open('r') as file:
                content = file.read()
                print(content)
                print("=" *50)
                extractor = EmailFeatureExtractor(content)
                listOfFeatures.append(extractor.extract_features())
                
    output_path = 'outputFeatures.txt'
    
    with open(output_path, 'w') as file:
        file.write(str(listOfFeatures))
    
    
def oldMain(): 
    parser = argparse.ArgumentParser(description='Process an email .eml file for spam detection.')
    parser.add_argument('email_file', type=str, help='The name of the .eml file')

    # Parse the command-line arguments
    args = parser.parse_args()
    if(args.email_file == 'all'):
        newMain()
    else:
        main("testEmails/" + args.email_file)
    
if __name__ == "__main__":
    oldMain()