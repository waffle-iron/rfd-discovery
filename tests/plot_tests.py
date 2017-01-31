import matplotlib.pyplot as plt
import pandas as pd
import os
plt.style.use('ggplot')


def getfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.remove(".gitignore")
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    a.reverse()
    return a


def plot():
    dirpath = os.path.abspath("../resources/test")
    files = getfiles(dirpath)
    file_path = os.path.join(dirpath, files[0])
    test_df = pd.read_csv(file_path, sep=";")
    grouped_df = test_df.groupby(['ds_name']).mean()
    print(grouped_df)
    grouped_df['ds_file_size_B'].plot(y='time_elapsed')
    grouped_df['ds_len'].plot(y='time_elapsed')
    grouped_df.plot(x='ds_len', y='time_elapsed', kind='scatter', s=grouped_df['ds_attr_size']*1000)
    # TODO nomi dei ds
    plt.show()

plot()
