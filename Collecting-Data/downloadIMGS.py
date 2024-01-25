import pandas as pd 
import requests
import os 

def download_img(url, folder, df_name):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            img_name = os.path.join(folder, os.path.basename(df_name + url))

            with open(img_name, 'wb') as f:
                f.write(response.content)
            return img_name

    except Exception as e:
        print(f"img couldnot download, :Error : {e}")
        

def main(img_url, df_name):
    folder = "../Data/imgs"
    os.makedirs(folder, exist_ok=True)
    download_img(img_url, folder, df_name)

for i in ['data_1.csv']:
    downloaded_imgs = []

    df = pd.read_csv('../Data/news-Data/' + i)
    df['img_paht'] = None

    for a in range(len(df)):
        img = df['Img_url'][a]
        main(img, i)