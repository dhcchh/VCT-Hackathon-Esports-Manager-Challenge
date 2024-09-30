import gzip
from bs4 import BeautifulSoup

# Function to extract and prettify XML from gzipped files
def extract_and_prettify_gz_file(file_path, output_file_path):
    try:
        # Step 1: Extract the gzip file
        with gzip.open(file_path, 'rb') as f:
            xml_content = f.read()

        # Step 2: Parse the XML content using BeautifulSoup
        soup = BeautifulSoup(xml_content, 'xml')

        # Step 3: Pretty print the XML content
        pretty_xml = soup.prettify()

        # Step 4: Save to output file with UTF-8 encoding
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(pretty_xml)

        print(f"Formatted XML saved to {output_file_path}")

    except UnicodeEncodeError as e:
        print(f"Encoding error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# File paths (replace with actual paths to your files)
gz_file_1 = './Data/fandomData/valorant_esports_pages.xml.gz'
gz_file_2 = './Data/fandomData/valorant_pages.xml.gz'

# Output paths for formatted XML files
output_file_1 = './Data/fandomData/valorant_esports_pages_formatted.xml'
output_file_2 = './Data/fandomData/valorant_pages_formatted.xml'

# Run the extraction and prettifying function for both files
extract_and_prettify_gz_file(gz_file_1, output_file_1)
extract_and_prettify_gz_file(gz_file_2, output_file_2)
