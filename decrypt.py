

message = "lOrEm Ipsum dOLOr SiT AmET cONSEcTetUR AdIPisCIng ElIt SEd dO eIusMOD tEMPOR iNCIdIDuNt Ut " \
    +"LABOrE Et DoLorE MAGNA aLiQuA UT enIM Ad MInIM vENIAM QUis NOstRUd ExErCiTaTiON uLLamCo LABorIS " \
    +"niSi UT ALIQu Ip EX Ea COmmODo CoNsEQUaT dUiS aUTe iRure DOloR iN ReprEHenDeRIT iN VoLUPTAte VEliT " \
    +"EsSE ciLLum Dol oRE eu FuGIat nULlA PArIATUr ExCePtEuR SiNT OCcAECat cUpIDAtAT NOn PRoId"

mask = ""
for char in message:
    if char.isspace():
        continue
    if char.isupper():
        mask += "1"
    else:
        mask += "0"
#print mask

key = {'0':'00000', '1':'00001', '2':'00010', '3':'00011', '4':'00100', '5':'00101', 
    '6':'00110', '7':'00111', '8':'01000', '9':'01001', 'A':'01010', 'B':'01011', 
    'C':'01100', 'D':'01101', 'E':'01110', 'F':'01111', 'G':'10000', 'H':'10001',
    'I':'10010', 'J':'10011', 'K':'10011', 'L':'10100', 'M':'10101', 'N':'10110',
    'O':'10111', 'P':'11000', 'Q':'11000', 'R':'11001', 'S':'11010', 'T':'11011',
    'U':'11100', 'V':'11101', 'W':'11110', 'X':'11110', 'Y':'11111', 'Z':'11111'}

inv_key = {v: k for k, v in key.iteritems()}
#print inv_key

result = ""
for i in xrange(0, len(mask), 5):
    result += inv_key[mask[i:i+5]]

print result