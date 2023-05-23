#py -3 -m pip install pyzipper
#py -3 -m pip install openpyxl
#py -3 -m pip install shutil
#py -3 -m pip install tqdm
import pyzipper
import random as rn
import os
import sys
import string
from openpyxl import load_workbook
from datetime import datetime
import shutil
from tqdm import tqdm
print("Zcryption Made by Máté Jakus")
print("Version: 1.0.1")
print("")
loc_f = ""
try:
    with open(".\\save.txt","r",encoding="utf-8") as f:
        loc_f = f.readlines()[0]
except:
    pass
if (loc_f == "" or loc_f == None):
    loc = input("Set TEMP folder (....\\TEMP\\): ")
    with open(".\\save.txt", "w", encoding="utf-8") as f:
        f.write(loc)
    loc_f = loc
PATH = f"{loc_f}list.xlsx"
try:
    wb = load_workbook(PATH,data_only=True)
except:
    print("Please make sure that you have accurately specified the path to the 'list.xlsx' file. Error(01) List.xlsx doesn't exist!")
    print(f"{PATH}")
    inp = input("")
    exit()
page = wb["Munka1"]
SEED = ""
folder = r'.\\'
unw = ["Zcryption.exe","TEMP","main.py","list.txt","venv",".idea",".git","save.txt","zipped.py"]
files = []
fnum = 0
for row in page["A2":"A100000"]:
    for cell in row:
        if (cell.value != None):
            fnum += 1
for i in range(fnum):
    files.append((page[f"A{i+2}"].value,page[f"B{i+2}"].value,page[f"C{i+2}"].value))
#print(files)
def create_password_protected_zip(zip_name, file_path, password):
    with pyzipper.AESZipFile(zip_name, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password.encode('utf-8'))
        zipf.write(file_path)
def extract_password_protected_zip(zip_name, output_dir, password):
    with pyzipper.AESZipFile(zip_name, 'r') as zipf:
        zipf.setpassword(password.encode('utf-8'))
        zipf.extractall(output_dir)
def ra(fnum):
    fnum += 1
    for fn in tqdm(os.listdir(folder)):
        if (fn not in unw):
            print(f" << - >> {fn}")
            s = folder + fn
            ty = ""
            xxed = False
            fname = ""
            for i in range(len(fn)):
                if(fn[i] == "."):
                    ty = fn[i+1:]
                    fname = fn[:i]
                    break
            if (ty == ""):
                shutil.make_archive(fn,"zip",s)
                shutil.rmtree(s)
                ty = "zip"
                fname = fn
                fn = f"{fn}.zip"
                s = folder + fn
                xxed = True
            ind = False
            for n in files:
                if (n[1] == fname or n[0] == fname):
                    ind = True
                    break
            if not (ind):
                fnum+=1
                page[f"A{fnum}"].value = fname
                if (xxed == True and ty == "zip"):
                    page[f"E{fnum}"].value = "x"
                deso = ""
                for d in range(25):
                    rd = rn.randint(0, 1)
                    if (rd == 0):
                        deso += rn.choice(string.ascii_letters)
                    else:
                        deso += str(rn.randint(0, 9))
                page[f"B{fnum}"].value = deso
                pswd = ""
                for d in range(25):
                    rd = rn.randint(0, 1)
                    if (rd == 0):
                        pswd += rn.choice(string.ascii_letters)
                    else:
                        pswd += str(rn.randint(0, 9))
                page[f"C{fnum}"].value = pswd
                #print(en(lines,SEED,s))
                des = folder + deso + ".zip"
                create_password_protected_zip(des, s, pswd)
                os.remove(s)
                #os.rename(s,des)
                now = datetime.now()
                today = datetime.today()
                page[f"D{fnum}"].value = f"{fn} = {des}  || {today}"
                #out.write(f"{fn} = {des}  || {today} \n")
            else:
                ind = 2
                for f in files:
                    if (f[1] == fname or f[0] == fname):
                        break
                    else:
                        ind += 1
                if (fname == files[ind-2][0]):
                    SeEd = page[f"C{ind}"].value
                    deso = page[f"B{ind}"].value
                    des = folder + deso + ".zip"
                    create_password_protected_zip(des, s, SeEd)
                    os.remove(s)
                else:
                    pass
                    #print("no")
        wb.save(PATH)
def de_ra():
    for fn in tqdm(os.listdir(folder)):
        if (fn not in unw):
            print(f" << - >> {fn}")
            s = folder + fn
            ty = ""
            fname = ""
            for i in range(len(fn)):
                if(fn[i] == "."):
                    ty = fn[i+1:]
                    fname = fn[:i]
                    break
            wi = 2
            ind = False
            for n in files:
                if (n[1] == fname):
                    ind = True
                    break
                else:
                    wi += 1
            if (ind):
                des = folder + page[f"A{wi}"].value + ".zip"
                extract_password_protected_zip(s, folder, page[f"C{wi}"].value)
                if (page[f"E{wi}"].value == "x"):
                    shutil.unpack_archive(des,page[f"A{wi}"].value)
                    os.remove(des)
                #os.rename(s,des)
                #if (ty == "zip"):
                #    shutil.unpack_archive(des, page[f"A{wi}"].value)
                os.remove(s)
def delete():
    for i in range(fnum):
        page[f"A{i+2}"].value = None
        page[f"B{i+2}"].value = None
        page[f"C{i+2}"].value = None
        page[f"D{i+2}"].value = None
        page[f"E{i+2}"].value = None
cmd = input("Encode (e) | Decode (d) | Delete All Data (delete): ")
if (cmd == "e"):
    ra(fnum)
elif (cmd == "delete"):
    delete()
else:
    de_ra()
#SEED = en(SEED)
#SEED = "755831824729698482178298983"
#print(SEED)
#de(SEED)
wb.save(PATH)
#create_password_protected_zip('protected_archive.zip', 'hey-ray-6.png', 'password123')
#extract_password_protected_zip('protected_archive.zip', '.\\h\\', 'password123')
