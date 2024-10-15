from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from .forms import *
from django.templatetags.static import static
from django.http import HttpResponse
from io import BytesIO
import base64
import seaborn as sns
import matplotlib.pyplot as plt
from.models import *
# Create your views here.
def index(request):
    return render(request, 'stockmarketpredictionsapp/index.html')

def stocklist(request):
    form = compprofileForm()
    names = DataSetSearchBar.objects.all().values()
    return render(request, 'stockmarketpredictionsapp/stocklist.html', {'names':names, 'form':form})

def stockprofile(request):
    return render(request, 'stockmarketpredictionsapp/stockprofile.html')

def testinput(request):
    if request.method == 'POST':
        form = predictionForm(request.POST)
        if form.is_valid():
            df = pd.read_excel(r'C:\APOLLOHOSP.xlsx')

            open = int(form.cleaned_data['open'])
            prevclose = int(form.cleaned_data['prevclose'])
            ltp = int(form.cleaned_data['ltp'])

            X = df.drop(['LOW ', 'Date '], axis=1)
            y = df['LOW ']
            model = LinearRegression()
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
            model.fit(X_train, y_train)

            highvalue = model.predict([[950, X[:1:]['HIGH '], 952, 962, X[:1:]['close '], X[:1:]['vwap '],
                                    X[:1:]['52W H '], X[:1:]['52W L '], X[:1:]['VOLUME '], X[:1:]['VALUE '],
                                    X[:1:]['No of trades ']]])
            return render(request, 'stockmarketpredictionsapp/regressionoutput.html', {'highvalue':highvalue})
    else :
        form = predictionForm()
    return render(request, 'stockmarketpredictionsapp/regressiontestinput.html', {'form':form})

def testoutput(request):
    return render(request, 'stockmarketpredictionsapp/regressiontestouput.html')

def printurl(request):
    url = static(r'stockmarketpredictions/datasets/APOLLOHOSP.xlsx')
    df = pd.read_excel(r'C:\BAJFINANCE.xlsx')
    X = df.drop(['LOW ', 'Date '], axis=1)
    y = df['LOW ']
    model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    print(type(X[:1:]['No of trades ']))

    return HttpResponse('Hello')


def companyprofile(request):
    form = compprofileForm(request.POST)
    form1 = predictionForm(request.POST)

    if form.is_valid():
        sitename = form.cleaned_data['name']
        try:
            coname = DataSetSearchBar.objects.filter(sitename=sitename).values()[0]['name']
        except Exception as e:
            return render(request, 'stockmarketpredictionsapp/companyprofileerror.html')
        compname= str(coname)

        path = 'C:\Django\stockmarketpredictions\media\datasets'+"\\"+compname+'.xlsx'
        df = pd.read_excel(path)

        close = int(df[:1:]['close '])
        vwap = int(df[:1:]['vwap '])
        fwh = int(df[:1:]['52W H '])
        fwl = int(df[:1:]['52W L '])
        volume = int(df[:1:]['VOLUME '])
        value = int(df[:1:]['VALUE '])
        nooftrades = int(df[:1:]['No of trades '])

        # plot = sns.relplot(data=df, kind='line', y='OPEN ', x = 'Date ')
        # buffer = BytesIO
        # plot.savefig(buffer, format='png')

        plot = plt.plot(df['Date '], df['OPEN '])

        # buffer = BytesIO()
        # plt.savefig(buffer, format='png')
        # buffer.seek(0)
        # image_png = buffer.getvalue()
        # buffer.close()
        #
        # graphic = base64.b64encode(image_png)
        # graphic = graphic.decode('utf-8')
        return render(request, 'stockmarketpredictionsapp/companyprofile.html', {'close':close, 'vwap':vwap, 'fwh':fwh, 'fwl':fwl, 'volume':volume, 'value':value, 'nooftrades':nooftrades,
                                                                                 'compname':compname, 'graphing_plot':'a', 'sitename':sitename, 'form':form1, 'graphic':'graphic'})
    else:
        return render(request, 'stockmarketpredictionsapp/stocklist.html', {'form':form1})

def predictionoutput(request):
    form = predictionForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            sitename = form.cleaned_data['sitename']
            try:
                coname = DataSetSearchBar.objects.filter(sitename=sitename).values()[0]['name']
            except Exception as e:
                return render(request, 'stockmarketpredictionsapp/companyprofileerror.html')

            compname = str(coname)
            path = 'C:\Django\stockmarketpredictions\media\datasets' + "\\" + compname + '.xlsx'
            df = pd.read_excel(path)
            Xhigh = df.drop(['HIGH ', 'Date ', ], axis=1)
            yhigh = df['HIGH ']
            Xlow = df.drop(['LOW ', 'Date ', ], axis=1)
            ylow = df['LOW ']

            modelhigh = LinearRegression()
            X_trainhigh, X_testhigh, y_trainhigh, y_testhigh = train_test_split(Xhigh, yhigh, test_size=0.3, random_state=0)
            modellow = LinearRegression()
            X_trainlow, X_testlow, y_trainlow, y_testlow = train_test_split(Xlow, ylow, test_size=0.3, random_state=0)

            modellow.fit(X_trainlow, y_trainlow)
            modelhigh.fit(X_trainlow, y_trainlow)

            OPEN = int(form.cleaned_data['open'])
            PrevClose = int(form.cleaned_data['prevclose'])
            LTP = int(form.cleaned_data['ltp'])

            xlow1 = Xlow[:1:]
            xhigh1 = Xhigh[:1:]

            xlow1.loc[0, "OPEN "] = OPEN
            xlow1.loc[0, "PREV. CLOSE "] = PrevClose
            xlow1.loc[0, "ltp "] = LTP

            xhigh1.loc[0, "OPEN "] = OPEN
            xhigh1.loc[0, "PREV. CLOSE "] = PrevClose
            xhigh1.loc[0, "ltp "] = LTP

            LOWvalue = modellow.predict(xlow1)
            HIGHvalue = modelhigh.predict(xhigh1)

            return render(request, 'stockmarketpredictionsapp/predictionoutput.html', {'highvalue':HIGHvalue, 'lowvalue':LOWvalue})

    return render(request, 'stockmarketpredictionsapp/predictionoutput.html')
