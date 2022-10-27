from difflib import SequenceMatcher
def Plagerism_checker(f1, f2):
    with open(f1,errors="ignore") as file1,open(f2,errors="ignore") as file2:
        f1_data=file1.read()
        f2_data=file2.read()
        checking=SequenceMatcher(None, f1_data, f2_data).ratio()
print(f"These files are {checking*100} % similar")
file_1=input("Enter file 1 path: ")
file_2=input("Enter file 2 path: ")
Plagerism_checker(file_1, file_2)