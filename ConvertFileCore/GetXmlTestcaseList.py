import re
from xml.etree.ElementTree import parse


class GetXmlTestcaseList:
    def ReadCaseFromXml(self, xmlfile):
        tree = parse(xmlfile)
        root = tree.getroot()
        # 逐行解析XML文件，将每行的内容存入list
        suite_list = []
        for node in root.getiterator('testsuite'):
            suite_dict = {}
            if node.tag == "testsuite":
                # print(node.attrib['name'])
                suite_dict['suite_name'] = GetXmlTestcaseList().removeInvalidCharacters(str(node.attrib['name']))
                case_list = []
                for child in node:
                    if child.tag == "node_order":
                        # print(child.text)
                        suite_dict['suite_node_order'] = child.text
                        continue
                    if child.tag == "details":
                        # print(child.text)
                        suite_dict['suite_details'] = str(child.text)
                        continue
                    if child.tag == "testcase":
                        case_dict = {}
                        # print(child.attrib['name'])
                        # print(child.attrib['internalid'])
                        case_dict['case_name'] = child.attrib['name']
                        case_dict['case_internalid'] = child.attrib['internalid']
                        for grandChild in child:
                            if grandChild.tag == "node_order":
                                # print(grandChild.text)
                                case_dict['case_node_order'] = grandChild.text
                                continue
                            if grandChild.tag == "externalid":
                                # print(grandChild.text)
                                case_dict['case_externalid'] = grandChild.text
                                continue
                            if grandChild.tag == "summary":
                                # print(str(grandChild.text))
                                case_dict['case_summary'] = GetXmlTestcaseList().removeHtmlTag(str(grandChild.text))
                                continue
                            if grandChild.tag == "steps":
                                # print(str(grandChild.text))
                                case_dict['case_steps'] = GetXmlTestcaseList().removeHtmlTag(str(grandChild.text))
                                continue
                            if grandChild.tag == "expectedresults":
                                # print(str(grandChild.text))
                                case_dict['case_expectedresults'] = GetXmlTestcaseList().removeHtmlTag(
                                    str(grandChild.text))
                                continue
                        case_list.append(case_dict)
                        # print(case_list)
                    suite_dict['testcase'] = case_list
                    # print(suite_dict)
            if len(suite_dict) > 0:
                suite_list.append(suite_dict)
        # print(suite_list)
        return suite_list

    def removeHtmlTag(self, testcase):
        testcase = re.sub(r'<.*?>', "", str(testcase))
        testcase = testcase.replace('\r', "")
        testcase = testcase.replace('&ldquo;', "\"")
        testcase = testcase.replace('&quot;', "\"")
        testcase = testcase.replace('&rdquo;', "\"")
        testcase = testcase.replace('&nbsp;', " ")
        testcase = testcase.replace('&hellip;', "...")
        testcase = testcase.replace('&lt;', "<")
        testcase = testcase.replace('&gt;', ">")
        testcase = testcase.replace('&amp;', "&")
        testcase = testcase.replace('&lsquo;', "【")
        testcase = testcase.replace('&rsquo;', "】")
        testcase = testcase.replace('\ufeff', "")
        return testcase

    def removeInvalidCharacters(self, param):
        invalidCharacters = ['*', ':', '/', '\\', '?', '[', ']']
        for i in range(len(invalidCharacters)):
            param = param.replace(invalidCharacters[i], ' ')
        return param


if __name__ == "__main__":
    GetXmlTestcaseList().ReadCaseFromXml('all_testsuites.xml')
