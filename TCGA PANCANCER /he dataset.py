{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bb1929d4",
   "metadata": {
    "papermill": {
     "duration": 0.00814,
     "end_time": "2022-06-28T01:42:25.893074",
     "exception": false,
     "start_time": "2022-06-28T01:42:25.884934",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**VISUALIZING THE TCGA PANCANCER DATASET**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d44aef58",
   "metadata": {
    "papermill": {
     "duration": 0.007149,
     "end_time": "2022-06-28T01:42:25.907444",
     "exception": false,
     "start_time": "2022-06-28T01:42:25.900295",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Importing the required libraries.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "841da4d9",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:25.924520Z",
     "iopub.status.busy": "2022-06-28T01:42:25.923522Z",
     "iopub.status.idle": "2022-06-28T01:42:44.222583Z",
     "shell.execute_reply": "2022-06-28T01:42:44.221781Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 18.309868,
     "end_time": "2022-06-28T01:42:44.225072",
     "exception": false,
     "start_time": "2022-06-28T01:42:25.915204",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.decomposition import PCA\n",
    "from sklearn.manifold import TSNE\n",
    "import umap.umap_ as umap"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a4afc519",
   "metadata": {
    "papermill": {
     "duration": 0.007495,
     "end_time": "2022-06-28T01:42:44.240332",
     "exception": false,
     "start_time": "2022-06-28T01:42:44.232837",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Loading the cancer dataset into a pandas dataframe for easy manipulation.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "dd2d6c79",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:44.257117Z",
     "iopub.status.busy": "2022-06-28T01:42:44.255816Z",
     "iopub.status.idle": "2022-06-28T01:42:57.292760Z",
     "shell.execute_reply": "2022-06-28T01:42:57.291965Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 13.047006,
     "end_time": "2022-06-28T01:42:57.294821",
     "exception": false,
     "start_time": "2022-06-28T01:42:44.247815",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "data = pd.read_csv('../input/pancancer/TCGA-PANCAN-HiSeq-801x20531/data.csv',index_col = 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "420cce23",
   "metadata": {
    "papermill": {
     "duration": 0.006727,
     "end_time": "2022-06-28T01:42:57.308924",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.302197",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Checking the number of rows and columns present in the dataset.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c4f8762c",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.324457Z",
     "iopub.status.busy": "2022-06-28T01:42:57.323863Z",
     "iopub.status.idle": "2022-06-28T01:42:57.328572Z",
     "shell.execute_reply": "2022-06-28T01:42:57.327866Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.014963,
     "end_time": "2022-06-28T01:42:57.330873",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.315910",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " The dataset has 801 rows and 20531 columns\n"
     ]
    }
   ],
   "source": [
    "rows, columns = data.shape\n",
    "print(f' The dataset has {rows} rows and {columns} columns')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a2ba886",
   "metadata": {
    "papermill": {
     "duration": 0.006903,
     "end_time": "2022-06-28T01:42:57.344775",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.337872",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Checking the first five rows of the dataset.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0c5c0140",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.360831Z",
     "iopub.status.busy": "2022-06-28T01:42:57.360154Z",
     "iopub.status.idle": "2022-06-28T01:42:57.390887Z",
     "shell.execute_reply": "2022-06-28T01:42:57.389933Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.04122,
     "end_time": "2022-06-28T01:42:57.393349",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.352129",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>gene_0</th>\n",
       "      <th>gene_1</th>\n",
       "      <th>gene_2</th>\n",
       "      <th>gene_3</th>\n",
       "      <th>gene_4</th>\n",
       "      <th>gene_5</th>\n",
       "      <th>gene_6</th>\n",
       "      <th>gene_7</th>\n",
       "      <th>gene_8</th>\n",
       "      <th>gene_9</th>\n",
       "      <th>...</th>\n",
       "      <th>gene_20521</th>\n",
       "      <th>gene_20522</th>\n",
       "      <th>gene_20523</th>\n",
       "      <th>gene_20524</th>\n",
       "      <th>gene_20525</th>\n",
       "      <th>gene_20526</th>\n",
       "      <th>gene_20527</th>\n",
       "      <th>gene_20528</th>\n",
       "      <th>gene_20529</th>\n",
       "      <th>gene_20530</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>sample_0</th>\n",
       "      <td>0.0</td>\n",
       "      <td>2.017209</td>\n",
       "      <td>3.265527</td>\n",
       "      <td>5.478487</td>\n",
       "      <td>10.431999</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.175175</td>\n",
       "      <td>0.591871</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>4.926711</td>\n",
       "      <td>8.210257</td>\n",
       "      <td>9.723516</td>\n",
       "      <td>7.220030</td>\n",
       "      <td>9.119813</td>\n",
       "      <td>12.003135</td>\n",
       "      <td>9.650743</td>\n",
       "      <td>8.921326</td>\n",
       "      <td>5.286759</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sample_1</th>\n",
       "      <td>0.0</td>\n",
       "      <td>0.592732</td>\n",
       "      <td>1.588421</td>\n",
       "      <td>7.586157</td>\n",
       "      <td>9.623011</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.816049</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>4.593372</td>\n",
       "      <td>7.323865</td>\n",
       "      <td>9.740931</td>\n",
       "      <td>6.256586</td>\n",
       "      <td>8.381612</td>\n",
       "      <td>12.674552</td>\n",
       "      <td>10.517059</td>\n",
       "      <td>9.397854</td>\n",
       "      <td>2.094168</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sample_2</th>\n",
       "      <td>0.0</td>\n",
       "      <td>3.511759</td>\n",
       "      <td>4.327199</td>\n",
       "      <td>6.881787</td>\n",
       "      <td>9.870730</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.972130</td>\n",
       "      <td>0.452595</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>5.125213</td>\n",
       "      <td>8.127123</td>\n",
       "      <td>10.908640</td>\n",
       "      <td>5.401607</td>\n",
       "      <td>9.911597</td>\n",
       "      <td>9.045255</td>\n",
       "      <td>9.788359</td>\n",
       "      <td>10.090470</td>\n",
       "      <td>1.683023</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sample_3</th>\n",
       "      <td>0.0</td>\n",
       "      <td>3.663618</td>\n",
       "      <td>4.507649</td>\n",
       "      <td>6.659068</td>\n",
       "      <td>10.196184</td>\n",
       "      <td>0.0</td>\n",
       "      <td>7.843375</td>\n",
       "      <td>0.434882</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>6.076566</td>\n",
       "      <td>8.792959</td>\n",
       "      <td>10.141520</td>\n",
       "      <td>8.942805</td>\n",
       "      <td>9.601208</td>\n",
       "      <td>11.392682</td>\n",
       "      <td>9.694814</td>\n",
       "      <td>9.684365</td>\n",
       "      <td>3.292001</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sample_4</th>\n",
       "      <td>0.0</td>\n",
       "      <td>2.655741</td>\n",
       "      <td>2.821547</td>\n",
       "      <td>6.539454</td>\n",
       "      <td>9.738265</td>\n",
       "      <td>0.0</td>\n",
       "      <td>6.566967</td>\n",
       "      <td>0.360982</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>5.996032</td>\n",
       "      <td>8.891425</td>\n",
       "      <td>10.373790</td>\n",
       "      <td>7.181162</td>\n",
       "      <td>9.846910</td>\n",
       "      <td>11.922439</td>\n",
       "      <td>9.217749</td>\n",
       "      <td>9.461191</td>\n",
       "      <td>5.110372</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 20531 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          gene_0    gene_1    gene_2    gene_3     gene_4  gene_5    gene_6  \\\n",
       "sample_0     0.0  2.017209  3.265527  5.478487  10.431999     0.0  7.175175   \n",
       "sample_1     0.0  0.592732  1.588421  7.586157   9.623011     0.0  6.816049   \n",
       "sample_2     0.0  3.511759  4.327199  6.881787   9.870730     0.0  6.972130   \n",
       "sample_3     0.0  3.663618  4.507649  6.659068  10.196184     0.0  7.843375   \n",
       "sample_4     0.0  2.655741  2.821547  6.539454   9.738265     0.0  6.566967   \n",
       "\n",
       "            gene_7  gene_8  gene_9  ...  gene_20521  gene_20522  gene_20523  \\\n",
       "sample_0  0.591871     0.0     0.0  ...    4.926711    8.210257    9.723516   \n",
       "sample_1  0.000000     0.0     0.0  ...    4.593372    7.323865    9.740931   \n",
       "sample_2  0.452595     0.0     0.0  ...    5.125213    8.127123   10.908640   \n",
       "sample_3  0.434882     0.0     0.0  ...    6.076566    8.792959   10.141520   \n",
       "sample_4  0.360982     0.0     0.0  ...    5.996032    8.891425   10.373790   \n",
       "\n",
       "          gene_20524  gene_20525  gene_20526  gene_20527  gene_20528  \\\n",
       "sample_0    7.220030    9.119813   12.003135    9.650743    8.921326   \n",
       "sample_1    6.256586    8.381612   12.674552   10.517059    9.397854   \n",
       "sample_2    5.401607    9.911597    9.045255    9.788359   10.090470   \n",
       "sample_3    8.942805    9.601208   11.392682    9.694814    9.684365   \n",
       "sample_4    7.181162    9.846910   11.922439    9.217749    9.461191   \n",
       "\n",
       "          gene_20529  gene_20530  \n",
       "sample_0    5.286759         0.0  \n",
       "sample_1    2.094168         0.0  \n",
       "sample_2    1.683023         0.0  \n",
       "sample_3    3.292001         0.0  \n",
       "sample_4    5.110372         0.0  \n",
       "\n",
       "[5 rows x 20531 columns]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d0b527bf",
   "metadata": {
    "papermill": {
     "duration": 0.007251,
     "end_time": "2022-06-28T01:42:57.408114",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.400863",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Checking for missing values in the dataset.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "146deae1",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.424319Z",
     "iopub.status.busy": "2022-06-28T01:42:57.424026Z",
     "iopub.status.idle": "2022-06-28T01:42:57.506007Z",
     "shell.execute_reply": "2022-06-28T01:42:57.505106Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.092628,
     "end_time": "2022-06-28T01:42:57.508599",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.415971",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 0 missing values in the dataset.\n"
     ]
    }
   ],
   "source": [
    "null = data.isnull().sum().sum()\n",
    "print(f'There are {null} missing values in the dataset.')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6936000b",
   "metadata": {
    "papermill": {
     "duration": 0.007466,
     "end_time": "2022-06-28T01:42:57.523827",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.516361",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Loading the labels of the dataset into a dataframe.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cb72956f",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.540643Z",
     "iopub.status.busy": "2022-06-28T01:42:57.540075Z",
     "iopub.status.idle": "2022-06-28T01:42:57.550928Z",
     "shell.execute_reply": "2022-06-28T01:42:57.550229Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.021049,
     "end_time": "2022-06-28T01:42:57.552778",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.531729",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "label =pd.read_csv('../input/pancancer/TCGA-PANCAN-HiSeq-801x20531/labels.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a351684",
   "metadata": {
    "papermill": {
     "duration": 0.007185,
     "end_time": "2022-06-28T01:42:57.567326",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.560141",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Checking the first five values of the label.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "17306231",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.583079Z",
     "iopub.status.busy": "2022-06-28T01:42:57.582785Z",
     "iopub.status.idle": "2022-06-28T01:42:57.590604Z",
     "shell.execute_reply": "2022-06-28T01:42:57.589899Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.017517,
     "end_time": "2022-06-28T01:42:57.592179",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.574662",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>sample_0</td>\n",
       "      <td>PRAD</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>sample_1</td>\n",
       "      <td>LUAD</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>sample_2</td>\n",
       "      <td>PRAD</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>sample_3</td>\n",
       "      <td>PRAD</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>sample_4</td>\n",
       "      <td>BRCA</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Unnamed: 0 Class\n",
       "0   sample_0  PRAD\n",
       "1   sample_1  LUAD\n",
       "2   sample_2  PRAD\n",
       "3   sample_3  PRAD\n",
       "4   sample_4  BRCA"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "label.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e81e507b",
   "metadata": {
    "papermill": {
     "duration": 0.007662,
     "end_time": "2022-06-28T01:42:57.608001",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.600339",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Checking the number of rows and columns of the label.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7076266c",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.624108Z",
     "iopub.status.busy": "2022-06-28T01:42:57.623638Z",
     "iopub.status.idle": "2022-06-28T01:42:57.627732Z",
     "shell.execute_reply": "2022-06-28T01:42:57.627016Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.014875,
     "end_time": "2022-06-28T01:42:57.630416",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.615541",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 801 rows and 2 columns of labels\n"
     ]
    }
   ],
   "source": [
    "rows, columns =label.shape\n",
    "print(f'There are {rows} rows and {columns} columns of labels')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05768a21",
   "metadata": {
    "papermill": {
     "duration": 0.007405,
     "end_time": "2022-06-28T01:42:57.646378",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.638973",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Checking for missing values in the label.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e9afadef",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.663161Z",
     "iopub.status.busy": "2022-06-28T01:42:57.662508Z",
     "iopub.status.idle": "2022-06-28T01:42:57.668719Z",
     "shell.execute_reply": "2022-06-28T01:42:57.667988Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.017254,
     "end_time": "2022-06-28T01:42:57.671200",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.653946",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 0 missing labels\n"
     ]
    }
   ],
   "source": [
    "null = label.isnull().sum().sum()\n",
    "print(f'There are {null} missing labels')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8eee287f",
   "metadata": {
    "papermill": {
     "duration": 0.007493,
     "end_time": "2022-06-28T01:42:57.687347",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.679854",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Checking the cancer types in the dataset.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c1f1cd8e",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.703945Z",
     "iopub.status.busy": "2022-06-28T01:42:57.703282Z",
     "iopub.status.idle": "2022-06-28T01:42:57.711252Z",
     "shell.execute_reply": "2022-06-28T01:42:57.710419Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.018003,
     "end_time": "2022-06-28T01:42:57.712912",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.694909",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['PRAD', 'LUAD', 'BRCA', 'KIRC', 'COAD'], dtype=object)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "label['Class'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b08685f",
   "metadata": {
    "papermill": {
     "duration": 0.00759,
     "end_time": "2022-06-28T01:42:57.728192",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.720602",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Converting the dataset into a 2d numpy array and checking the first two rows.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e517c874",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.745075Z",
     "iopub.status.busy": "2022-06-28T01:42:57.744394Z",
     "iopub.status.idle": "2022-06-28T01:42:57.750645Z",
     "shell.execute_reply": "2022-06-28T01:42:57.749769Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.01656,
     "end_time": "2022-06-28T01:42:57.752450",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.735890",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.        , 2.01720929, 3.26552691, ..., 8.92132623, 5.28675919,\n",
       "        0.        ],\n",
       "       [0.        , 0.59273209, 1.58842082, ..., 9.39785429, 2.09416849,\n",
       "        0.        ]])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = data.values\n",
    "X[:2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89b1c5b0",
   "metadata": {
    "papermill": {
     "duration": 0.007696,
     "end_time": "2022-06-28T01:42:57.768069",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.760373",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Standardizing the dataset...z = (sample -mean)/standard deviation.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "40350998",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:57.785267Z",
     "iopub.status.busy": "2022-06-28T01:42:57.784584Z",
     "iopub.status.idle": "2022-06-28T01:42:58.022646Z",
     "shell.execute_reply": "2022-06-28T01:42:58.021833Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.248723,
     "end_time": "2022-06-28T01:42:58.024752",
     "exception": false,
     "start_time": "2022-06-28T01:42:57.776029",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "SS= StandardScaler()\n",
    "S_data = SS.fit_transform(X)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a142566",
   "metadata": {
    "papermill": {
     "duration": 0.007765,
     "end_time": "2022-06-28T01:42:58.040826",
     "exception": false,
     "start_time": "2022-06-28T01:42:58.033061",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Creating functions for the visualization tools.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "244e4625",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:58.057799Z",
     "iopub.status.busy": "2022-06-28T01:42:58.057474Z",
     "iopub.status.idle": "2022-06-28T01:42:58.067739Z",
     "shell.execute_reply": "2022-06-28T01:42:58.066973Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.020725,
     "end_time": "2022-06-28T01:42:58.069407",
     "exception": false,
     "start_time": "2022-06-28T01:42:58.048682",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "def pca(X, y):\n",
    "\tpca = PCA(n_components = 2)\n",
    "\tpca_data = pca.fit_transform(X)\n",
    "\tP_df = pd.DataFrame(pca_data, columns= ['pca1', 'pca2']).join(y)\n",
    "\treturn sns.scatterplot(x ='pca1', y = 'pca2', hue='Class', data = P_df)\n",
    "\t\n",
    "def tsne(X, y):\n",
    "\ttsne = TSNE(n_components = 2, learning_rate = 5, random_state = 42, init = 'random')\n",
    "\tt_data = tsne.fit_transform(X)\n",
    "\tt_df = pd.DataFrame(t_data, columns = ['tsne1','tsne2']).join(y)\n",
    "\treturn sns.scatterplot(x = 'tsne1', y = 'tsne2', hue = 'Class', data = t_df)\n",
    "\t\n",
    "\n",
    "def pca_tsne(X, y):\n",
    "\tpca = PCA(n_components = 50)\n",
    "\tp_data = pca.fit_transform(X)\n",
    "\ttsne = TSNE(n_components = 2, learning_rate = 5, random_state = 42, init ='random')\n",
    "\tt_data = tsne.fit_transform(p_data)\n",
    "\tt_df = pd.DataFrame(t_data, columns = ['p_tsne1', 'p_tsne2']).join(y)\n",
    "\treturn sns.scatterplot(x = 'p_tsne1', y = 'p_tsne2', hue = 'Class', data = t_df)\t\n",
    "\t\n",
    "def Umap(X, y):\n",
    "\tUmap = umap.UMAP(n_components = 2)\n",
    "\tu_data = Umap.fit_transform(X)\n",
    "\tu_df = pd.DataFrame(u_data, columns = ['umap1','umap2']).join(y)\n",
    "\treturn sns.scatterplot(x = 'umap1', y = 'umap2', hue = 'Class', data = u_df)\t\n",
    "\t\t"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf9164c4",
   "metadata": {
    "papermill": {
     "duration": 0.007543,
     "end_time": "2022-06-28T01:42:58.084683",
     "exception": false,
     "start_time": "2022-06-28T01:42:58.077140",
     "status": "completed"
    },
    "tags": []
   },
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "51e202f0",
   "metadata": {
    "papermill": {
     "duration": 0.007606,
     "end_time": "2022-06-28T01:42:58.100089",
     "exception": false,
     "start_time": "2022-06-28T01:42:58.092483",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**THE VISUALIZATION PLOTS WITH COLOR BY CANCER TYPE**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0355cd6d",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:42:58.117234Z",
     "iopub.status.busy": "2022-06-28T01:42:58.116457Z",
     "iopub.status.idle": "2022-06-28T01:43:00.019942Z",
     "shell.execute_reply": "2022-06-28T01:43:00.019182Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 1.914657,
     "end_time": "2022-06-28T01:43:00.022396",
     "exception": false,
     "start_time": "2022-06-28T01:42:58.107739",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "VISUALIZATION WITH PRINCIPAL COMPONENT ANALYSIS\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "pca(S_data, label)\n",
    "print('VISUALIZATION WITH PRINCIPAL COMPONENT ANALYSIS')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "33b9fd60",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:43:00.041993Z",
     "iopub.status.busy": "2022-06-28T01:43:00.041693Z",
     "iopub.status.idle": "2022-06-28T01:43:05.218883Z",
     "shell.execute_reply": "2022-06-28T01:43:05.218155Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 5.189023,
     "end_time": "2022-06-28T01:43:05.220723",
     "exception": false,
     "start_time": "2022-06-28T01:43:00.031700",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "VISUALIZATION WITH T-DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "tsne(S_data, label)\n",
    "print('VISUALIZATION WITH T-DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c77dd011",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:43:05.242391Z",
     "iopub.status.busy": "2022-06-28T01:43:05.242093Z",
     "iopub.status.idle": "2022-06-28T01:43:13.207445Z",
     "shell.execute_reply": "2022-06-28T01:43:13.206773Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 7.978049,
     "end_time": "2022-06-28T01:43:13.209175",
     "exception": false,
     "start_time": "2022-06-28T01:43:05.231126",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "VISUALIZATION WITH PRINCIPAL COMPONENT ANALYSIS + T- DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "pca_tsne(S_data, label)\n",
    "print('VISUALIZATION WITH PRINCIPAL COMPONENT ANALYSIS + T- DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b344f8ac",
   "metadata": {
    "_cell_guid": "b3911a97-5721-46ba-899e-552fa759d817",
    "_uuid": "17344906-ac3e-4d9a-a8dd-74585d3de1b6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-06-28T01:43:13.231874Z",
     "iopub.status.busy": "2022-06-28T01:43:13.231486Z",
     "iopub.status.idle": "2022-06-28T01:43:24.664421Z",
     "shell.execute_reply": "2022-06-28T01:43:24.663715Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 11.445962,
     "end_time": "2022-06-28T01:43:24.666081",
     "exception": false,
     "start_time": "2022-06-28T01:43:13.220119",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "VISUALIZATION WITH UNIFORM MANIFOLD APPROXIMATION AND PROJECTION\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "Umap(S_data, label)\n",
    "print('VISUALIZATION WITH UNIFORM MANIFOLD APPROXIMATION AND PROJECTION')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 70.374902,
   "end_time": "2022-06-28T01:43:27.986588",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2022-06-28T01:42:17.611686",
   "version": "2.3.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
