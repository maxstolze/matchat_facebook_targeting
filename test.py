from admanager.AdManager import *

#import admanager.AdManager

if __name__ == '__main__':

    # 472518946157433 = Heiko Friedrich Ad Account

    my_account_id = 'act_212526696146973'
    my_business_id = '212501799482796'

    admanager = AdManager('act_212526696146973', '212501799482796')

    my_account = AdAccount(fbid=my_account_id) # Ad Account 1
    my_account.remote_read()
    print "account id: " + my_account.get_id_assured()

    campaigns = admanager.listAllCampaigns()
    print "campaigns: " + str(campaigns)


    # campaign = createCampaign(my_account_id)
    # adset1 = createAdSet(my_account_id, campaign.get_id())
    # adset2 = createAdSet(my_account_id, campaign.get_id())
    # createSplitTestAdStudy(my_business_id, adset1.get_id(), adset2.get_id())
    #createAd(my_account_id, '23842999065780500', '135003680685668')

    adsets = admanager.listAllAdsets()
    print "adsets: " + str(list(adsets))

    adsets = admanager.listAllAds()
    print "ads: " + str(list(adsets))


    # deleteAllCampaigns('act_212526696146973')
    #
    # campaigns = listAllCampaigns('act_212526696146973')
    # print "campaigns: " + str(campaigns)

    # campaign = readCampaign('23842983211330500')
    # print "campaign: " + campaign[Campaign.Field.name]