#######################################################
#  _______        __  _______  __  ____  ____  _____  # 
# | ____\ \      / / | ____\ \/ / |  _ \|  _ \|  ___| #
# |  _|  \ \ /\ / /  |  _|  \  /  | |_) | | | | |_    #
# | |___  \ V  V /   | |___ /  \  |  __/| |_| |  _|   #
# |_____|  \_/\_/    |_____/_/\_\ |_|   |____/|_|     #
#                                                     #
#######################################################

######################################################
# import modules
# Modulen imortieren
# modulok importálása
######################################################

import ew_prj as prj

import ew_sw as sw
import ew_rw as rw
import ew_vs as vs

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B',  12)

h = 6

# Move to 8 cm to the right
# pdf.cell(80)
# Centered text in a framed 20*10 mm cell and line break
pdf.cell(0, h, 'Title', 1, 1, 'C')

pdf.cell(0, h, txt = prj.bauvorhaben, ln = 1)
pdf.cell(0, h, txt = prj.bauvorhaben_anschrift, ln = 1)
pdf.cell(0, h, txt = prj.bauherr, ln = 1)
pdf.cell(0, h, txt = prj.bauherr_anschrift, ln = 1)


# pdf.cell(0, h, txt = vs.rs_005, ln = 1)
pdf.cell(0, h, txt = vs.pdf_Q_zu, ln = 1)


pdf.output('ew_vs.pdf', 'F')





