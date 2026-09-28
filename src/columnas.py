tipos_datos = {
    "PONDERA": {"TIPO" :"int" ,   "COMPLETITUD" : 100},
    "ESTADO" : {"TIPO" :"int" ,   "COMPLETITUD" : 69},
    "CAT_OCUP": {"TIPO":"int",   "COMPLETITUD" : 92},
    "EDAD"   : {"TIPO" :"int" ,   "COMPLETITUD" : 78},
    "REGION" : {"TIPO" :"int" ,   "COMPLETITUD" : 86},
    "AGLOMERADO":{"TIPO":"int",  "COMPLETITUD" : 96},
    "MAS_500" : {"TIPO" :"str",   "COMPLETITUD" : 73},
    "ANO4"     : {"TIPO":"int" ,    "COMPLETITUD" : 70},
    "TRIMESTRE":{"TIPO" :"int",    "COMPLETITUD" : 42},
    "ITF":      {"TIPO" :"int",    "COMPLETITUD" : 75},
    "GDECCFR":  {"TIPO" :"int" ,   "COMPLETITUD" : 26}
}

docente={
    "columnas_interes": ['PONDERA', 'EDAD' , 'REGION'],
    "criterio_orden": "completitud",
    "forma" : "D",
    "completitud_minima": None
}
investigador={
    "columnas_interes": ['ITF','AGLOMERADO', 'TRIMESTRE'],
    "criterio_orden":"completitud",
    "forma": "D",
    "completitud_minima" : 60
}
analista={
     "columnas_interes": ['GDECCFR' , 'TRIMESTRE', 'ANO4' ],
        "criterio_orden": "nombre",
        "forma" : "A",
        "completitud_minima":80
}

roles={
    "docente":docente,
    "investigador":investigador,
    "analista":analista
}
############################


def informar_columnas(rol=None):
    """
    Muestra información de las columnas según el rol solicitado.
    Si no se especifica rol, muestra todas las columnas ordenadas
    por completitud de forma descendente. Si el rol no existe en
    'roles', informa que no es válido.
    """
     
    if rol is None:
        resultado = sorted(
            tipos_datos.items(),
            key=lambda item: item[1]['COMPLETITUD'],
            reverse=True
        )
        for nombre, datos in resultado:
            print(f"{nombre}: tipo={datos['TIPO']}, completitud={datos['COMPLETITUD']}%")
        return resultado

    elif rol not in roles:
        print(f"El rol '{rol}' no es válido.")
        return None

    else:
        columnas_interes = roles[rol]["columnas_interes"]
        criterio = roles[rol]["criterio_orden"]
        forma = roles[rol]["forma"]
        minimo = roles[rol]["completitud_minima"]

        if minimo is not None:
            columnas_interes = [col for col in columnas_interes if tipos_datos[col]['COMPLETITUD'] >= minimo]

        if criterio == "completitud":
            resultado = sorted(columnas_interes, key=lambda col: tipos_datos[col]['COMPLETITUD'], reverse=(forma == "D"))
        else:
            resultado = sorted(columnas_interes, key=lambda col: col, reverse=(forma == "D"))

        for col in resultado:
            print(f"{col}: tipo={tipos_datos[col]['TIPO']}, completitud={tipos_datos[col]['COMPLETITUD']}%")
        return resultado