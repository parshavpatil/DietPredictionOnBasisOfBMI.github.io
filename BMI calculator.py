while True:

        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine BMI category and print result
        if bmi < 18.5:
            print("Your BMI is", bmi, "which is considered Underweight.\n Your Diet plan is as follows \n :- Increase calorie intake with healthy sources like nuts, avocados, and lean proteins. Eat frequently and include protein-rich foods to promote weight gain.")
        elif bmi < 25:
            print("Your BMI is", bmi, "which is considered Normal.\n Your Diet plan is as follows \n :- Maintain a balanced diet with fruits, vegetables, whole grains, lean proteins, and healthy fats. Control portion sizes and engage in regular physical activity.")
        elif bmi < 30:
            print("Your BMI is", bmi, "which is considered Overweight.\n Your Diet plan is as follows \n :- Aim for a calorie deficit, consume nutrient-dense foods, limit added sugars, and exercise regularly for gradual weight loss.")
        else:
            print("Your BMI is", bmi, "which is considered Obesity.\n Your Diet plan is as follows \n :- Work with a professional to establish a calorie deficit, focus on whole foods, control portion sizes, and engage in regular exercise to promote weight loss.")
