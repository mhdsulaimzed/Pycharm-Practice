import json

def load_json():
    with open('journal.json') as j:
        data=json.load(j)
    for i in list(data):
        if i["squirrel"]:
            return data
        
        
def get_correlation(data, event):
    N11 = 0
    N00 = 0
    N10 = 0
    N01 = 0
    

    for entry in data:
        is_squirrel = entry['squirrel']
        is_event = event in entry['events']

        if is_squirrel and is_event:
            N11 += 1
        elif not is_squirrel and not is_event:
            N00 += 1
        elif not is_squirrel and is_event:
            N10 += 1
        elif is_squirrel and not is_event:
            N01 += 1

    phi = (N11 * N00 - N10 * N01) / ((N11 + N10) * (N01 + N00) * (N11 + N01) * (N10 + N00)) ** 0.5

    return phi
def main():
    data = load_json()
    entrylist=[]

    for i in data:
        for j in i["events"]:
            entrylist.append(j)
    correlation = {}
    print(entrylist)

    for i in entrylist:
        result = get_correlation(data,i)
        correlation[i]=result

    print("most_correlated_event =   "+max(correlation,key=correlation.get))

    print("min_correlated_event  =   "+min(correlation,key=correlation.get))


main()











