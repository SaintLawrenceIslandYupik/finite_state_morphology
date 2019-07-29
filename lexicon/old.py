#!/usr/bin/env python3.7

import re
from typing import Iterable, Optional, List

class Morpheme:

    JACOBSON_SYMBOLS = ['@₁~flu/na', '@₁~fy/~f(ng₁)', '@₁–lghii/@*ngugh*',
                        '~sf-w%:(e)tgun/teggun', '~f-w/-w',
                        #'@~–(g)ke', '@~–(g)ka', '(pete)fte',
                        '@~–(g)', '@~–(g)', '(pete)',
                        '(i/u)', '(q/t)', '(s/z)', '(t/y)', '(p/v)', '(g/t)',
                        '(at)', '(te)',
                        '(i₂)', '(i₁)', '(ng₂)', '(ng₁)',
                        '(s)', '(a)', '(u)',  '(t)', '(g)',
                        '(e)', '––', '-w', '~h', '~f', '~sf',
                        '@₂', '@₁', '@*', '%:', '~', '-', '–']

    def __init__(self,
                 category: str,
                 surface: str,
                 underlying: str,
                 definition: List[str],
                 continuation: str):
        self.category: str = category
        self.surface: str = surface
        self.underlying: str = underlying
        self.definition: List[str] = definition
        self.continuation: str = continuation

    def entry(self) -> str:
        underlying = self.underlying
        for symbol in Morpheme.JACOBSON_SYMBOLS:
            underlying = underlying.replace(symbol, "")
        return f"{underlying}[{self.category}]:{self.surface}"

    def get_definition(self) -> str:
        return f"  ! {' '.join(self.definition)}" if self.definition else ""

    def __str__(self):
        return f"{self.entry()}\t{self.continuation};{self.get_definition()}"


def process_line(category: str, line: str):
    start_of_comment = line.find("!")
    if start_of_comment >= 0:
        definition = line[start_of_comment+1:].strip()
        definition = [gloss.strip() for gloss in definition.split(";")] if ";" in definition else [definition]
    else:
        definition = list()

    semicolon = line.find(";")
    parts = line[:semicolon].split()

    continuation = parts[-1]

    entry = " ".join(parts[0:-1])
    if ":" in entry:
        split_point = re.search('[^%]:', entry).end()
        underlying = entry[0:split_point-1]
        surface = entry[split_point:]
    else:
        underlying = entry
        surface = entry

    return Morpheme(category, surface, underlying, definition, continuation)


def process(lexc: Iterable[str]):

    section: Optional[str] = None

    for line in lexc:  # type: str
        line = line.strip()
        if line.startswith("!"):
            pass
        elif line.startswith("LEXICON"):
            section = line.split("LEXICON ")[1]
        elif section and ";" in line:
            print()
            print(line)
            print(process_line(section, line))


if __name__ == "__main2__":

    sections = ["DemInfl",
                "Demonstrative",
                "EmotionalRoot",
                "EmotionalRootPostbase",
                "EncliticOrEnd",
                "Interrogative",
                "Multichar_Symbols",
                "NounBase",
                "NounInfl",
                "NounPostbase",
                "Numeral",
                "Particle",
                "PersonalPronoun",
                "PosRootPostbase",
                "PosturalRoot",
                "ProperNoun",
                "QuantQual",
                "QuantQualPostbase",
                "Root",
                "UnpdOblique",
                "VerbBase",
                "VerbEte",
                "VerbMoodInfl",
                "VerbPersonNumber",
                "VerbPostbase"]

    for section in sections:
        with open(f"sections/{section}.lexc") as lexc:
            process(lexc)

if __name__ == "__main__":
    #sections=dict()
    all_lines=""
    import re
    entry = re.compile('^((?:.*?)+)\\s+([A-Za-z\#]+)\\s*(;)')
    with open(f"../ess.lexc") as lexc:
        for line in lexc:
            if '!' in line:
                line = line[:line.find('!')]
                line = line.strip()
            if len(line) > 0:
                all_lines += line.replace(';',';\n')

        section=None
        lexicon=dict()
        for line in all_lines.split('\n'):
            line = line.strip()
            if len(line) > 0:
                #print("-"+line.strip()+"-")
                #continue
            #line = line.strip()
                if section==None or section=="Root":
                    pass
                if line.startswith("LEXICON"):
            #    print(line)
                    section=line.split()[1]
            #        print(section)
                    if section != "Root":
                        lexicon[section] = list()
                elif ';' in line:
                    match = entry.search(line)
                    if match:
                    #    print(match[1] + "___\t___" + match[2])
                        lexicon[section].append(match[1])
                    else:
                        pass
                    #   print(f"No match for {line}")
                #print(line)
                #word = "'" + line[:line.rfind(' ')].strip() + "'"
                #print(word)
                #parts = line.split('; ')
                #for part in parts:
                #    print(f"'{part}'")

        index = 0
        for section in lexicon.keys():
            for word in lexicon[section]:
                index += 1
                if ":" in word:
                    print(f"{index}\t{word}\t{section}")
            #print(f"{len(lexicon[section])}\t{section}")
