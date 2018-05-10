from admanager.AdManager import *

#import admanager.AdManager

if __name__ == '__main__':

    this_dir = os.path.dirname(__file__)
    resource_path = os.path.join(this_dir, 'resources')

    admanager = AdManager('act_212526696146973', '212501799482796', resource_path)

    # create the first campaign
    admanager.deleteAllCampaigns()
    campaigns = admanager.loadCampaignsFromResources()
    admanager.createCampaign(campaigns[0])
    print "created campaign: " + campaigns[0][Campaign.Field.name]

    # create the adsets with ads
    adsets = []

    # with interests: Sharing, Sharing economy
    adset = admanager.loadAdsetFromJson(os.path.join(resource_path, "adsets", "adset_sharing.json"))
    admanager.createAdSet(adset, campaigns[0].get_id())
    adsets.append(adset)

    image = admanager.createImageFromResources(os.path.join(resource_path, "ads", "images", "matchat_graph_16_9.png"))
    ad = admanager.loadAdFromJson(os.path.join(resource_path, "ads", "ad_matchat.json"))
    admanager.createAd(ad, adset.get_id(), image.get_hash(), "Matchat Sharing Ad")
    print "created adset with ad: " + adset[AdSet.Field.name] + " => " + ad[Ad.Field.name]

    # with interests: Flea market
    adset = admanager.loadAdsetFromJson(os.path.join(resource_path, "adsets", "adset_fleamarket.json"))
    admanager.createAdSet(adset, campaigns[0].get_id())
    adsets.append(adset)

    image = admanager.createImageFromResources(os.path.join(resource_path, "ads", "images", "matchat_graph_16_9.png"))
    ad = admanager.loadAdFromJson(os.path.join(resource_path, "ads", "ad_matchat.json"))
    admanager.createAd(ad, adset.get_id(), image.get_hash(), "Matchat Flea Market Ad")
    print "created adset with ad: " + adset[AdSet.Field.name] + " => " + ad[Ad.Field.name]

    # parents with children up to age 18
    adset = admanager.loadAdsetFromJson(os.path.join(resource_path, "adsets", "adset_parents.json"))
    admanager.createAdSet(adset, campaigns[0].get_id())
    adsets.append(adset)

    image = admanager.createImageFromResources(os.path.join(resource_path, "ads", "images", "matchat_graph_16_9.png"))
    ad = admanager.loadAdFromJson(os.path.join(resource_path, "ads", "ad_matchat.json"))
    admanager.createAd(ad, adset.get_id(), image.get_hash(), "Matchat Parents Ad")
    print "created adset with ad: " + adset[AdSet.Field.name] + " => " + ad[Ad.Field.name]

    # create the split test
    # adsets = admanager.listAllAdsets()
    adstudy = admanager.createSplitTestAdStudy("Matchat Split Test", 1532512562, 1532512563, adsets)
    print "created adstudy for split test: " + adstudy[AdStudy.Field.name]

