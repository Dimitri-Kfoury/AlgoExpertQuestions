def getLowestCommonManager(topManager, reportOne, reportTwo):
    return findLowest(topManager, reportOne, reportTwo)


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

    def addDirectReports(self, directReports):
        for directReport in directReports:
            self.directReports.append(directReport)


def orgContains(self, item):

    if not self.directReports:
        return False
    elif self == item or self.directReports.__contains__(item):
        return True
    else:
        i = False
        for report in self.directReports:
            i = i or orgContains(report,item)
        return i


def findLowest(Node, reportOne, reportTwo):
    for report in Node.directReports:
        if orgContains(report,reportOne) and orgContains(report,reportTwo):
            return findLowest(report, reportOne, reportTwo)
        else:
            return Node


ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def getOrgCharts():
    orgCharts = {}
    for letter in ALPHABET:
        orgCharts[letter] = OrgChart(letter)
    return orgCharts

