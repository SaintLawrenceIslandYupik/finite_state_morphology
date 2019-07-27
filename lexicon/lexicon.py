#!/usr/bin/env python3.7

import re
from typing import Iterable, Optional, Dict

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
                 index: int,
                 category: str,
                 surface: str,
                 underlying: str,
                 continuation: str):
        self.index: int = index
        self.category: str = category
        self.surface: str = surface
        self.underlying: str = underlying
        self.continuation: str = continuation

        self.features: Dict[str, bool] = dict()

        self.demonstrative    = (self.category == "Demonstrative" or
                                 self.category == "DemInfl")
        self.emotional        = (self.category == "EmotionalRoot" or
                                 self.category == "EmotionalRootPostbase")
        self.interrogative    = (self.category == "Interrogative")
        self.particle         = (self.category == "Particle")
        self.noun             = (self.category == "NounBase" or
                                 self.category == "NounPostbase" or
                                 self.category == "NounInfl" or
                                 self.category == "Numeral" or
                                 self.category == "ProperNoun" or
                                 "[N]" in self.underlying or
                                 "[V→N]" in self.underlying or
                                 "[N→N]" in self.underlying or
                                 self.continuation == "NounPostbase" or
                                 self.continuation == "NounTag" or
                                 self.continuation == "NounInfl"
                                 )
        self.numeral          = (self.category == "Numeral")
        self.particle         = (self.category == "Particle")
        self.personal_pronoun = (self.category == "PersonalPronoun")
        self.postural         = (self.category == "PosturalRoot" or
                                 self.category == "PosRootPostbase")
        self.proper_noun      = (self.category == "ProperNoun")
        self.quant_qual       = (self.category == "QuantQual" or
                                 self.category == "QuantQualPostbase")
        self.verb             = (self.category == "VerbBase" or
                                 self.category == "VerbPostbase" or
                                 self.category == "VerbMoodInfl" or
                                 "Intransitive" in self.category or
                                 "Intransitive" in self.continuation or
                                 "Transitive" in self.category or
                                 "Transitive" in self.continuation or
                                 self.continuation == "VerbTag" or
                                 self.continuation == "VerbPostbase" or
                                 "[V]" in self.underlying or
                                 "[V→V]" in self.underlying or
                                 "[N→V]" in self.underlying)
        self.foreign_word     = (self.category == "ForeignWord")
        self.enclitic         = (self.category == "EncliticOrEnd")

        self.root_word = (self.category == "Demonstrative" or
                          self.category == "EmotionalRoot" or
                          self.category == "Interrogative" or
                          self.category == "Particle" or
                          self.category == "NounBase" or
                          self.category == "Numeral" or
                          self.category == "PersonalPronoun" or
                          self.category == "PosturalRoot" or
                          self.category == "ProperNoun" or
                          self.category == "QuantQual" or
                          self.category == "VerbBase" or
                          self.category == "ForeignWord")

        self.postbase = (self.category == "NounPostbase" or
                         self.category == "VerbPostbase" or
                         self.category == "PosRootPostbase" or
                         self.category == "EmotionalRootPostbase" or
                         self.category == "DemInfl")

        self.inflection = (not self.root_word) and (not self.postbase) and (not self.enclitic)

        self.v2v = "[V→V]" in self.underlying
        self.v2n = "[V→N]" in self.underlying
        self.n2v = "[N→V]" in self.underlying
        self.n2n = "[N→N]" in self.underlying

        self.transitive   = "[Trns]" in self.underlying or "Intransitive" in self.category
        self.intransitive = "[Intr]" in self.underlying or "Transitive" in self.category

        self.indicative    = "[Ind]" in self.underlying
        self.participial   = "[Ptcp]" in self.underlying
        self.interrogative = "[Intrg]" in self.underlying
        self.optative      = "[Optative]" in self.underlying
        self.participial_oblique = "[Ptcp_Obl]" in self.underlying

        self.present = "[PRS]" in self.underlying
        self.future  = "[FUT]" in self.underlying
        self.negative = "[NEG]" in self.underlying

        self.precessive = "[Prec]" in self.underlying
        self.consequential_i = "[CnsqI]" in self.underlying
        self.consequential_ii = "[CnsqII]" in self.underlying
        self.concessive = "[Conc]" in self.underlying
        self.contemporative = "[Ctmp]" in self.underlying
        self.conditional = "[Cond]" in self.underlying
        self.subordinative = "[Sbrd]" in self.underlying

        self.possesor_none = "[Unpd]" in self.underlying
        self.possesor_1sg  = "[1SgPoss]" in self.underlying
        self.possesor_1du  = "[1DuPoss]" in self.underlying
        self.possesor_1pl  = "[1PlPoss]" in self.underlying
        self.possesor_2sg  = "[2SgPoss]" in self.underlying
        self.possesor_2du  = "[2DuPoss]" in self.underlying
        self.possesor_2pl  = "[2PlPoss]" in self.underlying
        self.possesor_3sg  = "[3SgPoss]" in self.underlying
        self.possesor_3du  = "[3DuPoss]" in self.underlying
        self.possesor_3pl  = "[3PlPoss]" in self.underlying
        self.possesor_4sg  = "[4SgPoss]" in self.underlying
        self.possesor_4du  = "[4DuPoss]" in self.underlying
        self.possesor_4pl  = "[4PlPoss]" in self.underlying

        self.possessed     = ("[SgPosd]" in self.underlying or
                              "[DuPosd]" in self.underlying or
                              "[PlPosd]" in self.underlying)

        self.singular = ("[Sg]" in self.underlying or
                         "[SgPosd]" in self.underlying)

        self.dual = ("[Du]" in self.underlying or
                         "[DuPosd]" in self.underlying)

        self.plural = ("[Pl]" in self.underlying or
                         "[PlPosd]" in self.underlying)

        self.absolutive = "[Abs]" in self.underlying
        self.ablative_modalis = "[Abl_Mod]" in self.underlying
        self.locative = "[Loc]" in self.underlying
        self.terminalis = "[Ter]" in self.underlying
        self.vialis = "[Via]" in self.underlying
        self.equalis = "[Equ]" in self.underlying
        self.relative = "[Rel]" in self.underlying

        self.intransitive_1sg = self.underlying.startswith("[1Sg]") and self.intransitive
        self.intransitive_1du = self.underlying.startswith("[1Du]") and self.intransitive
        self.intransitive_1pl = self.underlying.startswith("[1Pl]") and self.intransitive
        self.intransitive_2sg = self.underlying.startswith("[2Sg]") and self.intransitive
        self.intransitive_2du = self.underlying.startswith("[2Du]") and self.intransitive
        self.intransitive_2pl = self.underlying.startswith("[2Pl]") and self.intransitive
        self.intransitive_3sg = self.underlying.startswith("[3Sg]") and self.intransitive
        self.intransitive_3du = self.underlying.startswith("[3Du]") and self.intransitive
        self.intransitive_3pl = self.underlying.startswith("[3Pl]") and self.intransitive
        self.intransitive_4sg = self.underlying.startswith("[4Sg]") and self.intransitive
        self.intransitive_4du = self.underlying.startswith("[4Du]") and self.intransitive
        self.intransitive_4pl = self.underlying.startswith("[4Pl]") and self.intransitive

        self.transitive_1sg_subject = self.underlying.startswith("[1Sg]") and self.transitive
        self.transitive_1du_subject = self.underlying.startswith("[1Du]") and self.transitive
        self.transitive_1pl_subject = self.underlying.startswith("[1Pl]") and self.transitive
        self.transitive_2sg_subject = self.underlying.startswith("[2Sg]") and self.transitive
        self.transitive_2du_subject = self.underlying.startswith("[2Du]") and self.transitive
        self.transitive_2pl_subject = self.underlying.startswith("[2Pl]") and self.transitive
        self.transitive_3sg_subject = self.underlying.startswith("[3Sg]") and self.transitive
        self.transitive_3du_subject = self.underlying.startswith("[3Du]") and self.transitive
        self.transitive_3pl_subject = self.underlying.startswith("[3Pl]") and self.transitive
        self.transitive_4sg_subject = self.underlying.startswith("[4Sg]") and self.transitive
        self.transitive_4du_subject = self.underlying.startswith("[4Du]") and self.transitive
        self.transitive_4pl_subject = self.underlying.startswith("[4Pl]") and self.transitive

        self.transitive_1sg_object = "[1Sg]:" in self.underlying and self.transitive
        self.transitive_1du_object = "[1Du]:" in self.underlying and self.transitive
        self.transitive_1pl_object = "[1Pl]:" in self.underlying and self.transitive
        self.transitive_2sg_object = "[2Sg]:" in self.underlying and self.transitive
        self.transitive_2du_object = "[2Du]:" in self.underlying and self.transitive
        self.transitive_2pl_object = "[2Pl]:" in self.underlying and self.transitive
        self.transitive_3sg_object = "[3Sg]:" in self.underlying and self.transitive
        self.transitive_3du_object = "[3Du]:" in self.underlying and self.transitive
        self.transitive_3pl_object = "[3Pl]:" in self.underlying and self.transitive
        self.transitive_4sg_object = "[4Sg]:" in self.underlying and self.transitive
        self.transitive_4du_object = "[4Du]:" in self.underlying and self.transitive
        self.transitive_4pl_object = "[4Pl]:" in self.underlying and self.transitive

        # Morphophonology
        self.semi_final_e = ("~sf" in self.surface or
                             "~h" in self.surface or
                             ("~" in self.surface and "~f" not in self.surface))

        self.final_e      = ("~f" in self.surface or
                             "~h" in self.surface or
                             ("~" in self.surface and "~sf" not in self.surface))

        self.require_hop  = ("~h" in self.surface)

        self.inter_consonantal_e = ("(e)" in self.surface)

        self.weak_final_c = ("-w" in self.surface)

        self.final_vc_drop = ("––" in self.surface)

        self.final_consonant_drop_assimilation = ("–" in self.surface)

        self.modify_te = ("@*" in self.surface or
                          "@₁" in self.surface or
                          "@₂" in self.surface)

        self.uvular_dropping = ("%:" in self.surface)



    def entry(self) -> str:
        underlying = self.underlying
        for symbol in Morpheme.JACOBSON_SYMBOLS:
            underlying = underlying.replace(symbol, "")
        return f"{underlying}:{self.surface}"

    def __str__(self):
        return f"{self.entry()}\t{self.continuation};"


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
    entry_parts = re.compile('^((?:.*?)[^%]):(.*)')
    with open(f"../ess.lexc") as lexc:
        for line in lexc:
            if '!' in line:
                line = line[:line.find('!')]
                line = line.strip()
            if len(line) > 0:
                all_lines += line.replace(';',';\n')

        section=None
        lexicon=dict()
        index = 0
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
                elif section=="NounTag" or section=="VerbTag" or section=="ForeignTag":
                    pass
                elif ';' in line:
                    match = entry.search(line)
                    if match:
                    #    print(match[1] + "___\t___" + match[2])
                        lexical_entry = match[1]
                        continuation = match[2]
                        match_lexical_entry = entry_parts.match(lexical_entry)
                        if match_lexical_entry:
                            underlying = match_lexical_entry[1]
                            surface = match_lexical_entry[2]
                        else:
                            underlying = lexical_entry
                            surface    = lexical_entry
                        index += 1
                        morpheme = Morpheme(index=index,
                                            category=section,
                                            surface=surface,
                                            underlying=underlying,
                                            continuation=continuation)
                        lexicon[section].append(morpheme)
                    else:
                        pass
                    #   print(f"No match for {line}")
                #print(line)
                #word = "'" + line[:line.rfind(' ')].strip() + "'"
                #print(word)
                #parts = line.split('; ')
                #for part in parts:
                #    print(f"'{part}'")

        for section in lexicon.keys():
            for morpheme in lexicon[section]:
                #if ":" in str(morpheme):
                if morpheme.inflection:
                    print(f"{morpheme.index}\t{str(morpheme)}")
            #print(f"{len(lexicon[section])}\t{section}")