from lxml import etree as et

########################################################################################################################
#                                                                                                                      #
########################################################################################################################
class XMLAttribute(object):
    
    ####################################################################################################################
    #                                                                                                                  #
    ####################################################################################################################
    def __init__(self, key, value, type=None):
        self.__key = key
        self.__value = value
        self.__type = type

        self.setValue(value)

    ####################################################################################################################
    #                                                                                                                  #
    ####################################################################################################################
    def getValue(self):
        return self.__value

    ####################################################################################################################
    #                                                                                                                  #
    ####################################################################################################################
    def setValue(self, newVal):
        if self.__type != None:
            try:
                self.__value = self.__type(newVal)
                return True
            except Exception as e:
                print(e)
                return False
        else:
            self.__value = newVal

    ####################################################################################################################
    #                                                                                                                  #
    ####################################################################################################################
    def getKey(self):
        return self.__key

    ####################################################################################################################
    #                                                                                                                  #
    ####################################################################################################################
    def __str__(self):
        return str(self.__value)