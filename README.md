# Pi Number Lookup Tool

With this Python script you can view the occurrences of numbers in Pi, view the properties of numbers, and more. You may view the Gematria of text, whether it's English/Hebrew/Greek.

You can also lookup dates, and do simple date calculations.

![Constant lookup](https://user-images.githubusercontent.com/86980762/124512347-1ca7ca00-dda6-11eb-8bfd-6a069a11ec73.png)

# Install (Windows)

Make sure you have Python downloaded and installed. (Python 2)

Then with Pip you can run this command:

    pip install pynput convertdate clipboard backports.shutil_get_terminal_size

## Linux

    sudo apt install -y xclip libncurses5-dev python-pip && pip install --upgrade pip && pip install readline pynput convertdate clipboard backports.shutil_get_terminal_size

## Running it

You can then run this program by `python "C:\Users\User\Downloads\multi_tool_v9.py"` (Windows)

(Linux) `python '/home/user/Downloads/multi_tool_v9.py'`

# Date Lookup

You can view information about a date by entering a single date group (`7 26 2020`) or you can do calculations like so:

```
Input: 11 12 1997 -> 7 26 2020


Date:            11/12/1997 (Day 316)              |       Date:            7/26/2020 (Day 208)
Long count:      12.19.4.12.2                      |       Long count:      13.0.7.12.14
Tzolk'in day:    102 (11, Ik')                   [A|B]     Tzolk'in day:    74 (9, 'Ix')
Hebrew date:     8/12/5758 (Day 42 C, 219 E)       |       Hebrew date:     5/5/5780 (Day 301 C, 123 E)
Coptic date:     3/3/1714 (Day 63)                 |       Coptic date:     11/19/1736 (Day 319)


11/12/1997 -> 7/26/2020 = 8292 days
```

You can do addition or subtractions: `11 12 1997 + 8292` (or shorthand `a + 8292`) or `7 26 2020 - 8292`

# Multiple Constants

With this program you have the choice of looking up numbers in multiple constants, like Euler-Mascheroni's (em) or Phi (phi)

Pi (pi), Phi (phi), e (e), Euler-Mascheroni Constant (em), 2Pi (2pi), Glaisher-Kinkelin Constant (A), Catalan Constant (cat), Khinchin-Levy Constant (kl), Square root of 2 (rt)

# Hebrew Gematria

![Hebrew Gematria](https://user-images.githubusercontent.com/86980762/124513584-1c5cfe00-dda9-11eb-8778-d463d86d5776.png)

Enter Hebrew Text `ועל צבא מטה בני גד אליסף בן דעואל` to view its Gematria

# Greek Gematria (Isopsephy)

Input Greek Text `ἤ πῶς δύνασαι λέγειν τῷ ἀδελφῷ σου, Ἀδελφέ, ἄφες ἐκβάλω τὸ κάρφος τὸ ἐν τῷ ὀφθαλμῷ σου, αὐτὸς τὴν ἐν τῷ ὀφθαλμῷ σοῦ δοκὸν οὐ βλέπων; ὑποκριτά, ἔκβαλε πρῶτον τὴν δοκὸν ἐκ τοῦ ὀφθαλμοῦ σοῦ, καὶ τότε διαβλέψεις ἐκβαλεῖν τὸ κάρφος τὸ ἐν τῷ ὀφθαλμῷ τοῦ ἀδελφοῦ σου.`

![Greek_Isopsephy](https://user-images.githubusercontent.com/86980762/124514860-fe44cd00-ddab-11eb-9715-546cb2c7f8ad.png)

# Math

Do simple expressions in this calculator:

`0 + 68 + 483 + 6716`

The Result of this expression is `7267`

# Other

Read the directions carefully at startup to view the functions of this script.
