import pandas as pd

def create_example():

    df = pd.DataFrame()

    df["time1"] = [
        "PSG",
        "PSG",
        "PSG",
        "PSG",
        "PSG"
    ]

    df["time2"] = [
        "Barcelona",
        "Real Madrid",
        "Chelsea",
        "Liverpool",
        "Juventus"
    ]

    df["Stage"] = [
        "Fase-de-Grupos",
        "Fase-de-Grupos",
        "Fase-de-Grupos",
        "Eliminatórias",
        "Final"
    ]

    df["Final"] = [
        [2,1],
        [1,1],
        [3,1],
        [5,4],
        [0,1]
    ]

    l = []

    for i in range(df.shape[0]):

        if df["Final"].loc[i][0] > df["Final"].loc[i][1]:
            l.append(df["time1"].loc[i])

        elif df["Final"].loc[i][0] < df["Final"].loc[i][1]:
            l.append((df["time2"].loc[i]))

        else:        
            l.append("Empate")

    df["Vencedor"] = l   
    
    return df

def create_score_book(dataframe):
    
    score_book = {}
    
    t1 = list(dataframe["time1"].value_counts().index)
    t2 = list(dataframe["time2"].value_counts().index)
    
    for team in (t1 + list(set(t2) - set(t1))):
        score_book[team] = 0
        
    return score_book

def get_points(stage):
    
    if stage == "Fase-de-Grupos":
        return 1
    
    elif stage == "Eliminatórias":
        return 2
    
    elif stage == "Final":
        return 5
    
def performance(df):

    score_book = create_score_book(df)
    
    for i in range(df.shape[0]):

        stage = (df["Stage"].loc[i])
        winner = (df["Vencedor"].loc[i])

        if winner != "Empate":

            score_book[winner] += get_points(stage)
            
    return score_book