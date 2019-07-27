#!/usr/bin/env python3.7

import re
from typing import Iterable, Optional, Dict, List, Tuple
import foma
from foma import FST

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
        self.duplicates = list()

        self.features: Dict[str, bool] = dict()

        self.features["demonstrative"] = (self.category == "Demonstrative" or
                                          self.category == "DemInfl")
        self.features["emotional"] = (self.category == "EmotionalRoot" or
                                      self.category == "EmotionalRootPostbase")
        self.features["interrogative"] = (self.category == "Interrogative")
        self.features["particle"] = (self.category == "Particle")
        self.features["noun"] = (self.category == "NounBase" or
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
        self.features["numeral"] = (self.category == "Numeral")
        self.features["particle"] = (self.category == "Particle")
        self.features["personal_pronoun"] = (self.category == "PersonalPronoun")
        self.features["postural"] = (self.category == "PosturalRoot" or
                                     self.category == "PosRootPostbase")
        self.features["proper_noun"] = (self.category == "ProperNoun")
        self.features["quant_qual"] = (self.category == "QuantQual" or
                                       self.category == "QuantQualPostbase")
        self.features["verb"] = (self.category == "VerbBase" or
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
        self.features["foreign_word"] = (self.category == "ForeignWord")
        self.features["enclitic"] = (self.category == "EncliticOrEnd")

        self.features["root_word"] = (self.category == "Demonstrative" or
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

        self.features["postbase"] = (self.category == "NounPostbase" or
                                     self.category == "VerbPostbase" or
                                     self.category == "PosRootPostbase" or
                                     self.category == "EmotionalRootPostbase" or
                                     self.category == "DemInfl")

        self.features["inflection"] = (not self.features["root_word"] and
                                       not self.features["postbase"] and
                                       not self.features["enclitic"])

        self.features["v2v"] = "[V→V]" in self.underlying
        self.features["v2n"] = "[V→N]" in self.underlying
        self.features["n2v"] = "[N→V]" in self.underlying
        self.features["n2n"] = "[N→N]" in self.underlying

        self.features["transitive"] = "[Trns]" in self.underlying or "Intransitive" in self.category
        self.features["intransitive"] = "[Intr]" in self.underlying or "Transitive" in self.category

        self.features["indicative"] = "[Ind]" in self.underlying
        self.features["participial"] = "[Ptcp]" in self.underlying
        self.features["interrogative"] = "[Intrg]" in self.underlying
        self.features["optative"] = "[Optative]" in self.underlying
        self.features["participial_oblique"] = "[Ptcp_Obl]" in self.underlying

        self.features["present"] = "[PRS]" in self.underlying
        self.features["future"] = "[FUT]" in self.underlying
        self.features["negative"] = "[NEG]" in self.underlying

        self.features["precessive"] = "[Prec]" in self.underlying
        self.features["consequential_i"] = "[CnsqI]" in self.underlying
        self.features["consequential_ii"] = "[CnsqII]" in self.underlying
        self.features["concessive"] = "[Conc]" in self.underlying
        self.features["contemporative"] = "[Ctmp]" in self.underlying
        self.features["conditional"] = "[Cond]" in self.underlying
        self.features["subordinative"] = "[Sbrd]" in self.underlying

        self.features["possesor_none"] = "[Unpd]" in self.underlying
        self.features["possesor_1sg"] = "[1SgPoss]" in self.underlying
        self.features["possesor_1du"] = "[1DuPoss]" in self.underlying
        self.features["possesor_1pl"] = "[1PlPoss]" in self.underlying
        self.features["possesor_2sg"] = "[2SgPoss]" in self.underlying
        self.features["possesor_2du"] = "[2DuPoss]" in self.underlying
        self.features["possesor_2pl"] = "[2PlPoss]" in self.underlying
        self.features["possesor_3sg"] = "[3SgPoss]" in self.underlying
        self.features["possesor_3du"] = "[3DuPoss]" in self.underlying
        self.features["possesor_3pl"] = "[3PlPoss]" in self.underlying
        self.features["possesor_4sg"] = "[4SgPoss]" in self.underlying
        self.features["possesor_4du"] = "[4DuPoss]" in self.underlying
        self.features["possesor_4pl"] = "[4PlPoss]" in self.underlying

        self.features["possessed"] = ("[SgPosd]" in self.underlying or
                                      "[DuPosd]" in self.underlying or
                                      "[PlPosd]" in self.underlying)

        self.features["singular"] = ("[Sg]" in self.underlying or
                                     "[SgPosd]" in self.underlying)

        self.features["dual"] = ("[Du]" in self.underlying or
                                 "[DuPosd]" in self.underlying)

        self.features["plural"] = ("[Pl]" in self.underlying or
                                   "[PlPosd]" in self.underlying)

        self.features["absolutive"] = "[Abs]" in self.underlying
        self.features["ablative_modalis"] = "[Abl_Mod]" in self.underlying
        self.features["locative"] = "[Loc]" in self.underlying
        self.features["terminalis"] = "[Ter]" in self.underlying
        self.features["vialis"] = "[Via]" in self.underlying
        self.features["equalis"] = "[Equ]" in self.underlying
        self.features["relative"] = "[Rel]" in self.underlying

        self.features["intransitive_1sg"] = self.underlying.startswith("[1Sg]") and self.features["intransitive"]
        self.features["intransitive_1du"] = self.underlying.startswith("[1Du]") and self.features["intransitive"]
        self.features["intransitive_1pl"] = self.underlying.startswith("[1Pl]") and self.features["intransitive"]
        self.features["intransitive_2sg"] = self.underlying.startswith("[2Sg]") and self.features["intransitive"]
        self.features["intransitive_2du"] = self.underlying.startswith("[2Du]") and self.features["intransitive"]
        self.features["intransitive_2pl"] = self.underlying.startswith("[2Pl]") and self.features["intransitive"]
        self.features["intransitive_3sg"] = self.underlying.startswith("[3Sg]") and self.features["intransitive"]
        self.features["intransitive_3du"] = self.underlying.startswith("[3Du]") and self.features["intransitive"]
        self.features["intransitive_3pl"] = self.underlying.startswith("[3Pl]") and self.features["intransitive"]
        self.features["intransitive_4sg"] = self.underlying.startswith("[4Sg]") and self.features["intransitive"]
        self.features["intransitive_4du"] = self.underlying.startswith("[4Du]") and self.features["intransitive"]
        self.features["intransitive_4pl"] = self.underlying.startswith("[4Pl]") and self.features["intransitive"]

        self.features["transitive_1sg_subject"] = self.underlying.startswith("[1Sg]") and self.features["transitive"]
        self.features["transitive_1du_subject"] = self.underlying.startswith("[1Du]") and self.features["transitive"]
        self.features["transitive_1pl_subject"] = self.underlying.startswith("[1Pl]") and self.features["transitive"]
        self.features["transitive_2sg_subject"] = self.underlying.startswith("[2Sg]") and self.features["transitive"]
        self.features["transitive_2du_subject"] = self.underlying.startswith("[2Du]") and self.features["transitive"]
        self.features["transitive_2pl_subject"] = self.underlying.startswith("[2Pl]") and self.features["transitive"]
        self.features["transitive_3sg_subject"] = self.underlying.startswith("[3Sg]") and self.features["transitive"]
        self.features["transitive_3du_subject"] = self.underlying.startswith("[3Du]") and self.features["transitive"]
        self.features["transitive_3pl_subject"] = self.underlying.startswith("[3Pl]") and self.features["transitive"]
        self.features["transitive_4sg_subject"] = self.underlying.startswith("[4Sg]") and self.features["transitive"]
        self.features["transitive_4du_subject"] = self.underlying.startswith("[4Du]") and self.features["transitive"]
        self.features["transitive_4pl_subject"] = self.underlying.startswith("[4Pl]") and self.features["transitive"]

        self.features["transitive_1sg_object"] = "[1Sg]:" in self.underlying and self.features["transitive"]
        self.features["transitive_1du_object"] = "[1Du]:" in self.underlying and self.features["transitive"]
        self.features["transitive_1pl_object"] = "[1Pl]:" in self.underlying and self.features["transitive"]
        self.features["transitive_2sg_object"] = "[2Sg]:" in self.underlying and self.features["transitive"]
        self.features["transitive_2du_object"] = "[2Du]:" in self.underlying and self.features["transitive"]
        self.features["transitive_2pl_object"] = "[2Pl]:" in self.underlying and self.features["transitive"]
        self.features["transitive_3sg_object"] = "[3Sg]:" in self.underlying and self.features["transitive"]
        self.features["transitive_3du_object"] = "[3Du]:" in self.underlying and self.features["transitive"]
        self.features["transitive_3pl_object"] = "[3Pl]:" in self.underlying and self.features["transitive"]
        self.features["transitive_4sg_object"] = "[4Sg]:" in self.underlying and self.features["transitive"]
        self.features["transitive_4du_object"] = "[4Du]:" in self.underlying and self.features["transitive"]
        self.features["transitive_4pl_object"] = "[4Pl]:" in self.underlying and self.features["transitive"]

        # Morphophonology
        self.features["semi_final_e"] = ("~sf" in self.surface or
                                         "~h" in self.surface or
                                         ("~" in self.surface and "~f" not in self.surface))

        self.features["final_e"] = ("~f" in self.surface or
                                    "~h" in self.surface or
                                    ("~" in self.surface and "~sf" not in self.surface))

        self.features["require_hop"] = ("~h" in self.surface)

        self.features["inter_consonantal_e"] = ("(e)" in self.surface)

        self.features["weak_final_c"] = ("-w" in self.surface)

        self.features["final_vc_drop"] = ("––" in self.surface)

        self.features["final_consonant_drop_assimilation"] = ("–" in self.surface)

        self.features["modify_te"] = ("@*" in self.surface or
                                      "@₁" in self.surface or
                                      "@₂" in self.surface)

        self.features["uvular_dropping"] = ("%:" in self.surface)

        self.feature_list = (
            "demonstrative",
            "emotional",
            "interrogative",
            "particle",
            "noun",
            "numeral",
            "particle",
            "personal_pronoun",
            "postural",
            "proper_noun",
            "quant_qual",
            "verb",
            "foreign_word",
            "enclitic",
            "root_word",
            "postbase",
            "inflection",
            "v2v",
            "v2n",
            "n2v",
            "n2n",
            "transitive",
            "intransitive",
            "indicative",
            "participial",
            "interrogative",
            "optative",
            "participial_oblique",
            "present",
            "future",
            "negative",
            "precessive",
            "consequential_i",
            "consequential_ii",
            "concessive",
            "contemporative",
            "conditional",
            "subordinative",
            "possesor_none",
            "possesor_1sg",
            "possesor_1du",
            "possesor_1pl",
            "possesor_2sg",
            "possesor_2du",
            "possesor_2pl",
            "possesor_3sg",
            "possesor_3du",
            "possesor_3pl",
            "possesor_4sg",
            "possesor_4du",
            "possesor_4pl",
            "possessed",
            "singular",
            "dual",
            "plural",
            "absolutive",
            "ablative_modalis",
            "locative",
            "terminalis",
            "vialis",
            "equalis",
            "relative",
            "intransitive_1sg",
            "intransitive_1du",
            "intransitive_1pl",
            "intransitive_2sg",
            "intransitive_2du",
            "intransitive_2pl",
            "intransitive_3sg",
            "intransitive_3du",
            "intransitive_3pl",
            "intransitive_4sg",
            "intransitive_4du",
            "intransitive_4pl",
            "transitive_1sg_subject",
            "transitive_1du_subject",
            "transitive_1pl_subject",
            "transitive_2sg_subject",
            "transitive_2du_subject",
            "transitive_2pl_subject",
            "transitive_3sg_subject",
            "transitive_3du_subject",
            "transitive_3pl_subject",
            "transitive_4sg_subject",
            "transitive_4du_subject",
            "transitive_4pl_subject",
            "transitive_1sg_object",
            "transitive_1du_object",
            "transitive_1pl_object",
            "transitive_2sg_object",
            "transitive_2du_object",
            "transitive_2pl_object",
            "transitive_3sg_object",
            "transitive_3du_object",
            "transitive_3pl_object",
            "transitive_4sg_object",
            "transitive_4du_object",
            "transitive_4pl_object",
            "semi_final_e",
            "final_e",
            "require_hop",
            "inter_consonantal_e",
            "weak_final_c",
            "final_vc_drop",
            "final_consonant_drop_assimilation",
            "modify_te",
            "uvular_dropping",
        )

        self.index_of_feature: Dict[str, int] = {feature: i for i, feature in enumerate(self.feature_list)}

    def entry(self) -> str:
        underlying = self.underlying
        surface = self.surface
        for symbol in Morpheme.JACOBSON_SYMBOLS:
            underlying = underlying.replace(symbol, "")
            surface    = surface.replace(symbol, "")
        return f"{underlying}:{surface}"

    def feature_vector(self):
        return [int(self.features[feature]) for feature in self.feature_list]

    def __str__(self):
        return f"{self.entry()}\t{self.continuation};"

    def __repr__(self):
        return str(self)

    def __getitem__(self, item) -> bool:
        if isinstance(item, int):
            if 0 < item < len(self.feature_list):
                feature = self.feature_list[item]
                return self.features[feature]
            else:
                raise IndexError
        elif isinstance(item, str):
            return self.features[item]
        else:
            raise TypeError


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
    with open(f"../ess.lexc") as lexc, open(f"../all.train.ess") as corpus, open(f"../all.train.analyzed.ess", "wt") as analyzed_file:
        for line in lexc:
            if '!' in line:
                line = line[:line.find('!')]
                line = line.strip()
            if len(line) > 0:
                all_lines += line.replace(';',';\n')

        underlying2morpheme = dict()
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

                        morpheme = Morpheme(index=index+1,
                                            category=section,
                                            surface=surface,
                                            underlying=underlying,
                                            continuation=continuation)
                        key = morpheme.entry()
                        if key in underlying2morpheme:
                            duplicate: Tuple[str,str] = (section, continuation)
                            morpheme.duplicates.append(duplicate)
                        else:
                            index += 1
                            lexicon[section].append(morpheme)
                            underlying2morpheme[key] = morpheme
                    else:
                        pass


        result = dict()
        for key, morpheme in underlying2morpheme.items():
            index = morpheme.index
            features = morpheme.feature_vector()
            result[key] = (index, features)

#        with open("morphemes.ess.pickle", "wb") as output:
#            import pickle
#            pickle.dump(result, output)

        def heuristic(analysis):
            result = 0
            parts = analysis.split(":")
            segments_in_lhs = parts[0].count("^") + 1
            segments_in_rhs = parts[1].count("^") + 1
            result += (segments_in_lhs - segments_in_rhs) * 1000

            lhs_elements = set(parts[0].split("^"))
            duplicates = segments_in_lhs - len(lhs_elements)
            result += duplicates * 10000

            result += len(parts[0])

            result += segments_in_rhs

            return result

        analyzed: Dict[str, str] = dict()

        s2u = FST.load("../ess.fomabin")
        s2i = FST.load("../ess.lex.fomabin")
        i2u = FST.load("../ess.underlying.fomabin")

        for line in corpus:
            tokens = line.strip().split()
            for token in tokens:
                #analyzed_tokens = list()
                if token not in analyzed:
                    underlying_analyses = list(s2u.apply_up(token))
                    if not underlying_analyses:
                        underlying_analyses = list(s2u.apply_up(token.lower()))
                    intermediate_analyses = [list(i2u.apply_down(underlying_analysis))[0] for underlying_analysis in underlying_analyses]
                    #print("\t".join(underlying_analyses))
                    options = sorted([underlying_analyses[i]+":"+intermediate_analyses[i] for i in range(len(underlying_analyses))], key=heuristic)
                    if len(options) > 0:
                        #analyzed_tokens.append(options[0])
                        analyzed[token] = options[0] + ":" + token
                    else:
                        analyzed[token] = "*" + token
                        #analyzed_tokens.append("*" + token)
                    #z="\t".join(options)
                    #print(token + "\t" + z)
                    #for option in options:
                    #    print(f"{heuristic(option)}\t{option}")
            print(" ".join([analyzed[token] for token in tokens]), file=analyzed_file)
   #     out = open("morphemes.out", "wt")
   #     for section in lexicon.keys():
   #         for morpheme in lexicon[section]:
   #             #if ":" in str(morpheme):
   #             #if morpheme["inflection"]:
   #             print(f"{str(morpheme.feature_vector()).replace(' ','')}\t{morpheme.index}\t{str(morpheme)}", file=out)
   #         #print(f"{len(lexicon[section])}\t{section}")