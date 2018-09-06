from xml.etree.ElementTree import iterparse


class GetXmlTestsuiteList:
    def ReadSuiteFromXml(self, xmlfile):
        # 逐行解析XML文件，将每行的内容存入list
        suite_list = []
        for (event, node) in iterparse(xmlfile, events=['start']):
            suite_dict = {}
            if node.tag == "testsuite":
                print(node.attrib['name'])
                suite_dict['suite_name'] = node.attrib['name']
                for child in node:
                    if child.tag == "node_order":
                        print(child.text)
                        suite_dict['suite_node_order'] = child.text
                    if child.tag == "details":
                        print(child.text)
                        suite_dict['suite_details'] = str(child.text)
                suite_list.append(suite_dict)
        print(suite_list)
        return suite_list


if __name__ == "__main__":
    GetXmlTestsuiteList().ReadSuiteFromXml('all_testsuites.xml')
