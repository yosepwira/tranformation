
## OVERVIEW
This Python script processes financial transaction data from a JSON file, transforming and formatting it into a structured format with masking, encryption, and additional metadata.

## FILE STRUCTURE

1. transformation_1_input_text_json.py  # Main transformation script
2. source_1.json                        # Sample input data file
3. transformation_1.log                 # Log file for transformation process
4. requirements.txt                     # Dependencies
5. README.md                            # Documentation file

## REQUIREMENTS
pip install -r requirements.txt

## RUN THE SCRIPT
python3 transformation_input_file_json.py source_1.json

- the script will automaticly read the data inside the source_1.json

## LOG
to check log
tail -f transformation.log

