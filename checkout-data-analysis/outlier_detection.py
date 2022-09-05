def IQR(data, feature, value):
    q1 = data[feature].percentile(0.25)
    q3 = data[feature].percentile(0.75)
    iqr = q3 - q1

    limite_superior = q3 + (1.5 * iqr)
    limite_inferior = q1 - (1.5 * iqr)

    return (value > limite_superior) or (value < limite_inferior)
