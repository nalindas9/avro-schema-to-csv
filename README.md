# avro-schema-to-csv
[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/nalindas9/avro-schema-to-csv/blob/master/LICENSE)

## About
Avro schema to CSV converter. PyPi Package can be found [here](https://pypi.org/project/avroSchemaToCsvConvertor/). (Developed and published using setuptools, wheel, twine and tqdm)

## Output

https://user-images.githubusercontent.com/44141068/161920566-f87b0fb4-63ff-49e4-a1c8-1a5250c3c073.mp4

## System and library requirements
- avro-python3==1.9.1
- pycodestyle==2.8.0

## How to Run
1. Clone this repo. <br>
2. Navigate into the folder `avro-schema-to-csv` <br>
3. Create and activate [Virtual Environment](https://docs.python.org/3/library/venv.html) <br>
4. Upgrade pip using `python -m pip install --upgrade pip`.
5. Install requirements.txt using command `pip install -r requirements.txt`
6. To run the code, from the terminal, run the command `python3 main.py --file <path to your .avsc Avro Schema File>` <br>
7. The converted CSV file is stored in the `csv` folder.
