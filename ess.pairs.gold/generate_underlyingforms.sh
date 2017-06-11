#!/bin/bash

# To block comment  :1,10s/^/#/
# To uncomment      :1,10s/^#//

#######################
#      CHAPTER 2      #
#######################

# Absolutive
#awk '{print $0 "[N][Abs][Du]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][Pl]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][Sg]"}' underlying.tsv &> underlying3.tsv

#######################
#      CHAPTER 3      #
#######################

# Ablative-Modalis 
#awk '{print $0 "[N][Abl_Mod][Unpd][Sg]"}' underlying.tsv | sort &> inputToSurface.tsv

# Intransitive Indicative 
#awk '{print $0 "[V][Intr_Ind][1Du]"}' underlying.tsv &> underlying1.tsv 
#awk '{print $0 "[V][Intr_Ind][1Pl]"}' underlying.tsv &> underlying2.tsv 
#awk '{print $0 "[V][Intr_Ind][1Sg]"}' underlying.tsv &> underlying3.tsv 
#awk '{print $0 "[V][Intr_Ind][2Du]"}' underlying.tsv &> underlying4.tsv 
#awk '{print $0 "[V][Intr_Ind][2Pl]"}' underlying.tsv &> underlying5.tsv 
#awk '{print $0 "[V][Intr_Ind][2Sg]"}' underlying.tsv &> underlying6.tsv 
#awk '{print $0 "[V][Intr_Ind][3Du]"}' underlying.tsv &> underlying7.tsv 
#awk '{print $0 "[V][Intr_Ind][3Pl]"}' underlying.tsv &> underlying8.tsv 
#awk '{print $0 "[V][Intr_Ind][3Sg]"}' underlying.tsv &> underlying9.tsv 
 
#######################
#      CHAPTER 4      #
#######################

# 1st/2nd Person Possessed Possessor Absolutive
#awk '{print $0 "[N][Abs][1SgPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][1SgPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][1SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][2SgPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][2SgPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][2SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][1PlPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][1PlPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][1PlPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][2PlPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][2PlPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][2PlPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][1DuPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][1DuPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][1DuPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][2DuPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][2DuPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][2DuPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv

# Chapter 4 Postbases
#awk '{print $0 "[N→N]"}' underlying.tsv &> underlying1.tsv

#######################
#      CHAPTER 5      #
#######################

# Localis / Terminalis / Vialis / Equalis Cases 
#awk '{print $0 "[N][Loc][Unpd][Sg]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Loc][Unpd][Pl]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Ter][Unpd][Sg]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Ter][Unpd][Pl]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Via][Unpd][Sg]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Via][Unpd][Pl]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Equ][Unpd][Sg]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Equ][Unpd][Pl]"}' underlying.tsv &> underlying2.tsv

#######################
#      CHAPTER 6      #
#######################

# 3rd Person Possessor Possessed Absolutive 
#awk '{print $0 "[N][Abs][3SgPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][3SgPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][3SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][3PlPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][3PlPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][3PlPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][3DuPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][3DuPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][3DuPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv

#awk '{print $0 "[N][Rel][Unpd][Sg]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Rel][Unpd][Pl]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Rel][Unpd][Du]"}' underlying.tsv &> underlying3.tsv

#######################
#      CHAPTER 7      #
#######################

# Possessed Relative Case
#awk '{print $0 "[N][Rel][Posd][1Sg]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Rel][Posd][1Pl]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Rel][Posd][2Sg]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Rel][Posd][2Pl]"}' underlying.tsv &> underlying4.tsv
#awk '{print $0 "[N][Rel][Posd][3Sg]"}' underlying.tsv &> underlying5.tsv
#awk '{print $0 "[N][Rel][Posd][3Pl]"}' underlying.tsv &> underlying6.tsv

# Transitive Indicative
#awk '{print $0 "[V][Trns_Ind][1Sg][2Sg]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[V][Trns_Ind][1Sg][3Sg]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[V][Trns_Ind][1Sg][3Pl]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[V][Trns_Ind][2Sg][1Sg]"}' underlying.tsv &> underlying4.tsv
#awk '{print $0 "[V][Trns_Ind][2Sg][3Sg]"}' underlying.tsv &> underlying5.tsv
#awk '{print $0 "[V][Trns_Ind][2Sg][3Pl]"}' underlying.tsv &> underlying6.tsv
#awk '{print $0 "[V][Trns_Ind][3Sg][1Sg]"}' underlying.tsv &> underlying7.tsv
#awk '{print $0 "[V][Trns_Ind][3Sg][2Sg]"}' underlying.tsv &> underlying8.tsv
#awk '{print $0 "[V][Trns_Ind][3Sg][3Sg]"}' underlying.tsv &> underlying9.tsv
#awk '{print $0 "[V][Trns_Ind][3Sg][3Pl]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[V][Trns_Ind][3Pl][3Sg]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[V][Trns_Ind][3Pl][3Pl]"}' underlying.tsv &> underlying3.tsv

# Possessed Oblique Case
#awk '{print $0 "[N][Abl_Mod][1SgPoss][SgPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abl_Mod][2SgPoss][SgPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abl_Mod][3SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Loc][1SgPoss][SgPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Loc][2SgPoss][SgPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Loc][3SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Ter][1SgPoss][SgPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Ter][2SgPoss][SgPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Ter][3SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Via][1SgPoss][SgPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Via][2SgPoss][SgPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Via][3SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Loc][1SgPoss][SgPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Loc][2SgPoss][SgPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Loc][3SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv

#######################
#      CHAPTER 8      #
#######################

# 2nd Person Subject Interrogatives
#awk '{print $0 "[V][Intrg][2Sg]"}' underlying.tsv &> underlying1.tsv 
#awk '{print $0 "[V][Intrg][2Pl]"}' underlying.tsv &> underlying2.tsv 
#awk '{print $0 "[V][Intrg][2Du]"}' underlying.tsv &> underlying3.tsv 
#awk '{print $0 "[V][Intrg][1Pl]"}' underlying.tsv &> underlying4.tsv 
#awk '{print $0 "[V][Intrg][1Du]"}' underlying.tsv &> underlying5.tsv 
#awk '{print $0 "[V][Intrg][2Sg][3Sg]"}' underlying.tsv &> underlying1.tsv 
#awk '{print $0 "[V][Intrg][2Sg][3Pl]"}' underlying.tsv &> underlying2.tsv 
#awk '{print $0 "[V][Intrg][2Sg][3Du]"}' underlying.tsv &> underlying3.tsv 
#awk '{print $0 "[V][Intrg][2Sg][1Sg]"}' underlying.tsv &> underlying4.tsv 
#awk '{print $0 "[V][Intrg][2Sg][1Pl]"}' underlying.tsv &> underlying5.tsv 

# 4th Person Possessor Possessed Absolutive
#awk '{print $0 "[N][Abs][4SgPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][4SgPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][4SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][4PlPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][4PlPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][4PlPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][4DuPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][4DuPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][4DuPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv

#######################
#      CHAPTER 9      #
#######################

# 3rd Person Subject Interrogatives
#awk '{print $0 "[V][Intrg][3Sg]"}' underlying.tsv &> underlying1.tsv 
#awk '{print $0 "[V][Intrg][3Pl]"}' underlying.tsv &> underlying2.tsv 
#awk '{print $0 "[V][Intrg][3Du]"}' underlying.tsv &> underlying3.tsv 
#awk '{print $0 "[V][Intrg][3Sg][1Sg]"}' underlying.tsv &> underlying1.tsv 
#awk '{print $0 "[V][Intrg][3Sg][1Pl]"}' underlying.tsv &> underlying2.tsv 
#awk '{print $0 "[V][Intrg][3Sg][3Sg]"}' underlying.tsv &> underlying3.tsv 
#awk '{print $0 "[V][Intrg][3Sg][3Pl]"}' underlying.tsv &> underlying4.tsv 
#awk '{print $0 "[V][Intrg][3Sg][3Du]"}' underlying.tsv &> underlying5.tsv 

# Optional Impersonal Agent Verb 
#awk '{print $0 "[V][Imprs_Agnt][3Sg][1Sg]"}' underlying.tsv &> underlying1.tsv 
#awk '{print $0 "[V][Imprs_Agnt][3Sg][2Sg]"}' underlying.tsv &> underlying2.tsv 
#awk '{print $0 "[V][Imprs_Agnt][3Sg][3Sg]"}' underlying.tsv &> underlying3.tsv 
#awk '{print $0 "[V][Imprs_Agnt][3Sg][3Pl]"}' underlying.tsv &> underlying4.tsv 

#######################
#      CHAPTER 10      #
#######################

# 2nd Person Subject / 1st Person Non-Singular Subject Optatives 
#awk '{print $0 "[V][Opt][PRES][2Sg]"}' underlying.tsv &> underlying1.tsv 
#awk '{print $0 "[V][Opt][PRES][2Pl]"}' underlying.tsv &> underlying2.tsv 
#awk '{print $0 "[V][Opt][PRES][2Du]"}' underlying.tsv &> underlying3.tsv 
#awk '{print $0 "[V][Opt][PRES][1Pl]"}' underlying.tsv &> underlying4.tsv 
#awk '{print $0 "[V][Opt][PRES][1Du]"}' underlying.tsv &> underlying5.tsv 

# 2nd Person Subject / 1st Person Non-Singular Subject Optatives 
awk '{print $0 "[V][Opt][PRES][2Sg][3Sg]"}' underlying.tsv &> underlying1.tsv 
awk '{print $0 "[V][Opt][PRES][2Sg][3Pl]"}' underlying.tsv &> underlying2.tsv 
awk '{print $0 "[V][Opt][PRES][2Sg][3Du]"}' underlying.tsv &> underlying3.tsv 
awk '{print $0 "[V][Opt][PRES][2Sg][1Sg]"}' underlying.tsv &> underlying4.tsv 
awk '{print $0 "[V][Opt][PRES][2Sg][1Pl]"}' underlying.tsv &> underlying5.tsv 

cat underlying[1-5].tsv | sort &> inputToSurface.tsv

rm underlying[1-5].tsv
