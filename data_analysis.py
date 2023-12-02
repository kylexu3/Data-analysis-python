# -*- coding: utf-8 -*-
"""data analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h3JjBupJKM0ZRLCQkjJsDW1hYBoJQGf3
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Path to where the results are hosted online
# This loads the data into a Pandas dataframe
Data=pd.read_csv('https://raw.githubusercontent.com/kylexu3/exp/main/nao.csv', sep=',')

# Macro to help with presenting the final plot.
# %matplotlib inline


# The following will produce a boxplot where each box collates
# (collects together) the measurements for all angles, at the
# distance intervals.
#
# Note that, we specify the data source for the plot with data=Data
# x axis set using the label column, 'Distance'
# y axis set using the label column, 'Measurement'
#

plt.figure(figsize=(12, 8))
bplot = sns.boxplot(y='competence', x='robot', data=Data, width=0.5)
bplot.set_title('Competence rating for Each Robot')
plt.figure(figsize=(12, 8))
bplot = sns.boxplot(y='warmth', x='robot', data=Data, width=0.5)
bplot.set_title('Warmth rating for Each Robot')
plt.figure(figsize=(12, 8))
bplot = sns.boxplot(y='discomfort', x='robot', data=Data, width=0.5)
bplot.set_title('Discomfort rating for Each Robot')
plt.figure(figsize=(12, 8))
bplot = sns.boxplot(y='PE', x='robot', data=Data, width=0.5)
bplot.set_title('Performance Expectation rating for Each Robot')
plt.figure(figsize=(12, 8))
bplot = sns.boxplot(y='EE', x='robot', data=Data, width=0.5)
bplot.set_title('Effort Expectancy rating for Each Robot')
plt.figure(figsize=(12, 8))
bplot = sns.boxplot(y='SI', x='robot', data=Data, width=0.5)
bplot.set_title('Social Influence rating for Each Robot')
plt.figure(figsize=(12, 8))
bplot = sns.boxplot(y='correct', x='robot1', data=Data, width=0.5)
bplot.set_title('Correct rate for each robot')
plt.figure(figsize=(12, 8))
bplot = sns.boxplot(y='correct1', x='illustrated', data=Data, width=0.5)
bplot.set_title('Correct rate before illustration or not')
# %matplotlib inline

# List of features
features = ['competence', 'warmth', 'discomfort', 'PE', 'EE', 'SI']
feature_labels = {
    'competence': 'Competence',
    'warmth': 'Warmth',
    'discomfort': 'Discomfort',
    'PE': 'Performance Expectation',
    'EE': 'Effort Expectancy',
    'SI': 'Social Influence'
}

# Create a 2x3 subplot grid
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))

# Loop through features and create box plots
for i, feature in enumerate(features):
    row = i // 3
    col = i % 3
    bplot = sns.boxplot(y=feature, x='robot', data=Data, width=0.5, ax=axes[row, col])
    bplot.set_title(f'{feature_labels[feature]} Rating for Each Robot')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Path to where the results are hosted online
# This loads the data into a Pandas dataframe
Data = pd.read_csv('https://raw.githubusercontent.com/kylexu3/exp/main/nao.csv', sep=',')

# Macro to help with presenting the final plot.
# %matplotlib inline

# Create a figure and axis
plt.figure(figsize=(12, 8))
bplot = sns.boxplot(y='Scores', x='robot', data=Data, width=0.5)
bplot.set_title('Participants Scores for Each Robot')

# Add group name annotation to the x-axis
group_names = ['competence', 'warmth', 'discomfort', 'PE', 'EE', 'SI']
group_positions = [0.5, 2.5, 4.5, 6.5, 8.5, 10.5]
for name, position in zip(group_names, group_positions):
    plt.text(position, bplot.get_ylim()[0] - 0.0001, name, fontsize=12, ha='center')

plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
df=pd.read_csv('https://raw.githubusercontent.com/kylexu3/exp/main/nao.csv', sep=',')
df['gender'] = df['gender'].str.strip()
gender_counts = df['gender'].value_counts()

labels = gender_counts.index
sizes = gender_counts.values

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Gender Distribution')
plt.show()

df['injuries'] = df['injuries'].str.strip()
injuries_counts = df['injuries'].value_counts()

labels = injuries_counts.index
sizes = injuries_counts.values

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Muscularskeletal Injuries Distribution')
plt.show()

df['memory'] = df['memory'].str.strip()
memory_counts = df['memory'].value_counts()

labels = memory_counts.index
sizes = memory_counts.values

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Memory Difficulties Distribution')
plt.show()

df['hearing'] = df['hearing'].str.strip()
hearing_counts = df['hearing'].value_counts()

labels = hearing_counts.index
sizes = hearing_counts.values

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Hearing Problem Distribution')
plt.show()

df['glasses'] = df['glasses'].str.strip()
glasses_counts = df['glasses'].value_counts()

labels = glasses_counts.index
sizes = glasses_counts.values

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Glasses Wearing Distribution')
plt.show()

df['education'] = df['education'].str.strip()
education_counts = df['education'].value_counts()

labels = education_counts.index
sizes = education_counts.values

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Education Level Distribution')
plt.show()

# 根据年龄范围进行分组
age_bins = [40, 50, 60, float('inf')]
age_labels = ['40-50', '50-60', '60+']

df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
age_counts = df['age_group'].value_counts()

labels = age_counts.index
sizes = age_counts.values

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Age Distribution')
plt.show()


df['attitudeN'] = df['attitudeN'].str.strip()
attitudeN_counts = df['attitudeN'].value_counts()

labels = attitudeN_counts.index
sizes =attitudeN_counts.values

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Participants Attitudes with NAO')
plt.show()

df['attitudeP'] = df['attitudeP'].str.strip()
attitudeN_counts = df['attitudeP'].value_counts()

labels = attitudeN_counts.index
sizes =attitudeN_counts.values

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Participants Attitudes with PEPPER')
plt.show()

df['gender'] = df['gender'].str.strip()
df['injuries'] = df['injuries'].str.strip()
df['hearing'] = df['hearing'].str.strip()
df['glasses'] = df['glasses'].str.strip()
df['education'] = df['education'].str.strip()

df['gender'] = df['gender'].str.strip()
df['injuries'] = df['injuries'].str.strip()
df['hearing'] = df['hearing'].str.strip()
df['glasses'] = df['glasses'].str.strip()
df['education'] = df['education'].str.strip()

# 创建一个2x3的子图布局
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
mpl.rcParams['font.size'] = 14
# 绘制饼图并将其放入子图中
def plot_pie(ax, data, title):
    counts = data.value_counts()
    labels = counts.index
    sizes = counts.values
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    ax.title.set_fontsize(30)  # 设置子图标题的字体大小
    ax.set_title(title)
# 添加大标题
plt.suptitle("Demographic Data Distribution", fontsize=20)

# 绘制子图
plot_pie(axes[0, 0], df['gender'], 'a')
plot_pie(axes[0, 1], df['injuries'], 'b')
plot_pie(axes[0, 2], df['hearing'], 'c')
plot_pie(axes[1, 0], df['glasses'], 'd')
plot_pie(axes[1, 1], df['education'], 'e')

# 调整子图之间的间距
plt.tight_layout()
fig.delaxes(axes[1, 2])

# 显示图
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib as mpl
df=pd.read_csv('https://raw.githubusercontent.com/kylexu3/exp/main/nao.csv', sep=',')
df['attitudeN'] = df['attitudeN'].str.strip()
attitudeN_counts = df['attitudeN'].value_counts()
labels_N = attitudeN_counts.index
sizes_N = attitudeN_counts.values
mpl.rcParams['font.size'] = 16
# 生成第二个饼图
df['attitudeP'] = df['attitudeP'].str.strip()
attitudeP_counts = df['attitudeP'].value_counts()
labels_P = attitudeP_counts.index
sizes_P = attitudeP_counts.values

# 创建一个1行2列的子图布局
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# 绘制第一个子图（左边）
axs[0].pie(sizes_N, labels=labels_N, autopct='%1.1f%%', startangle=140)
axs[0].set_title('a')

# 绘制第二个子图（右边）
axs[1].pie(sizes_P, labels=labels_P, autopct='%1.1f%%', startangle=140)
axs[1].set_title('b')
plt.suptitle("Participants' Attitudes Towards Two Robots", fontsize=20)
# 调整子图布局
plt.tight_layout()

# 显示图表
plt.show()