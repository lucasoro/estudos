def ArrayToString(array,string):
    s = ""
    for i in range(len(array)):
        if i != len(array) -1:
            s += array[i] + " "+string+" "
        else:
            s += array[i]
    return s


uni = ""
fase = []
det = ""
naoLembro = []

query = "SELECT * FROM data_Patrimonio.tutu inner join teste on teste.ID = tutu.testeID $REPLACE"
array = []

if uni != "":
    array.append("numTerr = " + uni)
if fase != []:
    array.append("fase in( " + ArrayToString(fase,",")+")")
if det != "":
    array.append("numTerr = " + det)
if naoLembro != []:
    array.append("fase in( " + ArrayToString(naoLembro,",")+")")
if len(array) > 0:
    query = query.replace("$REPLACE", "where "+ArrayToString(array,"and"))
else:
    query = query.replace("$REPLACE", "")
print(query)