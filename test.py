from admanager.AdManager import *

#import admanager.AdManager

if __name__ == '__main__':
    initSession()
    campaign = readCampaign('23842983211330500')
    print "campaign: " + campaign[Campaign.Field.name]