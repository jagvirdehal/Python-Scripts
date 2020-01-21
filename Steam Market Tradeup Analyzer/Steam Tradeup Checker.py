#List of qualities for each Weapon Skin
qual = ['Battle-Scarred','Well-Worn','Field-Tested','Minimal Wear','Factory New']
#List of Weapon skins for each Weapon, including possible wear
guns = [[],
        ['AK-47',{'Aquamarine Revenge':qual, 'Black Laminate':qual, 'Blue Laminate':qual[1:5], 'Cartel':qual, 'Case Hardened':qual, 'Elite Build':qual, 'Emerald Pinstripe':qual, 'Fire Serpent':qual[0:4], 'First Class':qual, 'Frontside Misty':qual, 'Fuel Injector':qual, 'Hydroponic':qual, 'Jaguar':qual, 'Jet Set':qual, 'Jungle Spray':qual, 'Neon Revolution':qual, 'Point Disarray':qual, 'Predator':qual, 'Red Laminate':qual, 'Redline':qual[0:4], 'Safari Mesh':qual, 'Vulcan':qual, 'Wasteland Rebel':qual}],
        ['AUG',{'Akihabara Accept':qual[0:4], 'Anodized Navy':qual[3:5], 'Aristocrat':qual, 'Bengal Tiger':qual, 'Chameleon':qual, 'Colony':qual, 'Condemned':qual, 'Contractor':qual, 'Copperhead':qual[2:4], 'Daedalus':qual, 'Fleet Flock':qual, 'Hot Rod':qual[3:5], 'Radiation Hazard':qual, 'Ricochet':qual, 'Storm':qual, 'Syd Mead':qual, 'Torque':qual, 'Wings':qual[3:5]}],
        ['AWP',{'Asiimov':qual[0:3], 'BOOM':qual[2:5], 'Corticera':qual[2:5], 'Electric Hive':qual[1:5], 'Elite Build':qual, 'Graphite':qual[3:5], 'Hyper Beast':qual, 'Lightning Strike':qual[3:5], 'Man-o\'-war':qual[2:4], 'Phobos':qual[1:5], 'Pink DDPAAT':qual, 'Pit Viper':qual[0:4], 'Redline':qual[1:4], 'Safari Mesh':qual, 'Snake Camo':qual, 'Sun in Leo':qual, 'Worm God':qual[1:5]}],
        ['CZ75-Auto',{'Army Sheen':qual[2:5], 'Chalice':qual[3:5], 'Crimson Web':qual, 'Emerald':qual[3:5], 'Green Plaid':qual, 'Hexane':qual[1:5], 'Imprint':qual, 'Nitro':qual, 'Poison Dart':qual, 'Pole Position':qual, 'Red Astor':qual, 'The Fuschia Is Now':qual[1:5], 'Tigris':qual, 'Tread Plate':qual[2:5], 'Tuxedo':qual, 'Twist':qual, 'Victoria':qual, 'Yellow Jacket':qual}],
        ['Desert Eagle',{'Blaze':qual[3:5], 'Bronze Deco':qual, 'Cobalt Disruption':qual[2:5], 'Conspiracy':qual[2:5], 'Corinthian':qual[1:5], 'Crimson Web':qual, 'Directive':qual, 'Golden Koi':qual[3:5], 'Hand Cannon':qual, 'Heirloom':qual, 'Hypnotic':qual[3:5], 'Kumicho Dragon':qual, 'Meteorite':qual[2:5], 'Midnight Storm':qual, 'Mudder':qual, 'Naga':qual, 'Night':qual, 'Pilot':qual, 'Sunset Storm 壱':qual, 'Sunset Storm 弐':qual, 'Urban DDPAT':qual, 'Urban Rubble':qual}],
        ['Dual Berettas',{'Anodized Navy':qual[3:5], 'Black Limba':qual, 'Briar':qual[2:5], 'Cartel':qual, 'Cobalt Quartz':qual[1:5], 'Colony':qual, 'Contractor':qual, 'Demolition':qual[0:3], 'Dualing Dragons':qual, 'Duelist':qual, 'Hemoglobin':qual[2:5], 'Marina':qual, 'Moon in Libra':qual, 'Panther':qual, 'Retribution':qual[1:5], 'Stained':qual, 'Urban Shock':qual, 'Ventilators':qual[1:5]}],
        ['FAMAS',{'Afterimage':qual[1:5], 'Colony':qual, 'Contrast Spray':qual, 'Cyanospatter':qual, 'Djinn':qual, 'Doomkitty':qual[2:4], 'Hexane':qual[1:5], 'Neural Net':qual, 'Pulse':qual[1:5], 'Roll Cage':qual, 'Sergeant':qual[0:4], 'Spitfire':qual, 'Styx':qual, 'Survivor Z':qual, 'Teardown':qual, 'Valence':qual}],
        ['Five-SeveN',{'Anodized Gunmetal':qual[3:5], 'Candy Apple':qual[2:5], 'Case Hardened':qual, 'Contractor':qual, 'Copper Galaxy':qual[2:5], 'Forest Night':qual, 'Fowl Play':qual, 'Hot Shot':qual, 'Jungle':qual, 'Kami':qual[2:5], 'Monkey Business':qual[0:4], 'Neon Kimonno':qual, 'Nightshade':qual, 'Nitro':qual, '}],
        ]

from collections import OrderedDict
from time import sleep
import requests
from bs4 import BeautifulSoup
gunID = int(input('Gun ID:'))
skindex = 0
qualdex = 0
print('http://steamcommunity.com/market/listings/730/'+guns[gunID][0]+'%20%7C%20'+list(guns[gunID][1].keys())[skindex]+'%20%28'+list(guns[gunID][1].values())[skindex][qualdex]+'%29')
page = requests.get('http://steamcommunity.com/market/listings/730/'+guns[0][0]+'%20%7C%20'+list(guns[0][1].keys())[0]+'%20%28'+list(guns[0][1].values())[0][0]+'%29')
print('Getting info from Steam...')
soup = BeautifulSoup(page.content, "lxml")
rawPrices = soup.find_all('span',class_="market_listing_price market_listing_price_with_fee")
prices = [i.text.strip().replace(',','.') for i in rawPrices]
print(prices)
for i in range(len(prices)):
    if 'pуб' in prices[i]:
        prices[i] = prices[i][:-1]
intPrice = [float(k) for k in [''.join([j for j in i if j in '0123456789.']) for i in prices] if k][0]
def convert(s):
    url = requests.get('http://themoneyconverter.com/%s/CAD.aspx' % s)
    url = BeautifulSoup(url.content, "lxml")
    url = url.find_all('div',id="cc-ratebox")
    url = [i.text.replace(',','.').strip() for i in url]
    url = [float(k) for k in [''.join([j for j in i if j in '0123456789.']) for i in url] if k][0]
    return url
def curr(sym,code,i):
    if sym in prices[i]:
        global CADPrice
        CADPrice = intPrice*convert(code)
if prices[0].lower() == 'sold!':
    sleep(0)
def check(i):
    curr('£','GBP',i)
    curr('€','EUR',i)
    curr('CHF','CHF',i)
    curr('pуб','RUB',i)
    curr('R$','BRL',i)
    #curr('¥','JPY')
    curr('kr','SEK',i)
    curr('Rp','IDR',i)
    curr('RM','MYR',i)
    curr('P','PHP',i)
    curr('S$','SGD',i)
    curr('฿','THB',i)
    curr('₩','KRW',i)
    curr('TL','TRY',i)
    curr('Mex$','MXN',i)
    curr('CDN$','CAD',i)
    curr('NZ$','NZD',i)
    #curr('¥','CNY')
    curr('INR','₹',i)
    curr('CLP#','CLP',i)
    curr('S/','PEN',i)
    curr('COL$','COP',i)
    curr('R ','ZAR',i)
    curr('HK$','HKD',i)
    curr('NT$','TWD',i)
    curr('SR','SRD',i)
    curr('AED','AED',i)
check(0)
if '$' in prices[0][0]:
    CADPrice = intPrice*convert('USD')
Round = 0
for i in prices:
    if '¥' in prices[Round]:
        Round += 1
        check(Round)
print(CADPrice)
