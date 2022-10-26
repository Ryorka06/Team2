def cal_score(score):
    if score > 90:
        print ('a')
    elif 80 <= score <90:
        print ('b')
    elif 70 <= score <80:
        print ('c')
    elif 60 <= score <70:
        print ('d')
    else:
        print ('f')
def main():
    score = int(input())
    cal_score(score)


if __name__ == "__main__":
    main()