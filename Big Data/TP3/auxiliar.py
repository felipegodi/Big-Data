def limpiar_eph(eph):

    '''
        función para limpiar la eph
        input:
            eph: Variable que tenga almacenada la eph sin limpiar

        output:
            eph: Variable que tiene almacenada la eph limpia
    '''
    
    eph.dropna(thresh = 1, inplace = True) # Si tiene todos NA, la fila se va
    eph.dropna(thresh = 1, axis = "columns", inplace = True) # Si la columna tiene todos NA, la columna se va
    #La primer parte es para individual
    try:
        # Si no lo defino como uno me dropea un montón de filas que tienen NaN
        eph.PP08D1 = eph.PP08D1.fillna(0)
        eph.PP08F2 = eph.PP08F2.fillna(0)
        # dropeo observaciones con valores que no tienen sentido. CH06 = edad, PP08D1, P21, P47T, ITF y IPCF son todas variables
        # de ingresos, no pueden ser menores a 0
        eph.drop(eph[(eph["CH06"] < 0) | (eph["PP08D1"] < 0) | (eph["P21"] < 0) | \
                           (eph["P47T"] < 0) | (eph["ITF"] < 0) | (eph["IPCF"] < 0) | (eph["PP08F2"] < 0)].index, inplace = True)
        eph["CH14"].fillna(99, inplace = True) #Muchos no respondieron entonces reemplazamos los missing por 99. 
    except:
        print("No se encontró alguna columna, revisar")
    eph.fillna(0, inplace = True) # Relleno todos con 0 las columnas que son subcategorías
    eph.reset_index(inplace = True, drop = True)    
        
    return eph

def drop_y(df):
    
    '''
        Dropea las columnas que terminan en '_y'
    '''
    
    to_drop = [x for x in df if x.endswith('_y')]
    df.drop(to_drop, axis=1, inplace=True)
    
    return df