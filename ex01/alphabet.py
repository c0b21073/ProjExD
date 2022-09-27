import random

tai_mojisu = 10
kee_mojisu = 2
roop = 2
num_of_alphabet = 26

alphabet = [chr(i+65) for i in range(num_of_alphabet)]

for i in range(roop):
    tai = random.sample(alphabet,tai_mojisu)
    kee = random.sample(tai,kee_mojisu)
    hyo = list(set(tai) ^ set(kee))

    print("対象文字:",end="")
    for i in tai:
        print(i,end=" ")

    print("\n欠損文字:",end="")
    for i in kee:
        print(i,end=" ")

    print("\n表示文字:",end="")
    for i in hyo:
        print(i,end=" ")

    ans_n = int(input("\n欠損文字はいくつあるでしょうか？:"))
    if ans_n == kee_mojisu:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください。")
        for i in range(kee_mojisu):
            ans = input(f"{i+1}つ目の文字を入力してください:")
            if ans in kee:
                kee.remove(ans)

            else:
                break
    else:
        print("不正解です。またチャレンジしてください")
    print("--------------------")