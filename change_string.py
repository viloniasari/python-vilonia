from dataclasses import replace
from datetime import datetime
from posixpath import split
from xml.etree.ElementTree import Comment

# capitalize each word
def caps_by_space (s):
    words = s.split (" ")
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return " ".join(words)
# Uppercase a word
def my_uppercase(word):
    if not word:
       return ''
    return word[0].upper() + word[1:]
# split by enter
def caps_by_enter(text):
    words = text.split("\n")
    for i in range (len(words)):
        words[i] = my_uppercase (words[i])
    return "\n".join(words)
# replace sentence
def replace_word(text, old,new):
    if not text:
        return ""
    return text.replace(old, new)

text_string = "BIODATA INTERVIEW\n\nNAMA: ARIEL ORTEGA\nSEKOLAH: BACHELOR OF DEGREE UNIVERSITY OF INDONESIA\nTANGGAL DAN JAM: <TIMESTAMP>\n\nPROGRAMMING LANGUAGE: PHYTON, C, JAVA, C++, C#, VISUAL BASIC, JAVASCRIPT, ASSEMBLY, SQL DATABASE(MYSQL, ORACLE, POSTGRES), PHP, OBJECTIVE C, GO, DELPHI/PASCAL OBJECT, MATLAB, FORTRAN, SWIFT, CLASSIC VISUAL BASIC, R, PERL, RUBY, FOXPRO, COBOL, LUA, DART, SCALA, KOTLIN, TYPESCRIPT, GROOVY.\n\nWAKTU MENGERJAKAN: <TIMESTAMP1> S/D <TIMESTAMP2>\nTERIMA KASIH "
x = datetime(2022, 9, 9, 15, 47, 00)
x1 = datetime(2022, 9, 9, 14, 47, 00)
date1 = x.strftime("%m/%d/%Y %H:%M:%S")
date2 = x1.strftime("%m/%d/%Y %H:%M:%S")

stamp1 = text_string.replace ("<TIMESTAMP>", date1)
stamp2 = stamp1.replace("<TIMESTAMP1>", date2)
stamp3 = stamp2.replace("<TIMESTAMP2>", date1)
rep1 = stamp3.replace("S/D", "-")
textlow = rep1.lower()
words = textlow.split(" ")

text1 = caps_by_space(textlow)
text2 = caps_by_enter(text1)

change1 = replace_word(text2, "Of", "of")
change2 = replace_word(change1, "Dan", "dan")
change3 = replace_word(change2, "Sql", "SQL")
change4 = replace_word(change3, "mysql", "MySQL")
change5 = replace_word(change4, "Php", "PHP")
change6 = replace_word(change5, "pascal", "Pascal")
change7 = replace_word(change6, "Terima", "\nTerima")
change8 = replace_word(change7, ": A", "\t\t: A")
change9 = replace_word(change8, ": B", "\t\t: B")
change10 = replace_word(change9, "m:", "m\t:")
change11 = replace_word(change10, "Language:", "\t:")

print (change11)
