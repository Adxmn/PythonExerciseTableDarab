def awards(score):
    if score > 80:
        return "Gold"
    elif score > 60:
        return "Silver"
    elif score > 40:
        return "Bronze"
    else:
        return "You Fail"

def mark():
    stud = {}
    num = int(input("How many students: "))

    for x in range(num):
        name = input(f"Enter student {x+1} name: ")
        score = int(input(f"Enter {name}'s score: "))
        award = awards(score)
        stud[x+1] = {'name': name, 'score': score, 'award': award}

    print("Student scores and awards:")
    print("{:<5} {:<15} {:<10} {:<15}".format('NO', 'NAME', 'SCORE', 'AWARDS'))
    for num, info in stud.items():
        print("{:<5} {:<15} {:<10} {:<15}".format(num, info['name'], info['score'], info['award']))

if __name__ == '__main__':
    mark()