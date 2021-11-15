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
# ['O', 'O', 'U-PERSON', 'O', 'O', 'O']
```

## Note
Only Japanese is supported.  
Only BILOU supports the tag format. (BIO may support in the future)
