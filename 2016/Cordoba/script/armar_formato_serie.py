
#Serie_Matorrales.psv ->> ID..........................: 409
#Serie_Matorrales.psv ->> CLASIFICACION...............: Argiustol tipico
#Serie_Matorrales.psv ->> SERIE.......................: MATORRALES (Mtrrls)
#Serie_Matorrales.psv ->> UBICACION...................: 13 Km al Oeste de la localidad de Matorrales, departamento Rio Segundo
#Serie_Matorrales.psv ->> PROVINCIA...................: CORDOBA
#Serie_Matorrales.psv ->> LATITUD.....................: S314229
#Serie_Matorrales.psv ->> LONGITUD....................: O633900
#Serie_Matorrales.psv ->> ALTITUD.....................: 276
#Serie_Matorrales.psv ->> PENDIENTE...................: FALTA!
#Serie_Matorrales.psv ->> DRENAJE.....................: FALTA!
#Serie_Matorrales.psv ->> ESCURRIMIENTO...............: FALTA!
#Serie_Matorrales.psv ->> PERMEABILIDAD...............: FALTA!
#Serie_Matorrales.psv ->> TIPO DE SUELO...............: LIMOSA FINA, MIXTA, TERMICA
#Serie_Matorrales.psv ->> COLOR ......................: PARDO GRISÁCEO OSCURO A PARDO GRISACEO MUY OSCURO
#Serie_Matorrales.psv ->> HORIZONTE->NOMBRE(S)........: Ap   | Bt    | BC    | Ck
#Serie_Matorrales.psv ->> HORIZONTE->PROFUNDIDADES(CM): 0-21 | 21-52 | 52-76 | 76a+
#Serie_Matorrales.psv ->> HORIZONTE->MATERIA ORGÁN.(%): 2,3  | 0,8   | 0,7   | 0,4
#Serie_Matorrales.psv ->> HORIZONTE->CARBONO ORGÁN.(%): 1,3  | 0,5   | 0,4   | 0,2
#Serie_Matorrales.psv ->> HORIZONTE->NITRÓGENO TOT.(%): 0,15 | 0,08  |       |
#Serie_Matorrales.psv ->> HORIZONTE->RELACIÓN C/N.....: 8,8  | 5,9   |       |
#Serie_Matorrales.psv ->> HORIZONTE->ARCILLA 2 (%)....: 24,9 | 30,3  | 27,7  | 22,5
#Serie_Matorrales.psv ->> HORIZONTE->LIMO 2-50 (%)....: 69,2 | 60,5  | 65,0  | 69,6
#Serie_Matorrales.psv ->> HORIZONTE->AMF 50-100 (%)...: 5,9  | 5,8   | 6,5   | 8,2
#Serie_Matorrales.psv ->> HORIZONTE->AF 100-250 (%)...: 1,1  | 0,6   | 0,8   | 0,9
#Serie_Matorrales.psv ->> HORIZONTE->AM 250-500 (%)...: 0,1  | 0,1   | 0,1   |
#Serie_Matorrales.psv ->> HORIZONTE->AG 500-1000 (%)..: 0,1  | 0,1   | 0,1   |
#Serie_Matorrales.psv ->> HORIZONTE->AMG 1-2 mm (%)...:      |       |       |
#Serie_Matorrales.psv ->> HORIZONTE->CALCAREO CaCO3(%):      |       |       | 4,6
#Serie_Matorrales.psv ->> HORIZONTE->EQUIV. HUMEDAD(%): 25,3 | 25,3  | 24,3  | 22,6
#Serie_Matorrales.psv ->> HORIZONTE->PH PASTA.........: 6,2  | 7,5   | 7,8   | 8,3
#Serie_Matorrales.psv ->> HORIZONTE->PH H2O 1:2,5.....: 6,5  | 7,7   | 7,9   | 8,4 
#Serie_Matorrales.psv ->> HORIZONTE->CI ME/100G-Ca ++.: 12,4 | 16,3  | 16,5  |
#Serie_Matorrales.psv ->> HORIZONTE->CI ME/100G-Mg ++.: 2,4  | 1,1   | 0,6   |
#Serie_Matorrales.psv ->> HORIZONTE->CI ME/100G-Na +..: 0,2  | 0,1   | 0,1   | 0,2
#Serie_Matorrales.psv ->> HORIZONTE->CI ME/100G-K +...: 3,0  | 2,7   | 2,3   | 2,2
#Serie_Matorrales.psv ->> HORIZONTE->CI ME/100G-H +...: 1,2  |       |       |
#Serie_Matorrales.psv ->> HORIZONTE->SUM.B. ME/100G(S): 18,0 | 20,2  | 19,5  |
#Serie_Matorrales.psv ->> HORIZONTE->CIC ME/100G(T)...: 19,3 | 20,1  | 19,5  | 14,5
#Serie_Matorrales.psv ->> HORIZONTE->SAT.B % (S/T)....: 93   | 100   | 100   | 100

import string

fileName = 'FN.txt' 		#Se obtiene del nombre de archivo (sin el ID)
idNro = 'idNumero' 		#Se obtiene del nombre del archivo (numero de orden o ID)
clasificacion = 'clasif' 	#Se obtiene de "^CLASIFICACION:"
serie = 'serieeee' 		#Se obtiene de "^Serie"
simbolo = 'siimbolo' 		#Se obtiene de "^Simbolo:"
ubicacion = 'ubiccc' 		#Se obtiene de "^UBICACION:"
latitud = 'lattiud'		#Se obtiene de "^LATITUD:" (ojo dar este formato S345826)
longitud = 'loongitud'		#Se obtiene de "^LONGITUD:" (ojo dar este formato S345826)
altitud = 'allltitud'		#Se obtiene de "^ALTITUD:"
tipoSuelo = 'tpS'		#Se obtiene de "^TPS:"

hNomb = 'hNomb'
hProf = 'hProf'
hMatOrg = 'hMatOrg'
hCarbOrg = 'hCarbOrg'
hNitTot = 'hNitTot'
hRelCN = 'hRelCN'
hArcilla = 'hArcilla'
hLim = 'hLim'
hAMF = 'hAMF'
hAF = 'hAF'
hAM = 'hAM'
hAG = 'hAG'
hAMG = 'hAMG'
hCalc = 'hCalc'
hEqHum = 'hEqHum'
hPHPast = 'hPHPast'
hPHH2O = 'hPHH2O'
hCICa = 'hCICa'
hCIMg = 'hCIMg'
hCINa = 'hCINa'
hCIK = 'hCIK'
hCIH = 'hCIH'
hSumB = 'hSumB'
hCIC = 'hCIC'
hSatB = 'hSatB'


print('-----------------------------------------------------------------------------------------------------------------------------------------------------------')
print('{} ->> ID...........................: {}'.format( fileName, idNro ) )
print('{} ->> CLASIFICACION................: {}'.format( fileName, clasificacion ) )
print('{} ->> SERIE........................: {} ({})'.format( fileName, serie, simbolo ) )
print('{} ->> UBICACION....................: {}'.format( fileName, ubicacion ) )
print('{} ->> PROVINCIA....................: CORDOBA'.format( fileName ) )
print('{} ->> LATITUD......................: FALTA!'.format( fileName ) )
print('{} ->> LONGITUD.....................: FALTA!'.format( fileName ) )
print('{} ->> ALTITUD......................: FALTA!'.format( fileName ) )
print('{} ->> PENDIENTE....................: FALTA!'.format( fileName ) )
print('{} ->> DRENAJE......................: FALTA!'.format( fileName, drenaje ) )
print('{} ->> ESCURRIMIENTO................: FALTA!'.format( fileName ) )
print('{} ->> PERMEABILIDAD................: FALTA!'.format( fileName ) )
print('{} ->> TIPO DE SUELO................: {}'.format( fileName, tipoSuelo) )
print('{} ->> COLOR .......................: FALTA!'.format( fileName ) )
print('{} ->> HORIZONTE->NOMBRE(S).........: {}'.format( fileName, hNomb ) )
print('{} ->> HORIZONTE->PROFUNDIDADES(CM).: {}'.format( fileName, hProf ) )
print('{} ->> HORIZONTE->MATERIA ORGÁN.(%).: {}'.format( fileName, hMatOrg ) )
print('{} ->> HORIZONTE->CARBONO ORGÁN.(%).: {}'.format( fileName, hCarbOrg ) )
print('{} ->> HORIZONTE->NITRÓGENO TOT.(%).: {}'.format( fileName, hNitTot ) )
print('{} ->> HORIZONTE->RELACIÓN C/N......: {}'.format( fileName, hRelCN ) )
print('{} ->> HORIZONTE->ARCILLA 2 (%).....: {}'.format( fileName, hArcilla ) )
print('{} ->> HORIZONTE->LIMO 2-50 (%).....: {}'.format( fileName, hLim ) )
print('{} ->> HORIZONTE->AMF 50-100 (%)....: {}'.format( fileName, hAMF ) )
print('{} ->> HORIZONTE->AF 100-250 (%)....: {}'.format( fileName, hAF ) )
print('{} ->> HORIZONTE->AM 250-500 (%)....: {}'.format( fileName, hAM ) )
print('{} ->> HORIZONTE->AG 500-1000 (%)...: {}'.format( fileName, hAG ) )
print('{} ->> HORIZONTE->AMG 1-2 mm (%)....: {}'.format( fileName, hAMG ) )
print('{} ->> HORIZONTE->CALCAREO CaCO3(%).: {}'.format( fileName, hCalc ) )
print('{} ->> HORIZONTE->EQUIV. HUMEDAD(%).: {}'.format( fileName, hEqHum ) )
print('{} ->> HORIZONTE->PH PASTA..........: {}'.format( fileName, hPHPast ) )
print('{} ->> HORIZONTE->PH H2O 1:2,5......: {}'.format( fileName, hPHH2O ) )
print('{} ->> HORIZONTE->CI ME/100G-Ca ++..: {}'.format( fileName, hCICa ) )
print('{} ->> HORIZONTE->CI ME/100G-Mg ++..: {}'.format( fileName, hCIMg ) )
print('{} ->> HORIZONTE->CI ME/100G-Na +...: {}'.format( fileName, hCINa ) )
print('{} ->> HORIZONTE->CI ME/100G-K +....: {}'.format( fileName, hCIK ) )
print('{} ->> HORIZONTE->CI ME/100G-H +....: {}'.format( fileName, hCIH ) )
print('{} ->> HORIZONTE->SUM.B. ME/100G(S).: {}'.format( fileName, hSumB ) )
print('{} ->> HORIZONTE->CIC ME/100G(T)....: {}'.format( fileName, hCIC ) )
print('{} ->> HORIZONTE->SAT.B % (S/T).....: {}'.format( fileName, hSatB ) )
