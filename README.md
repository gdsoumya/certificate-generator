# Certificate Generator
##
The Certificate Generator is a simple dynamic course/event certificate generator. It is easy to use and highly customizable.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites

Certificate Generator requires [ **Python (> Python 3.5)**](https://www.python.org/) .

##### Get the project.
#
```sh
$ git clone https://github.com/gdsoumya/certificate-generator.git
or 
Download and extract the Zip-File
```
#### Installing Dependencies
The Project has a few dependencies which can be installed by running.
```sh
$ cd certificate-generator
$ pip install -r dependencies.txt 
```

## Configuration

To configure the script edit the ['**config.txt**'](https://github.com/gdsoumya/certificate-generator/blob/master/config.txt) file. A properly configured file should look like :
```
[SETTINGS]
TEMPLATE = template/example-template.jpg

[NAME]
NAME_FONT = fonts/Cookie-Regular.ttf
NAME_FONT_SIZE = 35
NAME_COLOR = rgb(0,0,0)
NAME_X = 122
NAME_Y = 220
NAME_WIDTH = 404

[EVENT]
EVENT_FONT = fonts/Kanit-Regular.ttf
EVENT_FONT_SIZE =30
EVENT_COLOR = rgb(0,0,0)
EVENT_X = 122
EVENT_Y = 318
EVENT_WIDTH = 404

[DATE]
DATE_FONT = fonts/Kanit-Regular.ttf
DATE_FONT_SIZE = 21
DATE_COLOR = rgb(0,0,0)
DATE_X = 90
DATE_Y = 375
DATE_WIDTH = 126
```
### OPTIONS 
| OPTION | DESCRIPTION |
| ------ | ------ |
| TEMPLATE | **Path of the Template** (IMAGE) of the Certificate |
| *_FONT | **Path of Font File** (.ttf) that will be use for * field in the Certificate |
| *_FONT_SIZE | **Font Size** that will be use for * field in the Certificate  |
| *_COLOR | **Font Color** that will be use for * field in the Certificate |
|*_X | **X Co-ordinate** from where the * field begins in the Certificate |
|*_Y | **Y Co-ordinate** from where the * field begins in the Certificate |
|*_WIDTH | **Width** of the * field in the Certificate |

##### * can be replaced with NAME/DATE/EVENT

#
#
## Running Script
The project comes with two example test files [test.py](https://github.com/gdsoumya/certificate-generator/blob/master/test.py) and [test-cli.py](https://github.com/gdsoumya/certificate-generator/blob/master/test-cli.py).

[test.py](https://github.com/gdsoumya/certificate-generator/blob/master/test.py) : It is an example that demonstrates how **Certificate Generator** can be implemented in already existing projects.
```sh
$ python test.py

>>  CERTIFICATE GENERATED AND SAVED AS : outputcertificate.png  <<
STATUS : SUCCESSFUL
```
[test-cli.py](https://github.com/gdsoumya/certificate-generator/blob/master/test-cli.py) : It is a cli based example that lets you test the script directly from the command line.

```sh
$ python test-cli.py -n "John Doe" -e "GREEN EARTH INITIATIVE" -d "01/02/2019" -o exampleCert.png

** DATA TO BE USED **
>> NAME : John Doe
>> EVENT : GREEN EARTH INITIATIVE
>> DATE : 01/02/2019
>> OUTPUT FILE : exampleCert.png

!! Is the Information Correct [y/n] :y

>>  CERTIFICATE GENERATED AND SAVED AS : exampleCert.png  <<
```

## Packages Used

- **[PILLOW](https://pillow.readthedocs.io/en/stable/)** : For Image Processing
- **[Configparser](https://docs.python.org/3/library/configparser.html)** : For reading config file.

## Author
-   **Soumya Ghosh Dastidar**

## Contributting
Any contribution/suggestions are welcomed.
