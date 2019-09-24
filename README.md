# nepali-roman
## Package to convert Nepali text to romanized English.

Many a time, while working with data, either from government sector or from private sector, we encounter Nepali names of
VDCs, municipalities, local level units, districts and places. While merging such data with another datasheet consisting
names of units in English, we need to romanize the Nepali names to English before using some text similarity algorithms 
to do string matching.

This package helps in romanizing Nepali names using rudimentary script. It is worth mentioning that romanization of 
Nepali text used in our daily life is inconsistent. For example, the popular romanization of "नेपाल" is "Nepal". It might
seem as the correct romanization but if we have to distinguish between "नेपाल" and "नेपल", we can't do that with this
romanization scheme. So, this package uses unique and standard romanization scheme such that no two Nepali words have
same romanization.

## Installation
`nepali-roman` package is available for `Python 3` and can be installed using `pip`. 

First make sure [`pip`](https://pip.pypa.io/en/stable/installing/) is installed.

Then, the package can be installed using this command.
```
pip install nepali-roman
```

## Usage

Import the `nepali_roman` module using the following command.
```python
import nepali_roman as nr
```
The `nepali_roman` module has two functions: `romanize_text` and `romanize`.

### `romanize_text`
This function can be used to romanize the Nepali text to English.

Syntax:
```python
>>> nr.romanize_text(nepali_text)
```
Example:
```python
>>> import nepali_roman as nr
>>> nr.romanize_text("नगरपालिका")
    nagarapaalikaa
```

### `romanize`
This function takes Nepali text file as an input and saves the romanized text in specified output file.

Syntax:
```python
>>> nr.romanize(input_file_path, output_file_path)
```

Example:
```python
>>> import nepali_roman as nr
>>> nr.romanize('nepali.txt', 'romanized_english.txt')
# this takes Nepali text file nepali.txt and stores romanized English in the file romanized_english.txt
```

## Contributions

The package is licenced with The MIT License (MIT) about which details can be found in the [LICENSE](LICENSE) file. As
the package is open sourced and requires many improvements and extensions, any contributions are welcome. Any other
feedback of any sort are highly welcome.