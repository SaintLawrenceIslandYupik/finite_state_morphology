#!/bin/bash

# To block comment  :1,10s/^/#/
# To uncomment      :1,10s/^#//

# ABSOLUTIVE
#awk '{print $0 "[N][Abs][Du]"}' underlying.tsv &> underlying1.tsv
#awk '{print $0 "[N][Abs][Pl]"}' underlying.tsv &> underlying2.tsv
#awk '{print $0 "[N][Abs][Sg]"}' underlying.tsv &> underlying3.tsv

# ABLATIVE-MODALIS
#awk '{print $0 "[N][Abl_Mod][Unpd][Sg]"}' underlying.tsv | sort &> inputToSurface.tsv

# INTRANSITIVE INDICATIVE
#awk '{print $0 "[V][Intr_Ind][1Du]"}' underlying.tsv &> underlying1.tsv 
#awk '{print $0 "[V][Intr_Ind][1Pl]"}' underlying.tsv &> underlying2.tsv 
#awk '{print $0 "[V][Intr_Ind][1Sg]"}' underlying.tsv &> underlying3.tsv 
#awk '{print $0 "[V][Intr_Ind][2Du]"}' underlying.tsv &> underlying4.tsv 
#awk '{print $0 "[V][Intr_Ind][2Pl]"}' underlying.tsv &> underlying5.tsv 
#awk '{print $0 "[V][Intr_Ind][2Sg]"}' underlying.tsv &> underlying6.tsv 
#awk '{print $0 "[V][Intr_Ind][3Du]"}' underlying.tsv &> underlying7.tsv 
#awk '{print $0 "[V][Intr_Ind][3Pl]"}' underlying.tsv &> underlying8.tsv 
#awk '{print $0 "[V][Intr_Ind][3Sg]"}' underlying.tsv &> underlying9.tsv 

# LOCALIS / TERMINALIS / VIALIS / EQUALIS CASE
#awk '{print $0 "[N][Loc][Unpd][Sg]"}' underlying.Ch2.N.tsv &> underlying1.tsv
#awk '{print $0 "[N][Loc][Unpd][Pl]"}' underlying.Ch2.N.tsv &> underlying2.tsv
#awk '{print $0 "[N][Ter][Unpd][Sg]"}' underlying.Ch2.N.tsv &> underlying1.tsv
#awk '{print $0 "[N][Ter][Unpd][Pl]"}' underlying.Ch2.N.tsv &> underlying2.tsv
#awk '{print $0 "[N][Via][Unpd][Sg]"}' underlying.Ch2.N.tsv &> underlying1.tsv
#awk '{print $0 "[N][Via][Unpd][Pl]"}' underlying.Ch2.N.tsv &> underlying2.tsv
awk '{print $0 "[N][Equ][Unpd][Sg]"}' underlying.Ch2.N.tsv &> underlying1.tsv
awk '{print $0 "[N][Equ][Unpd][Pl]"}' underlying.Ch2.N.tsv &> underlying2.tsv


cat underlying[1-2].tsv | sort &> inputToSurface.tsv

rm underlying[1-2].tsv
