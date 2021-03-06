import time

import datetime

from admanager.AdManager import *


if __name__ == '__main__':

    this_dir = os.path.dirname(__file__)
    resource_path = os.path.join(this_dir, 'resources')

    admanager = AdManager(resource_path)

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
    reach_estimate = admanager.getPotentialReachForTargeting(adset[AdSet.Field.targeting])
    print "created adset with ad: " + adset[AdSet.Field.name] + " => " + ad[Ad.Field.name] + " with potential reach of " + str(reach_estimate) + " users"
    time.sleep(60)

    # with interests: Flea market
    adset = admanager.loadAdsetFromJson(os.path.join(resource_path, "adsets", "adset_fleamarket.json"))
    admanager.createAdSet(adset, campaigns[0].get_id())
    adsets.append(adset)

    image = admanager.createImageFromResources(os.path.join(resource_path, "ads", "images", "matchat_graph_16_9.png"))
    ad = admanager.loadAdFromJson(os.path.join(resource_path, "ads", "ad_matchat.json"))
    admanager.createAd(ad, adset.get_id(), image.get_hash(), "Matchat Flea Market Ad")
    reach_estimate = admanager.getPotentialReachForTargeting(adset[AdSet.Field.targeting])
    print "created adset with ad: " + adset[AdSet.Field.name] + " => " + ad[Ad.Field.name] + " with potential reach of " + str(reach_estimate) + " users"
    time.sleep(60)

    # parents with children up to age 18
    adset = admanager.loadAdsetFromJson(os.path.join(resource_path, "adsets", "adset_parents.json"))
    admanager.createAdSet(adset, campaigns[0].get_id())
    adsets.append(adset)

    image = admanager.createImageFromResources(os.path.join(resource_path, "ads", "images", "matchat_graph_16_9.png"))
    ad = admanager.loadAdFromJson(os.path.join(resource_path, "ads", "ad_matchat.json"))
    admanager.createAd(ad, adset.get_id(), image.get_hash(), "Matchat Parents Ad")
    reach_estimate = admanager.getPotentialReachForTargeting(adset[AdSet.Field.targeting])
    print "created adset with ad: " + adset[AdSet.Field.name] + " => " + ad[Ad.Field.name] + " with potential reach of " + str(reach_estimate) + " users"

    # create the split test, start it 5 minutes from now and end it a day later
    start_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    end_time = start_time + datetime.timedelta(hours=24)
    adstudy = admanager.createSplitTestAdStudy("Matchat Split Test", start_time, end_time, adsets)
    print "created adstudy for split test: " + adstudy[AdStudy.Field.name]

