#decimal - binario
def decimal_binario(decimal):
    binario = ""
    while(decimal>=2):
        binario = str(decimal%2) + binario
        decimal = decimal // 2
        if (decimal<2):
            binario = str(decimal) + binario
    return binario

#Decimal ternario
def decimal_ternario(decimal):
    ter = ""
    while(decimal>=3):
        ter = str(decimal%3) + ter
        decimal = decimal // 3
        if (decimal<3):
            ter = str(decimal) + ter
    return ter

#Decimal - cuaternario
def decimal_cuaternario(decimal):
    cua = ""
    while(decimal>=4):
        cua = str(decimal%4) + cua
        decimal = decimal // 4
        if (decimal<4):
            cua = str(decimal) + cua
    return cua

#decimal - octal
def decimal_octal(decimal):
    octal = ""
    while(decimal>=8):
        octal = str(decimal%8) + octal
        decimal = decimal // 8
        if (decimal<8):
            octal = str(decimal) + octal
    return octal

#decimal - hexadecimal
def decimal_hexadecimal(decimal):
    hexa = ""
    resto = ""
    while(decimal>=16):
        resto = str(decimal%16)
        if(resto == "10"):
            resto = "A"
        elif(resto == "11"):
            resto = "B"
        elif(resto == "12"):
            resto = "C"
        elif(resto == "13"):
            resto = "D"
        elif(resto == "14"):
            resto = "E"
        elif(resto =="15"):
            resto = "F"
        hexa = resto + hexa
        decimal = decimal//16
    
    if(decimal == 10):
        hexa = "A" + hexa
    elif(decimal == 11):
        hexa = "B" + hexa
    elif(decimal== 12):
        hexa = "C" + hexa
    elif(decimal == 13):
        hexa = "D" + hexa
    elif(decimal == 14):
        hexa = "E" + hexa
    elif(decimal ==15):
        hexa = "F" + hexa
    else:
        hexa = str(decimal) + hexa
    return hexa



#binario - decimal
def binario_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        if(binario[len(binario) - 1 - i]=="1"):
            decimal += 2**i
    return decimal

#ternario - decimal
def ternario_decimal(ter):
    decimal = 0
    for i in range(len(ter)):
        decimal += int(ter[len(ter) - 1 - i])*3**i
    return decimal

#Cuaternario - decimal
def cuaternario_decimal(cua):
    decimal = 0
    for i in range(len(cua)):
        decimal+=int(cua[len[cua]-1-i])*4**i
    return cua

#octal - decimal
def octal_decimal(octal):
    decimal = 0
    for i in range(len(octal)):
        decimal += int(octal[len(octal) - 1 - i])*8**i
    return decimal

#hexadecimal - decimal
def hexadecimal_decimal(hexa):
    decimal = 0
    for i in range(len(hexa)):
        if (hexa[len(hexa)-1-i].upper() == "A"):
            decimal += 10*16**i
        elif(hexa[len(hexa)-1-i].upper() == "B"):
            decimal += 11*16**i
        elif(hexa[len(hexa)-1-i].upper() == "C"):
            decimal += 12*16**i
        elif(hexa[len(hexa)-1-i].upper() == "D"):
            decimal += 13*16**i
        elif(hexa[len(hexa)-1-i].upper() == "E"):
            decimal += 14*16**i
        elif(hexa[len(hexa)-1-i].upper() == "F"):
            decimal += 15*16**i
        else:
            decimal += int(hexa[len(hexa) - 1 - i])*16**i
    return decimal

#Funcion para comprabar que el numero de la base especificada sea correcto
def comprobar(cadena,num):
    if(cadena.lower() =="decimal"):
        for char in num:
            if char not in "0123456789":
                return False
        if num == None:
            return False
        return True
    elif(cadena.lower() == "binario"):
        for char in num:
            if char not in "01":
                return False
        if num == None:
            return False
        return True
    elif(cadena.lower() == "octal"):
        for char in num:
            if char not in "01234567":
                return False
        if num == None:
            return False
        return True
    elif(cadena.lower() == "ternario"):
        for char in num:
            if char not in "012":
                return False
        if num == None:
            return False
        return True
    elif(cadena.lower() == "cuaternario"):
        for char in num:
            if char not in "0123":
                return False
        if num == None:
            return False
        return True
    elif(cadena.lower() == "hexadecimal"):
        for char in num:
            if char not in "0123456789ABCDEFabcdf":
                return False
        if num == None:
            return False
        return True

#Funcion para mostrar las conversiones
def basen(cadena,num):
    con = ""
    if(comprobar(cadena,num)):
        if(cadena.lower() =="decimal"):
            con="Decimal a binario: "+decimal_binario(int(num))+"\nDecimal a ternario: "+decimal_ternario(int(num))+"\nDecimal a cuaternario: "+decimal_cuaternario(int(num))+"\nDecimal a octal: "+decimal_octal(int(num))+"\nDecimal a hexadecimal: "+decimal_hexadecimal(int(num))
           
        elif(cadena.lower() == "binario"):
            con="Binario a decimal: "+str(binario_decimal(num))+"\nBinario a octal: "+decimal_octal(binario_decimal(num))+"\nBinario a hexadecimal: "+decimal_hexadecimal(binario_decimal(num))

        elif(cadena.lower() == "ternario"):
            con="Ternario a binario: "+decimal_binario(ternario_decimal(num))+"\nTernario a decimal: "+str(ternario_decimal(num))+"\nTernario a cuaternario: "+decimal_cuaternario(ternario_decimal(num))+"\nTernario a octal: "+decimal_octal(ternario_decimal(num))+"\nTernario a hexadecimal: "+decimal_hexadecimal(ternario_decimal(num))

        elif(cadena.lower() == "cuaternario"):
            con="Cuaternario a binario: "+decimal_binario(cuaternario_decimal(num))+"\nCuaternario a decimal: "+str(cuaternario_decimal(num))+"\nCuaternario a terciario: "+decimal_ternario(cuaternario_decimal(num))+"\nCuaternario a octal: "+decimal_octal(cuaternario_decimal(num))+"\nCuaternario a hexadecimal: "+decimal_hexadecimal(cuaternario_decimal(num))


        elif(cadena.lower() == "octal"):
            con="Octal a decimal: "+str(octal_decimal(num))+"\nOctal a binario: "+decimal_binario(octal_decimal(num))+"\nOctal a ternario: "+decimal_ternario(octal_decimal(num))+"\nOctal a cuaternario: "+decimal_cuaternario(octal_decimal(num))+"\nOctal a hexadecimal: "+decimal_hexadecimal(octal_decimal(num))
            
        elif(cadena.lower() == "hexadecimal"):
            con="Hexadecimal a decimal: "+str(hexadecimal_decimal(num))+"\nHexadecimal a binario: "+decimal_binario(hexadecimal_decimal(num))+"\nHexadecimal a ternario: "+decimal_ternario(hexadecimal_decimal(num))+"\nHexadecimal a cuaternario: "+decimal_cuaternario(hexadecimal_decimal(num))+"\nHexadecimal a octal: "+decimal_octal(hexadecimal_decimal(num))
        return con
    else:
        con="Numero de la base especificada escrito incorrectamente"
        return con



#basen(cadena,num)
