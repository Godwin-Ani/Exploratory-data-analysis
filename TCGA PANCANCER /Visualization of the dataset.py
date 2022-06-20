# %% [markdown]
# **VISUALIZING THE TCGA PANCANCER DATASET**

# %% [markdown]
# **Importing the required libraries.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T20:45:11.258165Z","iopub.execute_input":"2022-06-19T20:45:11.258595Z","iopub.status.idle":"2022-06-19T20:45:33.444539Z","shell.execute_reply.started":"2022-06-19T20:45:11.258512Z","shell.execute_reply":"2022-06-19T20:45:33.443541Z"}}
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap.umap_ as umap

# %% [markdown]
# **Loading the cancer dataset into a pandas dataframe for easy manipulation.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:13:23.530534Z","iopub.execute_input":"2022-06-19T21:13:23.531065Z","iopub.status.idle":"2022-06-19T21:13:39.062633Z","shell.execute_reply.started":"2022-06-19T21:13:23.531023Z","shell.execute_reply":"2022-06-19T21:13:39.061873Z"}}
data = pd.read_csv('../input/pancancer/TCGA-PANCAN-HiSeq-801x20531/data.csv',index_col = 0)

# %% [markdown]
# **Checking the number of rows and columns present in the dataset.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:21:52.722656Z","iopub.execute_input":"2022-06-19T21:21:52.723107Z","iopub.status.idle":"2022-06-19T21:21:52.728857Z","shell.execute_reply.started":"2022-06-19T21:21:52.723066Z","shell.execute_reply":"2022-06-19T21:21:52.727735Z"}}
rows, columns = data.shape
print(f' The dataset has {rows} rows and {columns} columns')

# %% [markdown]
# **Checking the first five rows of the dataset.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:15:57.787630Z","iopub.execute_input":"2022-06-19T21:15:57.788780Z","iopub.status.idle":"2022-06-19T21:15:57.829092Z","shell.execute_reply.started":"2022-06-19T21:15:57.788740Z","shell.execute_reply":"2022-06-19T21:15:57.828363Z"}}
data.head()

# %% [markdown]
# **Checking for missing values in the dataset.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:20:57.031193Z","iopub.execute_input":"2022-06-19T21:20:57.031604Z","iopub.status.idle":"2022-06-19T21:20:57.130630Z","shell.execute_reply.started":"2022-06-19T21:20:57.031573Z","shell.execute_reply":"2022-06-19T21:20:57.129585Z"}}
null = data.isnull().sum().sum()
print(f'There are {null} missing values in the dataset.')

# %% [markdown]
# **Loading the labels of the dataset into a dataframe.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:30:36.057588Z","iopub.execute_input":"2022-06-19T21:30:36.058392Z","iopub.status.idle":"2022-06-19T21:30:36.079339Z","shell.execute_reply.started":"2022-06-19T21:30:36.058349Z","shell.execute_reply":"2022-06-19T21:30:36.078361Z"}}
label =pd.read_csv('../input/pancancer/TCGA-PANCAN-HiSeq-801x20531/labels.csv')

# %% [markdown]
# **Checking the first five values of the label.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:36:45.974445Z","iopub.execute_input":"2022-06-19T21:36:45.974941Z","iopub.status.idle":"2022-06-19T21:36:45.984766Z","shell.execute_reply.started":"2022-06-19T21:36:45.974910Z","shell.execute_reply":"2022-06-19T21:36:45.984101Z"}}
label.head()

# %% [markdown]
# **Checking the number of rows and columns of the label.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:43:28.018560Z","iopub.execute_input":"2022-06-19T21:43:28.019693Z","iopub.status.idle":"2022-06-19T21:43:28.025582Z","shell.execute_reply.started":"2022-06-19T21:43:28.019646Z","shell.execute_reply":"2022-06-19T21:43:28.024576Z"}}
rows, columns =label.shape
print(f'There are {rows} rows and {columns} columns of labels')

# %% [markdown]
# **Checking for missing values in the label.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:44:13.908534Z","iopub.execute_input":"2022-06-19T21:44:13.909175Z","iopub.status.idle":"2022-06-19T21:44:13.916114Z","shell.execute_reply.started":"2022-06-19T21:44:13.909136Z","shell.execute_reply":"2022-06-19T21:44:13.915374Z"}}
null = label.isnull().sum().sum()
print(f'There are {null} missing labels')

# %% [markdown]
# **Checking the cancer types in the dataset.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:44:35.348363Z","iopub.execute_input":"2022-06-19T21:44:35.349077Z","iopub.status.idle":"2022-06-19T21:44:35.355896Z","shell.execute_reply.started":"2022-06-19T21:44:35.349038Z","shell.execute_reply":"2022-06-19T21:44:35.355007Z"}}
label['Class'].unique()

# %% [markdown]
# **Converting the dataset into a 2d numpy array and checking the first two rows.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T21:51:15.664978Z","iopub.execute_input":"2022-06-19T21:51:15.665432Z","iopub.status.idle":"2022-06-19T21:51:15.671948Z","shell.execute_reply.started":"2022-06-19T21:51:15.665397Z","shell.execute_reply":"2022-06-19T21:51:15.671186Z"}}
X = data.values
X[:2]

# %% [markdown]
# **Standardizing the dataset...z = (sample -mean)/standard deviation.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T22:04:03.359834Z","iopub.execute_input":"2022-06-19T22:04:03.360221Z","iopub.status.idle":"2022-06-19T22:04:03.738622Z","shell.execute_reply.started":"2022-06-19T22:04:03.360193Z","shell.execute_reply":"2022-06-19T22:04:03.737547Z"}}
SS= StandardScaler()
S_data = SS.fit_transform(X)

# %% [markdown]
# **Creating functions for the visualization tools.**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T22:10:57.352159Z","iopub.execute_input":"2022-06-19T22:10:57.353044Z","iopub.status.idle":"2022-06-19T22:10:57.366349Z","shell.execute_reply.started":"2022-06-19T22:10:57.353000Z","shell.execute_reply":"2022-06-19T22:10:57.365256Z"}}
def pca(X, y):
	pca = PCA(n_components = 2)
	pca_data = pca.fit_transform(X)
	P_df = pd.DataFrame(pca_data, columns= ['pca1', 'pca2']).join(y)
	return sns.scatterplot(x ='pca1', y = 'pca2', hue='Class', data = P_df)
	
def tsne(X, y):
	tsne = TSNE(n_components = 2, learning_rate = 5, random_state = 42, init = 'random')
	t_data = tsne.fit_transform(X)
	t_df = pd.DataFrame(t_data, columns = ['tsne1','tsne2']).join(y)
	return sns.scatterplot(x = 'tsne1', y = 'tsne2', hue = 'Class', data = t_df)
	

def pca_tsne(X, y):
	pca = PCA(n_components = 50)
	p_data = pca.fit_transform(X)
	tsne = TSNE(n_components = 2, learning_rate = 5, random_state = 42, init ='random')
	t_data = tsne.fit_transform(p_data)
	t_df = pd.DataFrame(t_data, columns = ['p_tsne1', 'p_tsne2']).join(y)
	return sns.scatterplot(x = 'p_tsne1', y = 'p_tsne2', hue = 'Class', data = t_df)	
	
def Umap(X, y):
	Umap = umap.UMAP(n_components = 2)
	u_data = Umap.fit_transform(X)
	u_df = pd.DataFrame(u_data, columns = ['umap1','umap2']).join(y)
	return sns.scatterplot(x = 'umap1', y = 'umap2', hue = 'Class', data = u_df)	
		

# %% [markdown]
# 

# %% [markdown]
# **THE VISUALIZATION PLOTS WITH COLOR BY CANCER TYPE**

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T22:04:46.052973Z","iopub.execute_input":"2022-06-19T22:04:46.054016Z","iopub.status.idle":"2022-06-19T22:04:48.353780Z","shell.execute_reply.started":"2022-06-19T22:04:46.053972Z","shell.execute_reply":"2022-06-19T22:04:48.352631Z"}}
pca(S_data, label)
print('VISUALIZATION WITH PRINCIPAL COMPONENT ANALYSIS')

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T22:08:21.879515Z","iopub.execute_input":"2022-06-19T22:08:21.880684Z","iopub.status.idle":"2022-06-19T22:08:25.839466Z","shell.execute_reply.started":"2022-06-19T22:08:21.880641Z","shell.execute_reply":"2022-06-19T22:08:25.838547Z"}}
tsne(S_data, label)
print('VISUALIZATION WITH T-DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING') 

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T22:11:04.953066Z","iopub.execute_input":"2022-06-19T22:11:04.953508Z","iopub.status.idle":"2022-06-19T22:11:11.247841Z","shell.execute_reply.started":"2022-06-19T22:11:04.953473Z","shell.execute_reply":"2022-06-19T22:11:11.246866Z"}}
pca_tsne(S_data, label)
print('VISUALIZATION WITH PRINCIPAL COMPONENT ANALYSIS + T- DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING')

# %% [code] {"jupyter":{"outputs_hidden":false},"execution":{"iopub.status.busy":"2022-06-19T22:12:41.745923Z","iopub.execute_input":"2022-06-19T22:12:41.746831Z","iopub.status.idle":"2022-06-19T22:12:55.678486Z","shell.execute_reply.started":"2022-06-19T22:12:41.746766Z","shell.execute_reply":"2022-06-19T22:12:55.677465Z"}}
Umap(S_data, label)
print('VISUALIZATION WITH UNIFORM MANIFOLD APPROXIMATION AND PROJECTION')