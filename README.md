# noyaki
Converts character span label information to tokenized text-based label information.

## Installation
```sh
$ pip install noyaki
```

## Usage
Pass the tokenized text and label information as arguments to the convert function.
```py
import noyaki

label_list = noyaki.convert(
        ['明日', 'は', '田中', 'さん', 'に', '会う'],
        [[3, 5, 'PERSON']]
    )

print(label_list)
# ['O', 'O', 'U-PERSON', 'O', 'O', 'O'] 
```
  
If you want to remove the subword symbol (eg. ##), specify the `subword` argument.  
```py
import noyaki

label_list = noyaki.convert(
        ['明日', 'は', '田', '##中', 'さん', 'に', '会う'],
        [[3, 5, 'PERSON']],
	subword="##"
    )

print(label_list)
# ['O', 'O', 'B-PERSON', 'L-PERSON', 'O', 'O', 'O']
```
  
If you want to use IOB2 tag format, specify the `scheme` argument.  
```py
import noyaki

label_list = noyaki.convert(
        ['明日', 'は', '田', '##中', 'さん', 'に', '会う'],
        [[3, 5, 'PERSON']],
	scheme="IOB2"
    )

print(label_list)
# ['O', 'O', 'B-PERSON', 'I-PERSON', 'O', 'O', 'O']
```

## Note
Only Japanese is supported.  
supported tag formats are follow:
- BILOU
- IOB2
