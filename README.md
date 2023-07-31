# Arabic-Buckwalter Transliteration

This project provides Python functions to convert Arabic text to Buckwalter transliteration and vice versa. 

## Installation

1. Clone this repository: `git clone https://github.com/hayderkharrufa/arabic-buckwalter-transliteration.git`.
2. Install the required packages (if any): `pip install -r requirements.txt`.

## Usage

The module `transliteration.py` provides the following functions:

- `buckwalter_to_arabic(text: str) -> str`: Convert Buckwalter transliterated text to Arabic.
- `arabic_to_buckwalter(text: str) -> str`: Convert Arabic text to Buckwalter transliteration.

Here's an example of how to use these functions:

```python
from arabic_buckwalter_transliteration.transliteration import buckwalter_to_arabic, arabic_to_buckwalter

arabic_text = 'اَلْسَّلامُ عَلَيْكُمْ يَا صَدِيقِي'
bw_text = arabic_to_buckwalter(arabic_text)
print(bw_text)

arabic_text_converted_back = buckwalter_to_arabic(bw_text)
print(arabic_text_converted_back)