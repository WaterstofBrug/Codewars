import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


def hystats_scrape(user):
    url = f"https://hystats.net/player/skywars/team_normal/{user}"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    k_d = soup.findAll('span')[123].text
    w_l = soup.findAll('span')[129].text

    return k_d, w_l


def hystats_entry(user):
    f = open(f"stat_holder/hystats/{user}.txt", "a")
    scrape = hystats_scrape(user)
    if scrape == ('0', '0'):
        print('no data')
    else:
        f.write(f'{str(scrape)}\n')
    f.close()


def hystats_print(user):
    f = open(f"stat_holder/hystats/{user}.txt", "r")
    w_l = []
    k_d = []
    remove_list = ['(', ')', ',', "'", '\n']
    for line in f.readlines():
        for char in remove_list:
            line = line.replace(char, '')
        line = line.split(' ')
        w_l.append(float(line[1]))
        k_d.append(float(line[0]))
    return w_l, k_d


def hystats_visualiser(user):
    w_l, k_d = hystats_print(user)
    w_l, k_d = np.array(w_l), np.array(k_d)

    x = np.array([i for i in range(len(w_l))])

    xnew = np.linspace(x.min(), x.max(), 200)
    spl_w_l = make_interp_spline(x, w_l, k=3)
    w_l_smooth = spl_w_l(xnew)
    spl_k_d = make_interp_spline(x, k_d, k=3)
    k_d_smooth = spl_k_d(xnew)

    plt.plot(xnew, w_l_smooth, label="W/L")
    plt.plot(xnew, k_d_smooth, label="K/D")

    plt.title(f'skywars stats {user}')

    plt.legend()
    plt.show()


#hystats_entry('Goatk1ck')
#hystats_entry('Diekss')
#print(hystats_print('Diekss'))
hystats_visualiser('Diekss')
