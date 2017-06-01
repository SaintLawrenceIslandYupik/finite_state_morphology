#!/bin/bash

# To block comment  :1,10s/^/#/
# To uncomment      :1,10s/^#//

# CHAPTER 2 - Absolutive 
#awk '{print $0 "[N][Abs][Du]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][Pl]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][Sg]"}' underlying.tsv &> underlying3.tsv

# CHAPTER 3 - Ablative-Modalis 
#awk '{print $0 "[N][Abl_Mod][Unpd][Sg]"}' underlying.tsv | sort &> inputToSurface.tsv

# CHAPTER 3 - Intransitive Indicative 
#awk '{print $0 "[V][Intr_Ind][1Du]"}' underlying.tsv &> underlying1.tsv 
#awk '{print $0 "[V][Intr_Ind][1Pl]"}' underlying.tsv &> underlying2.tsv 
#awk '{print $0 "[V][Intr_Ind][1Sg]"}' underlying.tsv &> underlying3.tsv 
#awk '{print $0 "[V][Intr_Ind][2Du]"}' underlying.tsv &> underlying4.tsv 
#awk '{print $0 "[V][Intr_Ind][2Pl]"}' underlying.tsv &> underlying5.tsv 
#awk '{print $0 "[V][Intr_Ind][2Sg]"}' underlying.tsv &> underlying6.tsv 
#awk '{print $0 "[V][Intr_Ind][3Du]"}' underlying.tsv &> underlying7.tsv 
#awk '{print $0 "[V][Intr_Ind][3Pl]"}' underlying.tsv &> underlying8.tsv 
#awk '{print $0 "[V][Intr_Ind][3Sg]"}' underlying.tsv &> underlying9.tsv 

# CHAPTER 4 - 1st/2nd Person Possessed Possessor Absolutive
#awk '{print $0 "[N][Abs][1SgPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][1SgPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][1SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
awk '{print $0 "[N][Abs][2SgPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
awk '{print $0 "[N][Abs][2SgPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
awk '{print $0 "[N][Abs][2SgPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][1PlPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][1PlPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][1PlPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv
#awk '{print $0 "[N][Abs][2PlPoss][DuPosd]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][2PlPoss][PlPosd]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][2PlPoss][SgPosd]"}' underlying.tsv &> underlying3.tsv

# LOCALIS / TERMINALIS / VIALIS / EQUALIS CASE
#awk '{print $0 "[N][Loc][Unpd][Sg]"}' underlying.Ch2.N.tsv &> underlying1.tsv
#awk '{print $0 "[N][Loc][Unpd][Pl]"}' underlying.Ch2.N.tsv &> underlying2.tsv
#awk '{print $0 "[N][Ter][Unpd][Sg]"}' underlying.Ch2.N.tsv &> underlying1.tsv
#awk '{print $0 "[N][Ter][Unpd][Pl]"}' underlying.Ch2.N.tsv &> underlying2.tsv
#awk '{print $0 "[N][Via][Unpd][Sg]"}' underlying.Ch2.N.tsv &> underlying1.tsv
#awk '{print $0 "[N][Via][Unpd][Pl]"}' underlying.Ch2.N.tsv &> underlying2.tsv
#awk '{print $0 "[N][Equ][Unpd][Sg]"}' underlying.Ch2.N.tsv &> underlying1.tsv
#awk '{print $0 "[N][Equ][Unpd][Pl]"}' underlying.Ch2.N.tsv &> underlying2.tsv


cat underlying[1-3].tsv | sort &> inputToSurface.tsv

rm underlying[1-3].tsv
