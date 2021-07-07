# Number Date and Gematria Python Tool

With this Tool you can view the properties of numbers, analyze dates, and view the Gematria of text whether it be English/Hebrew/Greek.

This tool can be used to view the occurrences of numbers in multiple Constants (Pi, Phi, Euler-Mascheroni's...)

![Pi Lookup Tool](https://user-images.githubusercontent.com/86980762/124818370-f36b7300-df38-11eb-9992-30b8b42ef049.png)

# Install (Windows)

First you will need Python downloaded and installed to run this script. ([Python 2](https://www.python.org/downloads/release/python-2717/))

Pip install the necessary components:

    pip install pynput convertdate clipboard backports.shutil_get_terminal_size

Then run from the Command Prompt:

    python "C:\Users\User\Downloads\multi_tool_v9.py"

## Linux

    sudo apt install -y xclip libncurses5-dev python-pip && pip install --upgrade pip && pip install readline pynput convertdate clipboard backports.shutil_get_terminal_size

Run it:

    python '/home/user/Downloads/multi_tool_v9.py'

# Date Lookup

View information about a date by entering a date group `7 26 2020`, or you can do date calculations like so:

```
Input: 11 12 1997 -> 7 26 2020


Date:            11/12/1997 (Day 316)              |       Date:            7/26/2020 (Day 208)
Long count:      12.19.4.12.2                      |       Long count:      13.0.7.12.14
Tzolk'in day:    102 (11, Ik')                   [A|B]     Tzolk'in day:    74 (9, 'Ix')
Hebrew date:     8/12/5758 (Day 42 C, 219 E)       |       Hebrew date:     5/5/5780 (Day 301 C, 123 E)
Coptic date:     3/3/1714 (Day 63)                 |       Coptic date:     11/19/1736 (Day 319)


11/12/1997 -> 7/26/2020 = 8292 days
```

The date on the left side becomes "a" in a variable, which can be referenced in additional calculations:

`a + 8292` `11 12 1997 + 8292` `7 26 2020 - 8292` `b + 5518`

The Right Hand result of a calculation becomes "b"

# Multiple Constants

You can chose which constant you would like to use by entering one of the following codes:

Pi (`pi`), Phi (`phi`), e (`e`), Euler-Mascheroni Constant (`em`), 2Pi (`2pi`), Glaisher-Kinkelin Constant (`A`), Catalan Constant (`cat`), Khinchin-Levy Constant (`kl`), Square Root of 2 (`rt`)

These constants can be viewed up to 1 million digits, except A which can be viewed up to 20000 digits.

# Hebrew Gematria

Enter Hebrew text: `ועל צבא מטה בני גד אליסף בן דעואל` to view its Gematria:

![Hebrew Gematria](https://user-images.githubusercontent.com/86980762/124827035-8ad5c380-df43-11eb-914d-02589297546a.png)

Text can be inputted and pasted from the Clipboard by pressing the Right Control key.

# Greek Isopsephy

`ἤ πῶς δύνασαι λέγειν τῷ ἀδελφῷ σου, Ἀδελφέ, ἄφες ἐκβάλω τὸ κάρφος τὸ ἐν τῷ ὀφθαλμῷ σου, αὐτὸς τὴν ἐν τῷ ὀφθαλμῷ σοῦ δοκὸν οὐ βλέπων; ὑποκριτά, ἔκβαλε πρῶτον τὴν δοκὸν ἐκ τοῦ ὀφθαλμοῦ σοῦ, καὶ τότε διαβλέψεις ἐκβαλεῖν τὸ κάρφος τὸ ἐν τῷ ὀφθαλμῷ τοῦ ἀδελφοῦ σου.`

![Greek Isopsephy](https://user-images.githubusercontent.com/86980762/124828545-6975d700-df45-11eb-8ede-7e74356cdc39.png)

# Math

Do simple expressions in this calculator:

`0 + 68 + 483 + 6716`

The Result is: `7267`

# Other

Read the directions carefully at startup to view the functions of this script.
