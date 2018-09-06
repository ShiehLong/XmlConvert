import sys

from ConvertFileCore.GetXmlTestcaseList import GetXmlTestcaseList
from ConvertFileCore.WriteDataToExcel import WriteDataToExcel

if __name__ == '__main__':
    path = input("请输入Xml文件路径:")
    if len(path) > 0:
        try:
            caselist = GetXmlTestcaseList().ReadCaseFromXml(path)
            WriteDataToExcel().WriteData(caselist)
        except Exception as e:
            print("有BUG!!!" + str(e))
    else:
        print("请输入文件路径!!!")
