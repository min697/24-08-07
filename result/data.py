import pandas as pd
data = {
    '이름' : ['alice','bob', 'hong'],
    '나이' : [25, 30, 26],
    '성별' : ['여', '남', '남']
}
df = pd.DataFrame(data)
df.to_csv("./data.csv")