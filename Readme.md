# Store AWS credentials inside your Keychain

## Installing

The easiest way to install `awscreds` is to use pip3:

    $ pip3 install awscreds

or from sources:

    $ git clone https://github.com/DmitriyLyalyuev/awscreds.git
    $ cd awscreds
    $ python3 setup.py install

## Get help

`awscreds -h`

## Store credentials into Keychain

`awscreds add`

`awscreds add -e prj_name`

## Delete credentials from Keychain

`awscreds delete`

`awscreds delete -e prj_name`

## Get credentials from Keychain in ready to use format

`awscreds get -e prj_name`

## Export credentials into your shell session

```
eval `awscreds export -e prj_name`
```
