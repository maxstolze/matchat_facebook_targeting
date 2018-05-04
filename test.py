from admanager.AdManager import *

#import admanager.AdManager

if __name__ == '__main__':
    initSession()

    # 472518946157433 = Heiko Friedrich Ad Account

    my_account = AdAccount(fbid='act_212526696146973') # Ad Account 1
    my_account.remote_read()
    print "account id: " + my_account.get_id_assured()

    campaigns = listAllCampaigns('act_212526696146973')
    print "campaigns: " + str(campaigns)

    # deleteAllCampaigns('act_212526696146973')
    #
    # campaigns = listAllCampaigns('act_212526696146973')
    # print "campaigns: " + str(campaigns)

    # campaign = readCampaign('23842983211330500')
    # print "campaign: " + campaign[Campaign.Field.name]