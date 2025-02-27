import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import squarify                                            #시각화


#CSV 파일을 불러와 DataFrame으로 반환
def load_data(file_path, encoding="EUC-KR"):
 
    df = pd.read_csv(file_path, encoding=encoding)
    columns0 = ['month', 'day', 'num', 'name', 'type']
    time_col = [f"{i}~{i+1}H" for i in range(5, 24)]          #5시 부터 24시까지 운영
    columns = columns0 + time_col + ['total']
#여기서 만약에 'total'(문자열) 을 인덱스로 추가해 버리면, type 뒤에 total이 정의되어서 총 total이 아닌, 5~6H인덱스의 합계가 total로 되어버린다. 따라서 리스트로 넣어줌
#이 csv 파일을 열어보면, total이 가장 끝에 있으므로, 끝으로 이동시켜주었다
    df.columns = columns
    return df
    
#데이터 그룹화 및 정리
def data(df):
    
    data = df.groupby(['month', 'day', 'num', 'name']).sum().reset_index()
    #월,일,번호,이름을 기준으로 각 인덱스의 합 표에 나타내줌
    gdata = data[['month', 'day', 'name', 'total']].sort_values(by=['name', 'day'], ascending=True)
    #data에서 월,일,역이름,합계를 가져온것을 gdata에 넣어줌
    #이름('name')열, 일('day')를 기준으로 정렬 함 , ascendging true =  가나다 ,알파벳순(오름차순)
    #젤 위에 있는 역이 가일테니 각산역이 나옴. 31개 출력
    
    mdata = gdata.groupby(by="name").sum().reset_index()
    tdata = mdata[['name', 'total']] 
    sdata = tdata.sort_values(by='total', ascending=False)       #내림차순, 큰거부터 정렬
    return sdata                                                 #최종 한 역의 한달치 출력
    

#상위 top 20개의 역 총 승하자 인원 트리맵으로 시각화
def top_stations(sdata, top_n=20, font_path="./D2Coding-Ver1.3.2-20180524.ttf"):

    fm.fontManager.addfont(font_path)
    plt.rcParams["font.family"] = "D2Coding"
    plt.rcParams['font.size'] = 16
    plt.rcParams['text.color'] = 'blue'
    
    total_data = sdata[:top_n]                                   #sdata의 상위 n개까지 자름
    plt.figure(figsize=(15, 8))
    squarify.plot(sizes=total_data['total'], label=total_data['name'], alpha=0.7)
    # total _data의 토탈 10개 까지만 자르기, alpha= 투명도 
    
    plt.gca().invert_yaxis()
    plt.axis("off")
    plt.show()

def main():
    file_path = "./대구교통공사_역별일별시간별승하차인원현황_20250131.csv"
    df = load_data(file_path)
    sdata = data(df)
    top_stations(sdata, top_n=20)

if __name__ == "__main__":
    main()
