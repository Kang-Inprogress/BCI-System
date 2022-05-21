def fe_recogniiton(fe_data): # 기쁨(low, high), 분노(low, high), 놀람(low, high), 중립
    result = ""
    # 놀람
    if(fe_data['uAct'] == 'surprise' and fe_data['eyeAct'] == 'neutral'):
        if(fe_data['lAct'] == 'clench'): # high
            result = "surprise_high"
        elif(fe_data['lAct'] == 'neutral'): # low
            result = "surprise_low"
        elif(fe_data['lAct'] == 'smile' or fe_data['lAct'] == 'laugh'):
            result = "happy_high"
    # 분노
    elif(fe_data['uAct'] == 'frown' and fe_data['eyeAct'] == 'neutral'):
        if(fe_data['lAct'] == 'clench'): # high
            result = "anger_high"
        elif(fe_data['lAct'] == 'neutral'): #low
            result = "anger_low"
        elif (fe_data['lAct'] == 'smile' or fe_data['lAct'] == 'laugh'):
            result = "happy_high"
    # 기쁨
    elif(fe_data['uAct'] == 'surprise' or fe_data['uAct'] == 'frown'):
        if(fe_data['eyeAct'] == 'winkL' or fe_data['eyeAct'] == 'winkR'):
            if(fe_data['lAct'] == 'smile'):
                result = "happy_high"
    elif(fe_data['uAct'] == 'neutral' and (fe_data['eyeAct'] == 'winkL' or fe_data['eyeAct'] == 'winkR' or fe_data['eyeAct'] == 'neutral')):
        if(fe_data['lAct'] == 'smile'):
            result == "happy_low"
    else:
        result = "neutral"

    return(result)