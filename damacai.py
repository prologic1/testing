from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options
import json
import csv
#from tqdm import tqdm                  #progress bar to track remaining time

import time
start = time.time()
#=======================================================================================================================
#Simplified Headless Mode
#"""
opts= Options()
opts.set_headless()
assert opts.headless  # operating in headless mode
driver = webdriver.Firefox(options=opts)
#"""
#-----------------------------------------------------------------------------------------------------------------------
#comment/uncomment the following line to enable/disable headless mode for debugging purposes
#driver = webdriver.Firefox()
#=======================================================================================================================
resultList = []

driver.get("https://www.4dmoon.com/")

RESULTS_LOCATOR = "//tr/td/div"
# wait for 10 secs to enable results to be displayed
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))

page1_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)

for item in page1_results:
        resultList.append(item.text)
        print(item.text)

#DAMACAI 1+3D
firstprize = (str(resultList[0].splitlines()))[2:6];
secondprize = (str(resultList[1].splitlines()))[2:6];
thirdprize = (str(resultList[2].splitlines()))[2:6];

special1= (str(resultList[3].splitlines()))[2:6];
special2= (str(resultList[4].splitlines()))[2:6];
special3= (str(resultList[5].splitlines()))[2:6];
special4= (str(resultList[6].splitlines()))[2:6];
special5= (str(resultList[7].splitlines()))[2:6];
special6= (str(resultList[8].splitlines()))[2:6];
special7= (str(resultList[9].splitlines()))[2:6];
special8= (str(resultList[10].splitlines()))[2:6];
special9= (str(resultList[11].splitlines()))[2:6];
special10= (str(resultList[12].splitlines()))[2:6];

con1= (str(resultList[13].splitlines()))[2:6];
con2= (str(resultList[14].splitlines()))[2:6];
con3= (str(resultList[15].splitlines()))[2:6];
con4= (str(resultList[16].splitlines()))[2:6];
con5= (str(resultList[17].splitlines()))[2:6];
con6= (str(resultList[18].splitlines()))[2:6];
con7= (str(resultList[19].splitlines()))[2:6];
con8= (str(resultList[20].splitlines()))[2:6];
con9= (str(resultList[21].splitlines()))[2:6];
con10= (str(resultList[22].splitlines()))[2:6];
print("===============================================================================================================")
#DAMACAI 3+3D
firstprize_3PL = (str(resultList[119].splitlines()))[2:8];
secondprize_3PL = (str(resultList[120].splitlines()))[2:8];
thirdprize_3PL = (str(resultList[121].splitlines()))[2:8];

special1_3PL= (str(resultList[125].splitlines()))[2:8];
special2_3PL= (str(resultList[126].splitlines()))[2:8];
special3_3PL= (str(resultList[127].splitlines()))[2:8];
special4_3PL= (str(resultList[128].splitlines()))[2:8];
special5_3PL= (str(resultList[129].splitlines()))[2:8];
special6_3PL= (str(resultList[130].splitlines()))[2:8];
special7_3PL= (str(resultList[131].splitlines()))[2:8];
special8_3PL= (str(resultList[132].splitlines()))[2:8];
special9_3PL= (str(resultList[134].splitlines()))[2:8];
special10_3PL= (str(resultList[135].splitlines()))[2:8];

con1_3PL= (str(resultList[137].splitlines()))[2:8];
con2_3PL= (str(resultList[138].splitlines()))[2:8];
con3_3PL= (str(resultList[139].splitlines()))[2:8];
con4_3PL= (str(resultList[140].splitlines()))[2:8];
con5_3PL= (str(resultList[141].splitlines()))[2:8];
con6_3PL= (str(resultList[142].splitlines()))[2:8];
con7_3PL= (str(resultList[143].splitlines()))[2:8];
con8_3PL= (str(resultList[144].splitlines()))[2:8];
con9_3PL= (str(resultList[146].splitlines()))[2:8];
con10_3PL= (str(resultList[147].splitlines()))[2:8];

print("===============================================================================================================")
#MAGNUM 4D
firstprize_magnum4D = (str(resultList[25].splitlines()))[2:6];
secondprize_magnum4D = (str(resultList[26].splitlines()))[2:6];
thirdprize_magnum4D = (str(resultList[27].splitlines()))[2:6];

special1_magnum4D= (str(resultList[28].splitlines()))[2:6];
special2_magnum4D= (str(resultList[29].splitlines()))[2:6];
special3_magnum4D= (str(resultList[30].splitlines()))[2:6];
special4_magnum4D= (str(resultList[31].splitlines()))[2:6];
special5_magnum4D= (str(resultList[32].splitlines()))[2:6];
special6_magnum4D= (str(resultList[33].splitlines()))[2:6];
special7_magnum4D= (str(resultList[34].splitlines()))[2:6];
special8_magnum4D= (str(resultList[35].splitlines()))[2:6];
special9_magnum4D= (str(resultList[36].splitlines()))[2:6];
special10_magnum4D= (str(resultList[37].splitlines()))[2:6];
special11_magnum4D= (str(resultList[38].splitlines()))[2:6];
special12_magnum4D= (str(resultList[39].splitlines()))[2:6];
special13_magnum4D= (str(resultList[40].splitlines()))[2:6];

con1_magnum4D= (str(resultList[41].splitlines()))[2:6];
con2_magnum4D= (str(resultList[42].splitlines()))[2:6];
con3_magnum4D= (str(resultList[43].splitlines()))[2:6];
con4_magnum4D= (str(resultList[44].splitlines()))[2:6];
con5_magnum4D= (str(resultList[45].splitlines()))[2:6];
con6_magnum4D= (str(resultList[46].splitlines()))[2:6];
con7_magnum4D= (str(resultList[47].splitlines()))[2:6];
con8_magnum4D= (str(resultList[48].splitlines()))[2:6];
con9_magnum4D= (str(resultList[49].splitlines()))[2:6];
con10_magnum4D= (str(resultList[50].splitlines()))[2:6];

print("===============================================================================================================")
#SPORTS TOTO 4D
firstprize_sports4D = (str(resultList[53].splitlines()))[2:6];
secondprize_sports4D = (str(resultList[54].splitlines()))[2:6];
thirdprize_sports4D = (str(resultList[55].splitlines()))[2:6];

special1_sports4D= (str(resultList[56].splitlines()))[2:6];
special2_sports4D= (str(resultList[57].splitlines()))[2:6];
special3_sports4D= (str(resultList[58].splitlines()))[2:6];
special4_sports4D= (str(resultList[59].splitlines()))[2:6];
special5_sports4D= (str(resultList[60].splitlines()))[2:6];
special6_sports4D= (str(resultList[61].splitlines()))[2:6];
special7_sports4D= (str(resultList[62].splitlines()))[2:6];
special8_sports4D= (str(resultList[63].splitlines()))[2:6];
special9_sports4D= (str(resultList[64].splitlines()))[2:6];
special10_sports4D= (str(resultList[65].splitlines()))[2:6];
special11_sports4D= (str(resultList[66].splitlines()))[2:6];
special12_sports4D= (str(resultList[67].splitlines()))[2:6];
special13_sports4D= (str(resultList[68].splitlines()))[2:6];

con1_sports4D= (str(resultList[69].splitlines()))[2:6];
con2_sports4D= (str(resultList[70].splitlines()))[2:6];
con3_sports4D= (str(resultList[71].splitlines()))[2:6];
con4_sports4D= (str(resultList[72].splitlines()))[2:6];
con5_sports4D= (str(resultList[73].splitlines()))[2:6];
con6_sports4D= (str(resultList[74].splitlines()))[2:6];
con7_sports4D= (str(resultList[75].splitlines()))[2:6];
con8_sports4D= (str(resultList[76].splitlines()))[2:6];
con9_sports4D= (str(resultList[77].splitlines()))[2:6];
con10_sports4D= (str(resultList[78].splitlines()))[2:6];

print("===============================================================================================================")
#SPORTS TOTO 5D
firstprize_sports5D = (str(resultList[81].splitlines()))[2:8];
fourthprize_sports5D = (str(resultList[82].splitlines()))[2:6];
secondprize_sports5D = (str(resultList[83].splitlines()))[2:8];
fifthprize_sports5D = (str(resultList[84].splitlines()))[2:5];
thirdprize_sports5D = (str(resultList[85].splitlines()))[2:8];
sixthprize_sports5D = (str(resultList[86].splitlines()))[2:4];

#SPORTS TOTO 6D
firstprize_sports6D = (str(resultList[87].splitlines()))[2:8];
secondprize1_sports6D = (str(resultList[88].splitlines()))[2:7];
secondprize2_sports6D = (str(resultList[89].splitlines()))[2:7];
thirdprize1_sports6D = (str(resultList[90].splitlines()))[2:6];
thirdprize2_sports6D = (str(resultList[91].splitlines()))[2:6];
fourthprize1_sports6D = (str(resultList[92].splitlines()))[2:5];
fourthprize2_sports6D = (str(resultList[93].splitlines()))[2:5];
fifthprize1_sports6D = (str(resultList[94].splitlines()))[2:4];
fifthprize2_sports6D = (str(resultList[95].splitlines()))[2:4];

#driver.close()
#quit()


print("***************************************************************************************************************")
print("RETRIEVING EAST MALAYSIA VALUES.......")
resultList = []

driver.get("https://www.4dmoon.com/sabah-sarawak-4d-results/")

RESULTS_LOCATOR = "//tr/td/div"
# wait for 10 secs to enable results to be displayed
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))

page1_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)

for item in page1_results:
        resultList.append(item.text)
        #print(item.text)

#SANDAKAN 4D
firstprize_san4D = (str(resultList[0].splitlines()))[2:6];
secondprize_san4D = (str(resultList[1].splitlines()))[2:6];
thirdprize_san4D = (str(resultList[2].splitlines()))[2:6];

special1_san4D= (str(resultList[3].splitlines()))[2:6];
special2_san4D= (str(resultList[4].splitlines()))[2:6];
special3_san4D= (str(resultList[5].splitlines()))[2:6];
special4_san4D= (str(resultList[6].splitlines()))[2:6];
special5_san4D= (str(resultList[7].splitlines()))[2:6];
special6_san4D= (str(resultList[8].splitlines()))[2:6];
special7_san4D= (str(resultList[9].splitlines()))[2:6];
special8_san4D= (str(resultList[10].splitlines()))[2:6];
special9_san4D= (str(resultList[11].splitlines()))[2:6];
special10_san4D= (str(resultList[12].splitlines()))[2:6];
special11_san4D= (str(resultList[13].splitlines()))[2:6];
special12_san4D= (str(resultList[14].splitlines()))[2:6];
special13_san4D= (str(resultList[15].splitlines()))[2:6];

con1_san4D= (str(resultList[16].splitlines()))[2:6];
con2_san4D= (str(resultList[17].splitlines()))[2:6];
con3_san4D= (str(resultList[18].splitlines()))[2:6];
con4_san4D= (str(resultList[19].splitlines()))[2:6];
con5_san4D= (str(resultList[20].splitlines()))[2:6];
con6_san4D= (str(resultList[21].splitlines()))[2:6];
con7_san4D= (str(resultList[22].splitlines()))[2:6];
con8_san4D= (str(resultList[23].splitlines()))[2:6];
con9_san4D= (str(resultList[24].splitlines()))[2:6];
con10_san4D= (str(resultList[25].splitlines()))[2:6];
print("===============================================================================================================")
#SABAH 3D
firstprize_sabah3D = (str(resultList[26].splitlines()))[2:5];
secondprize_sabah3D = (str(resultList[27].splitlines()))[2:5];
thirdprize_sabah3D = (str(resultList[28].splitlines()))[2:5];
print("===============================================================================================================")
#SABAH 4D
firstprize_sabah4D = (str(resultList[29].splitlines()))[2:6];
secondprize_sabah4D = (str(resultList[30].splitlines()))[2:6];
thirdprize_sabah4D = (str(resultList[31].splitlines()))[2:6];

special1_sabah4D= (str(resultList[32].splitlines()))[2:6];
special2_sabah4D= (str(resultList[33].splitlines()))[2:6];
special3_sabah4D= (str(resultList[34].splitlines()))[2:6];
special4_sabah4D= (str(resultList[35].splitlines()))[2:6];
special5_sabah4D= (str(resultList[36].splitlines()))[2:6];
special6_sabah4D= (str(resultList[37].splitlines()))[2:6];
special7_sabah4D= (str(resultList[38].splitlines()))[2:6];
special8_sabah4D= (str(resultList[39].splitlines()))[2:6];
special9_sabah4D= (str(resultList[40].splitlines()))[2:6];
special10_sabah4D= (str(resultList[41].splitlines()))[2:6];
special11_sabah4D= (str(resultList[42].splitlines()))[2:6];
special12_sabah4D= (str(resultList[43].splitlines()))[2:6];
special13_sabah4D= (str(resultList[44].splitlines()))[2:6];

con1_sabah4D= (str(resultList[45].splitlines()))[2:6];
con2_sabah4D= (str(resultList[46].splitlines()))[2:6];
con3_sabah4D= (str(resultList[47].splitlines()))[2:6];
con4_sabah4D= (str(resultList[48].splitlines()))[2:6];
con5_sabah4D= (str(resultList[49].splitlines()))[2:6];
con6_sabah4D= (str(resultList[50].splitlines()))[2:6];
con7_sabah4D= (str(resultList[51].splitlines()))[2:6];
con8_sabah4D= (str(resultList[52].splitlines()))[2:6];
con9_sabah4D= (str(resultList[53].splitlines()))[2:6];
con10_sabah4D= (str(resultList[54].splitlines()))[2:6];
print("===============================================================================================================")
#SARAWAK CASHSWEEP
firstprize_sar = (str(resultList[64].splitlines()))[2:6];
secondprize_sar = (str(resultList[65].splitlines()))[2:6];
thirdprize_sar = (str(resultList[66].splitlines()))[2:6];

special1_sar= (str(resultList[67].splitlines()))[2:6];
special2_sar= (str(resultList[68].splitlines()))[2:6];
special3_sar= (str(resultList[69].splitlines()))[2:6];
special4_sar= (str(resultList[70].splitlines()))[2:6];
special5_sar= (str(resultList[71].splitlines()))[2:6];
special6_sar= (str(resultList[72].splitlines()))[2:6];
special7_sar= (str(resultList[73].splitlines()))[2:6];
special8_sar= (str(resultList[74].splitlines()))[2:6];
special9_sar= (str(resultList[75].splitlines()))[2:6];
special10_sar= (str(resultList[76].splitlines()))[2:6];

con1_sar= (str(resultList[77].splitlines()))[2:6];
con2_sar= (str(resultList[78].splitlines()))[2:6];
con3_sar= (str(resultList[79].splitlines()))[2:6];
con4_sar= (str(resultList[80].splitlines()))[2:6];
con5_sar= (str(resultList[81].splitlines()))[2:6];
con6_sar= (str(resultList[82].splitlines()))[2:6];
con7_sar= (str(resultList[83].splitlines()))[2:6];
con8_sar= (str(resultList[84].splitlines()))[2:6];
con9_sar= (str(resultList[85].splitlines()))[2:6];
con10_sar= (str(resultList[86].splitlines()))[2:6];


print("===============================================================================================================")
#APPEND TO JSON
line_items=[]

myjson3 = [
  {
    "damacai1_3d": [
      {
        "firstprize": firstprize,
        "secondprize": secondprize,
        "thirdprize": thirdprize

      },
      {
        "special1": special1,
        "special2": special2,
        "special3": special3,
        "special4": special4,
        "special5": special5,
        "special6": special6,
        "special7": special7,
        "special8": special8,
        "special9": special9,
        "special10": special10

      },
      {
        "con1": con1,
        "con2": con2,
        "con3": con3,
        "con4": con4,
        "con5": con5,
        "con6": con6,
        "con7": con7,
        "con8": con8,
        "con9": con9,
        "con10": con10
      }
    ]
  },
  {
    "damacai3_3d": [
      {
        "firstprize": firstprize_3PL,
        "secondprize": secondprize_3PL,
        "thirdprize": thirdprize_3PL
      },
      {
        "special1": special1_3PL,
        "special2": special2_3PL,
        "special3": special3_3PL,
        "special4": special4_3PL,
        "special5": special5_3PL,
        "special6": special6_3PL,
        "special7": special7_3PL,
        "special8": special8_3PL,
        "special9": special9_3PL,
        "special10": special10_3PL

      },
      {
        "con1": con1_3PL,
        "con2": con2_3PL,
        "con3": con3_3PL,
        "con4": con4_3PL,
        "con5": con5_3PL,
        "con6": con6_3PL,
        "con7": con7_3PL,
        "con8": con8_3PL,
        "con9": con9_3PL,
        "con10": con10_3PL
      }
    ]
  },
  {
    "magnum4d": [
      {
        "firstprize": firstprize_magnum4D,
        "secondprize": secondprize_magnum4D,
        "thirdprize": thirdprize_magnum4D
      },
      {
        "special1": special1_magnum4D,
        "special2": special2_magnum4D,
        "special3": special3_magnum4D,
        "special4": special4_magnum4D,
        "special5": special5_magnum4D,
        "special6": special6_magnum4D,
        "special7": special7_magnum4D,
        "special8": special8_magnum4D,
        "special9": special9_magnum4D,
        "special10": special10_magnum4D,
        "special11": special11_magnum4D,
        "special12": special12_magnum4D,
        "special13": special13_magnum4D
      },
      {
        "con1": con1_magnum4D,
        "con2": con2_magnum4D,
        "con3": con3_magnum4D,
        "con4": con4_magnum4D,
        "con5": con5_magnum4D,
        "con6": con6_magnum4D,
        "con7": con7_magnum4D,
        "con8": con8_magnum4D,
        "con9": con9_magnum4D,
        "con10": con10_magnum4D
      }
    ]
  },
  {
    "sports4d": [
      {
        "firstprize": firstprize_sports4D,
        "secondprize": secondprize_sports4D,
        "thirdprize": thirdprize_sports4D
      },
      {
        "special1": special1_sports4D,
        "special2": special2_sports4D,
        "special3": special3_sports4D,
        "special4": special4_sports4D,
        "special5": special5_sports4D,
        "special6": special6_sports4D,
        "special7": special7_sports4D,
        "special8": special8_sports4D,
        "special9": special9_sports4D,
        "special10": special10_sports4D,
        "special11": special11_sports4D,
        "special12": special12_sports4D,
        "special13": special13_sports4D
      },
      {
        "con1": con1_sports4D,
        "con2": con2_sports4D,
        "con3": con3_sports4D,
        "con4": con4_sports4D,
        "con5": con5_sports4D,
        "con6": con6_sports4D,
        "con7": con7_sports4D,
        "con8": con8_sports4D,
        "con9": con9_sports4D,
        "con10": con10_sports4D
      }
    ]
  },
  {
    "sports5d": [
      {
        "firstprize": firstprize_sports5D,
        "secondprize": secondprize_sports5D,
        "thirdprize": thirdprize_sports5D,
        "fourthprize": fourthprize_sports5D,
        "fifthprize": fifthprize_sports5D,
        "sixthprize": sixthprize_sports5D
      }

    ]
  },
  {
    "sports6d": [
      {
        "firstprize": firstprize_sports6D,
        "secondprize1": secondprize1_sports6D,
        "secondprize2": secondprize2_sports6D,
        "thirdprize1": thirdprize1_sports6D,
        "thirdprize2": thirdprize2_sports6D,
        "fourthprize1": fourthprize1_sports6D,
        "fourthprize2": fourthprize2_sports6D,
        "fifthprize1": fifthprize1_sports6D,
        "fifthprize2": fifthprize2_sports6D
      }

    ]
  },
  {
    "san4d": [
      {
        "firstprize": firstprize_san4D,
        "secondprize": secondprize_san4D,
        "thirdprize": thirdprize_san4D
      },
      {
        "special1": special1_san4D,
        "special2": special2_san4D,
        "special3": special3_san4D,
        "special4": special4_san4D,
        "special5": special5_san4D,
        "special6": special6_san4D,
        "special7": special7_san4D,
        "special8": special8_san4D,
        "special9": special9_san4D,
        "special10": special10_san4D,
        "special11": special11_san4D,
        "special12": special12_san4D,
        "special13": special13_san4D
      },
      {
        "con1": con1_san4D,
        "con2": con2_san4D,
        "con3": con3_san4D,
        "con4": con4_san4D,
        "con5": con5_san4D,
        "con6": con6_san4D,
        "con7": con7_san4D,
        "con8": con8_san4D,
        "con9": con9_san4D,
        "con10": con10_san4D
      }
    ]
  },
  {
    "sabah3d": [
      {
        "firstprize": firstprize_sabah3D,
        "secondprize": secondprize_sabah3D,
        "thirdprize": thirdprize_sabah3D
      }

    ]
  },
  {
    "sabah4d": [
      {
        "firstprize": firstprize_sabah4D,
        "secondprize": secondprize_sabah4D,
        "thirdprize": thirdprize_sabah4D
      },
      {
        "special1": special1_sabah4D,
        "special2": special2_sabah4D,
        "special3": special3_sabah4D,
        "special4": special4_sabah4D,
        "special5": special5_sabah4D,
        "special6": special6_sabah4D,
        "special7": special7_sabah4D,
        "special8": special8_sabah4D,
        "special9": special9_sabah4D,
        "special10": special10_sabah4D,
        "special11": special11_sabah4D,
        "special12": special12_sabah4D,
        "special13": special13_sabah4D
      },
      {
        "con1": con1_sabah4D,
        "con2": con2_sabah4D,
        "con3": con3_sabah4D,
        "con4": con4_sabah4D,
        "con5": con5_sabah4D,
        "con6": con6_sabah4D,
        "con7": con7_sabah4D,
        "con8": con8_sabah4D,
        "con9": con9_sabah4D,
        "con10": con10_sabah4D
      }
    ]
  },
{
    "sarawak": [
      {
        "firstprize": firstprize_sar,
        "secondprize": secondprize_sar,
        "thirdprize": thirdprize_sar
      },
      {
        "special1": special1_sar,
        "special2": special2_sar,
        "special3": special3_sar,
        "special4": special4_sar,
        "special5": special5_sar,
        "special6": special6_sar,
        "special7": special7_sar,
        "special8": special8_sar,
        "special9": special9_sar,
        "special10": special10_sar
      },
      {
        "con1": con1_sar,
        "con2": con2_sar,
        "con3": con3_sar,
        "con4": con4_sar,
        "con5": con5_sar,
        "con6": con6_sar,
        "con7": con7_sar,
        "con8": con8_sar,
        "con9": con9_sar,
        "con10": con10_sar
      }
    ]
  }
]


line_items.append(myjson3)

with open('plogictoto.json', 'w') as outfile:
    json.dump(line_items, outfile)
print(json.dumps(line_items))





#TO CHECK ACCURACY OF RESULTS
#print(con10)
print("firstprize: "+firstprize_magnum4D)
print("special1: "+special1_magnum4D)
print("con1: "+con1_magnum4D)

print("firstprize: "+firstprize_3PL)
print("special1: "+special1_3PL)
print("con1: "+con1_3PL)

print("firstprize_sports4d: "+firstprize_sports4D)
print("special1_sports4d: "+special1_sports4D)
print("con1_sports4d: "+con1_sports4D)
print("***************************************************************************************************************")
print("5th price 5D:    "+fifthprize_sports5D)
print("6th price 5D:    "+sixthprize_sports5D)

print("5th price 6D (1st choice):    "+fifthprize1_sports6D)
print("5th price 6D (2nd choice):    "+fifthprize2_sports6D)
print("***************************************************************************************************************")
print("1st price sandakan:    "+firstprize_san4D)
print("consolation sandakan:    "+con1_san4D)


#=======================================================================================================================
""""
#Save Results as CSV

w = csv.writer(open("devList.csv","w", newline=''))      #"w" indicates that you're writing strings to the file

#Loop over multiple lists at the same time
for results, urls in zip(resultList, urlList):
    w.writerow([results, urls])
#"""

#=======================================================================================================================
end = time.time()
print("Execution time: "+ str(end - start))
driver.close()
quit()


""""
start = time.time()
XXX
end = time.time()
print(end - start)
"""