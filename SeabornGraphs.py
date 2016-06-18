# from https://web.stanford.edu/~mwaskom/software/seaborn/tutorial/distributions.html


import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


np.random.seed(sum(map(ord, "distributions")))

x = np.random.normal(size = 100)
sns.distplot(x);

mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])
sns.jointplot(x="x", y="y", data=df);

sns.jointplot(x="x", y="y", data=df, kind="kde");

f, ax = plt.subplots(figsize=(6, 6))
sns.kdeplot(df.x, df.y, ax=ax)
sns.rugplot(df.x, color="g", ax=ax)
sns.rugplot(df.y, vertical=True, ax=ax);

iris = sns.load_dataset("iris")
sns.pairplot(iris);