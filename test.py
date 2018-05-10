from admanager.AdManager import *

#import admanager.AdManager

if __name__ == '__main__':

    this_dir = os.path.dirname(__file__)
    resource_path = os.path.join(this_dir, 'resources')

    admanager = AdManager('act_212526696146973', '212501799482796', resource_path)

    # create the first campaign
    #admanager.deleteAllCampaigns()
    campaigns = admanager.loadCampaignsFromResources()
    #admanager.createCampaign(campaigns[0])

    # create the adsets
    # with interests: Sharing, Sharing economy
    #adsets = admanager.loadAdsetsFromResources()
    category_names = ["Sharing", "Sharing economy"]
    targetSearchResults = admanager.searchForTargetingInterests(category_names)
    for i in range(0, len(category_names)):
        print("Potential Reach for keyword '" + str(category_names[i]) + "' is: " + str(targetSearchResults[i]['audience_size']))
    targetingOptions = admanager.createInterestsFromTargetSearchResults(targetSearchResults)
    print targetingOptions
    #admanager.createAdSet(adsets[0], campaigns[0].get_id(), targetingOptions)

    # with interests: Flea market
    #adsets = admanager.loadAdsetsFromResources()
    category_names = ["Flea market"]
    targetSearchResults = admanager.searchForTargetingInterests(category_names)
    for i in range(0, len(category_names)):
        print("Potential Reach for keyword '" + str(category_names[i]) + "' is: " + str(targetSearchResults[i]['audience_size']))
    targetingOptions = admanager.createInterestsFromTargetSearchResults(targetSearchResults)
    print targetingOptions
    #admanager.createAdSet(adsets[0], campaigns[0].get_id(), targetingOptions)

    # parents with children up to age 18
    #adsets = admanager.loadAdsetsFromResources()
    category_names = ["New parents (0-12 months)", "Parents with toddlers (01-02 years)", "Parents with  preschoolers (03-05 years)", "Parents with early school-age children (06-08 years)", "Parents with teenagers (13-18 years)"]
    targetSearchResults = admanager.searchForOtherTargetingCategories(category_names)
    for i in range(0, len(category_names)):
        print("Potential Reach for keyword '" + str(category_names[i]) + "' is: " + str(targetSearchResults[i]['audience_size']))
    targetingOptions = admanager.createInterestsFromTargetSearchResults(targetSearchResults)
    print targetingOptions
    #admanager.createAdSet(adsets[0], campaigns[0].get_id(), targetingOptions)

    #print(targetingOptions)

    # params = {
    #     'q': 'family_statuses',
    #     'type': 'adTargetingCategory',
    # }
    # response = TargetingSearch.search(params)
    # print(response)






    # my_account = AdAccount(fbid=my_account_id) # Ad Account 1
    # my_account.remote_read()
    # print "account id: " + my_account.get_id_assured()

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

    # print "adsets: " + str(adsets)
    #




    # resp2 = admanager.searchForTargetingInterest("Sharing economy")
    # print("targeting response:" + str(resp2))
    #
    # interests = [{
    #     'id': resp1['id'],
    #     'name': resp1['name'],
    # }, {
    #     'id': resp2['id'],
    #     'name': resp2['name'],
    # }]
    #
    # admanager.createAdSet(adsets[0], '23842999336300500', interests)

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

    # ads = admanager.loadAdsFromResources()
    # print "read ads: " + str(ads)
    #
    # # admanager.createAd(ads[0], adsets[0].get_id())
    #
    # images = admanager.createAllImagesFromResources()
    # admanager.createAd(ads[0], adsets[0].get_id(), images[0].get_hash())
    #
    # ads = admanager.listAllAds()
    # print "ads: " + str(ads)

    #adstudy = admanager.createSplitTestAdStudy("SplitTest1", 1532512562, 1532512563, adsets)
