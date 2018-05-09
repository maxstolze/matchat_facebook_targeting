from admanager.AdManager import *

#import admanager.AdManager

if __name__ == '__main__':

    # 472518946157433 = Heiko Friedrich Ad Account

    my_account_id = 'act_212526696146973'
    my_business_id = '212501799482796'


    this_dir = os.path.dirname(__file__)
    resource_path = os.path.join(this_dir, 'resources')


    admanager = AdManager('act_212526696146973', '212501799482796', resource_path)

    my_account = AdAccount(fbid=my_account_id) # Ad Account 1
    my_account.remote_read()
    print "account id: " + my_account.get_id_assured()

    # img_path = os.path.join(this_dir, 'resources', 'ads', 'images', 'matchat_graph_16_9.png')
    # print img_path
    # hash = admanager.createImageFromResources(img_path)
    # print hash

    # images = admanager.createAllImagesFromResources()
    # print images

    # campaigns = admanager.listAllCampaigns()
    # print "campaigns: " + str(campaigns)

    # campaigns = admanager.readCampaignsFromResources()
    # print "read campaigns: " + str(campaigns)
    #
    # for c in campaigns:
    #     admanager.createCampaign(c)
    #
    #
    # adsets = admanager.readAdsetsFromResources()
    # print "adsets: " + str(adsets)
    #
    # admanager.createAdSet(adsets[0], c.get_id())

    # campaign = createCampaign(my_account_id)
    # adset1 = createAdSet(my_account_id, campaign.get_id())
    # adset2 = createAdSet(my_account_id, campaign.get_id())
    # createSplitTestAdStudy(my_business_id, adset1.get_id(), adset2.get_id())
    #createAd(my_account_id, '23842999065780500', '135003680685668')
    #
    adsets = admanager.listAllAdsets()
    print "adsets: " + str(adsets)
    #
    # adsets = admanager.listAllAds()
    # print "ads: " + str(adsets)


    # campaigns = admanager.listAllCampaigns()
    # print "campaigns: " + str(campaigns)
    #
    # admanager.deleteAllCampaigns()

    # campaigns = admanager.listAllCampaigns()
    # print "campaigns: " + str(campaigns)

    # campaign = readCampaign('23842983211330500')
    # print "campaign: " + campaign[Campaign.Field.name]

    ads = admanager.loadAdsFromResources()
    print "read ads: " + str(ads)

    # admanager.createAd(ads[0], adsets[0].get_id())

    images = admanager.createAllImagesFromResources()
    admanager.createAd(ads[0], adsets[0].get_id(), images[0].get_hash())

    ads = admanager.listAllAds()
    print "ads: " + str(ads)

    #adstudy = admanager.createSplitTestAdStudy("SplitTest1", 1532512562, 1532512563, adsets)
