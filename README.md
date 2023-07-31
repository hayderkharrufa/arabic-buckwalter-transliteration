# Arabic-Buckwalter Transliteration

Arabic-Buckwalter Transliteration is a Python library that provides an easy way to convert Arabic text to Buckwalter transliteration, and vice versa. It supports all Arabic characters and diacritics, making it flexible for a wide range of transliteration tasks.

## Installation

You can install the package via pip:
```bash
pip install arabic_buckwalter_transliteration
```

## Usage

```python
from arabic_buckwalter_transliteration.transliteration import buckwalter_to_arabic, arabic_to_buckwalter

# Convert Buckwalter to Arabic
arabic_text = buckwalter_to_arabic('Aalos~alAmu Ealayokumo yaA Sadiyqiy')
print(arabic_text)  # outputs: اَلْسَّلامُ عَلَيْكُمْ يَا صَدِيقِي

# Convert Arabic to Buckwalter
buckwalter_text = arabic_to_buckwalter('اَلْسَّلامُ عَلَيْكُمْ يَا صَدِيقِي')
print(buckwalter_text)  # outputs: Aalos~alAmu Ealayokumo yaA Sadiyqiy
```

## Running Tests

You can run the tests by navigating to the project root directory and running the following command in your terminal:
```python
python -m unittest tests/test_transliteration.py
```

## Contributing
We appreciate all the help we can get. If you want to contribute to this project, please read our [CONTRIBUTING.md](https://github.com/hayderkharrufa/arabic-buckwalter-transliteration/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the terms of the MIT license. See the [LICENSE](https://github.com/hayderkharrufa/arabic-buckwalter-transliteration/blob/main/LICENSE) file for the full text.