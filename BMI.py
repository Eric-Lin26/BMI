height = float(input("請輸入身高： "))
height = height/100
weight = int(input("請輸入體重： "))
bmi = weight/height**2

if bmi >= 18.5 and bmi < 24:
    print("您的BMI值如下： ", bmi, "恭喜！您的BMI在正常範圍")
elif bmi < 18.5:
    print("您的BMI值如下： ", bmi, "您的體重過輕哦！")
elif bmi >= 24.1 and bmi <=27:
    print("您的BMI值如下： ", bmi, "您的體重過重哦！")
elif bmi >= 27.1 and bmi <= 30:
    print("您的BMI值如下： ", bmi, "您輕度肥胖哦！")
elif bmi >= 30.1 and bmi <= 35:
    print("您的BMI值如下： ", bmi, "您中度肥胖哦！")
else:
    print("您的BMI值如下： ", bmi, "您過度肥胖哦！")
