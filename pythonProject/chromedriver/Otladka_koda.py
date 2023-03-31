import pandas as pd

question1 = ["ept bl9"]
question2 = ["ept bl9ха муха, это второй вопрос"]
df = pd.DataFrame()
df['question1'] = question1

# for i in range(5):
#     new_data = {"A": i, "B": "a", "F": "b"}
#     df = df.append(new_data, ignore_index=True)
#     pass
answers1 = ["6 м2\n4,5 м2\nПлощадь на одно постоянное рабочее место пользователей персональных компьютеров на базе электронно-лучевой трубки, должна составлять не менее 6 м2, в помещениях культурно-развлекательных учреждений, на базе плоских дискретных экранов (жидкокристаллические, плазменные) - не менее 4,5 м2"]
print(len(answers1))
print(type(answers1))
new_row = []
for i in answers1:

    new_row = i.split("\n")
    print(len(i))
    print(type(i))
    print(new_row)
    # df['Answers'] = i
    # Записываем данные в таблицу Excel
    # print(df)
# df.to_excel('data.xlsx', index=False)
print(len(new_row))

answer1 = new_row[0]
answer2 = new_row[1]
answer3 = new_row[2]
print("Ответ 1:", answer1)
print("Ответ 2:", answer2)
print("Ответ 3:", answer3)

df["answer1"] = answer1
df["answer2"] = answer2
df["answer3"] = answer3

df.loc[len(df)] = [question2, answer1, answer2, answer3]
df.to_excel('xyyata.xlsx', index=False)
print(df)
# напиши что нибудь