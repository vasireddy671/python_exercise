import json

def json_remover(x):
    obj  = json.load(open("test_payload.json"))
    for i in obj:
        for j in obj[i]:
            print(j)
            if j == str(x):
                obj[i].pop(j)
                break
        if i == str(x):
            obj.pop(i)
            break

    with open('updated_test_paylaod.json', 'w') as f:
        json.dump(obj,f, indent=2)

json_remover(input())   

        