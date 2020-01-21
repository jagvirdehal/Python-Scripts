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
        ['Five-SeveN',{'Anodized Gunmetal':qual[3:5], 'Candy Apple':qual[2:5], 'Case Hardened':qual, 'Contractor':qual, 'Copper Galaxy':qual[2:5], 'Forest Night':qual, 'Fowl Play':qual, 'Hot Shot':qual, 'Jungle':qual, 'Kami':qual[2:5], 'Monkey Business':qual[0:4], 'Neon Kimonno':qual, 'Nightshade':qual, 'Nitro':qual, 'Orange Peel':qual, 'Retrobution':qual, 'Scumbria':qual, 'Silver Quartz':qual[1:5], 'Triumvirate':qual, 'Urban Hazard':qual[2:5], 'Violent Daimyo':qual}],
        ]

Alpha = []
ArmsDeal = []
ArmsDeal2 = []
ArmsDeal3 = []
Assault = []
Aztec = []
Baggage = []
Bank = []
Bravo = []
Breakout = []
Cache = []
ChopShop = []
Chroma = []
Chroma2 = []
Chroma3 = []
Cobblestone = []
Dust = []
Dust2 = []
eSports2013 = []
eSports2013Winter = []
eSports2014Summer = []
Falchion = []
Gamma = []
Gamma2 = []
Glove = []
GodsAndMonsters = []
Huntsman = []
Inferno = []
Italy = []
Lake = []
Militia = []
Mirage = []
Nuke = []
Office = []
Overpass = []
Phoenix = []
Revolver = []
RisingSun = []
Safehouse = []
Shadow = []
Train = []
Vanguard = []
Vertigo = []
Wildfire = []
WinterOffensive = []
Unknown = []

def sorter(c,g,p,i):
    global Alpha, ArmsDeal, ArmsDeal2, ArmsDeal3, Assault, Aztec, Baggage, Bank, Bravo, Breakout, Cache, ChopShop, Chroma, Chroma2, Chroma3, Cobblestone, Dust, Dust2, eSports2013, eSports2013Winter, eSports2014Summer, Falchion, Gamma, Gamma2, Glove, GodsAndMonsters, Huntsman, Inferno, Italy, Lake, Militia, Mirage, Nuke, Office, Overpass, Phoenix, Revolver, RisingSun, Safehouse, Shadown, Train, Vanguard, Vertigo, Wildfire, WinterOffensive, Unknown
    if "The Alpha Collection" in c:
        Alpha.append([g,p,i])
    elif "The Arms Deal Collection" in c:
        ArmsDeal.append([g,p,i])
    elif "The Arms Deal 2 Collection" in c:
        ArmsDeal2.append([g,p,i])
    elif "The Arms Deal 3 Collection" in c:
        ArmsDeal3.append([g,p,i])
    elif "The Assault Collection" in c:
        Assault.append([g,p,i])
    elif "The Aztec Collection" in c:
        Aztec.append([g,p,i])
    elif "The Baggage Collection" in c:
        Baggage.append([g,p,i])
    elif "The Bank Collection" in c:
        Bank.append([g,p,i])
    elif "The Bravo Collection" in c:
        Bravo.append([g,p,i])
    elif "The Breakout Collection" in c:
        Breakout.append([g,p,i])
    elif "The Cache Collection" in c:
        Cache.append([g,p,i])
    elif "The Chop Shop Collection" in c:
        ChopShop.append([g,p,i])
    elif "The Chroma Collection" in c:
        Chroma.append([g,p,i])
    elif "The Chroma 2 Collection" in c:
        Chroma2.append([g,p,i])
    elif "The Chroma 3 Collection" in c:
        Chroma3.append([g,p,i])
    elif "The Cobblestone Collection" in c:
        Cobblestone.append([g,p,i])
    elif "The Dust Collection" in c:
        Dust.append([g,p,i])
    elif "The Dust 2 Collection" in c:
        Dust2.append([g,p,i])
    elif "The eSports 2013 Collection" in c:
        eSports2013.append([g,p,i])
    elif "The eSports 2013 Winter Collection" in c:
        eSports2013Winter.append([g,p,i])
    elif "The eSports 2014 Summer Collection" in c:
        eSports2014Summer.append([g,p,i])
    elif "The Falchion Collection" in c:
        Falchion.append([g,p,i])
    elif "The Gamma Collection" in c:
        Gamma.append([g,p,i])
    elif "The Gamma 2 Collection" in c:
        Gamma2.append([g,p,i])
    elif "The Glove Collection" in c:
        Glove.append([g,p,i])
    elif "The Gods and Monsters Collection" in c:
        GodsAndMonsters.append([g,p,i])
    elif "The Huntsman Collection" in c:
        Huntsman.append([g,p,i])
    elif "The Inferno Collection" in c:
        Inferno.append([g,p,i])
    elif "The Italy Collection" in c:
        Italy.append([g,p,i])
    elif "The Lake Collection" in c:
        Lake.append([g,p,i])
    elif "The Militia Collection" in c:
        Militia.append([g,p,i])
    elif "The Mirage Collection" in c:
        Mirage.append([g,p,i])
    elif "The Nuke Collection" in c:
        Nuke.append([g,p,i])
    elif "The Office Collection" in c:
        Office.append([g,p,i])
    elif "The Overpass Collection" in c:
        Overpass.append([g,p,i])
    elif "The Phoenix Collection" in c:
        Phoenix.append([g,p,i])
    elif "The Revolver Collection" in c:
        Revolver.append([g,p,i])
    elif "The Rising Sun Collection" in c:
        RisingSun.append([g,p,i])
    elif "The Safehouse Collection" in c:
        Safehouse.append([g,p,i])
    elif "The Shadow Collection" in c:
        Shadow.append([g,p,i])
    elif "The Train Collection" in c:
        Train.append([g,p,i])
    elif "The Vanguard Collection" in c:
        Vanguard.append([g,p,i])
    elif "The Vertigo Collection" in c:
        Vertigo.append([g,p,i])
    elif "The Wildfire Collection" in c:
        Wildfire.append([g,p,i])
    elif "The Winter Offensive Collection" in c:
        WinterOffensive.append([g,p,i])
    else:
        Unknown.append([g,p,i])
    
#Import required libraries
from time import sleep
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
#Function to obtain the price of the weapon skins
def GetPrice(gunID,skindex,qualdex,qualname):
    #Link created based upon weapon skin
    link = 'http://steamcommunity.com/market/listings/730/'+guns[gunID][0]+'%20%7C%20'+sorted(list(guns[gunID][1].keys()))[skindex]+'%20%28'+guns[gunID][1][qualname][qualdex]+'%29'
    print(link)
    gunInfo = (guns[gunID][0],sorted(list(guns[gunID][1].keys()))[skindex],guns[gunID][1][qualname][qualdex])
    print(' '.join(gunInfo))
    #Store the webpage as a variable
    #page = requests.get(link)
    page = webdriver.PhantomJS()
    page.get(link)
    soup = BeautifulSoup(page.page_source, "lxml")
    page.quit()
    print('Getting info from Steam...')
    #Check if there is a timeout error
    errorCheck = soup.find_all('div',id="mainContents")
    errorCheck = [i.text.strip() for i in errorCheck]
    #Wait 3 mins if there is a timeout error
    if 'Error' in errorCheck[0]:
        print('Timeout... Waiting for response...')
        sleep(200)
        page = requests.get(link)
        soup = BeautifulSoup(page.content, "lxml")
        
    #Check if there are no listings
    listingCheck = soup.find_all('div',class_="market_listing_table_message")
    listingCheck = [i.text.strip() for i in listingCheck]
    #Get prices
    rawPrices = soup.find_all('span',class_="market_listing_price market_listing_price_with_fee")

    #Get the collection
    collection = soup.find_all('div',class_="descriptor",style="color: rgb(157, 161, 169);")
    collection = [i.text.strip() for i in collection][0]
    print('  ',collection)

    #Get the grade
    grade = soup.find_all('div',id="largeiteminfo_item_type")
    grade = [i.text.strip() for i in grade][0]
    print('  ',grade)
    
    #If there are any listings, get the cheapest price of the weapon skin
    if listingCheck != ['There are no listings for this item.']:
        prices = [i.text.strip() for i in rawPrices]
        #Filter through each price to make sure they are convertable into a float
        for i in range(len(prices)):
            if '¥' in prices[i]:
                prices[i] = prices[i].replace(',','')
            elif 'pуб' in prices[i]:
                prices[i] = prices[i][:-1]
                prices[i] = prices[i].replace(',','.')
            elif 'USD' in prices[i]:
                prices[i] = prices[i].replace(',','.')
            elif 'kr' or '฿' or '₩' in prices[i]:
                prices[i] = prices[i].replace(',','::::')
                prices[i] = prices[i].replace('.',',')
                prices[i] = prices[i].replace('::::','.')
            else:
                prices[i] = prices[i].replace(',','.')
        print(prices)
        #Convert prices into floats
        intPrice = [float(k) for k in [''.join([j for j in i if j in '0123456789.']) for i in prices] if k][0]
        
        #Convert currecies to CAD using exchange rates
        def convert(s):
            url = requests.get('http://themoneyconverter.com/%s/CAD.aspx' % s)
            url = BeautifulSoup(url.content, "lxml")
            url = url.find_all('div',id="cc-ratebox")
            url = [i.text.replace(',','.').strip() for i in url]
            url = [float(k) for k in [''.join([j for j in i if j in '0123456789.']) for i in url] if k][0]
            return url
        
        #Recognize the currency of each price before conversion
        def curr(sym,code,i):
            global CADPrice
            if sym in prices[i]:
                CADPrice = intPrice*convert(code)
                print('    '+str(CADPrice),'\n ',prices[i])
                sorter(collection, grade, CADPrice, gunInfo)
                
        #Go through each possible currency and check if the lowest price is matching
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
            curr('CLP$','CLP',i)
            curr('S/','PEN',i)
            curr('COL$','COP',i)
            curr('R ','ZAR',i)
            curr('HK$','HKD',i)
            curr('NT$','TWD',i)
            curr('SR','SRD',i)
            curr('AED','AED',i)
            curr('USD','USD',i)
        check(0)
##        #Check if the Currency is USD
##        if '$' in prices[0][0]:
##            CADPrice = intPrice*convert('USD')

        #If the currency is in YEN or YUAN, check next lowest currency
        for i in range(len(prices)):
            if '¥' in prices[i] and i < len(prices)-1:
                check(i+1)
            else:
                break
    #If there are no listings, print 'No Listings'
    else:
        print('No Listings')


gunc = int(input('...'))
#Goes through each skin and wear for the selected gun and gets the price
for s in sorted(list(guns[gunc][1].keys())):
    for w in guns[gunc][1][s]:
        GetPrice(gunc,sorted(list(guns[gunc][1])).index(s),guns[gunc][1][s].index(w),s)
