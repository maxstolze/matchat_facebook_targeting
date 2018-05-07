from facebookads import FacebookAdsApi
from facebookads import FacebookSession
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adaccountuser import AdAccountUser
from facebookads.adobjects.adstudy import AdStudy
from facebookads.adobjects.campaign import Campaign
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adset import AdSet
from facebookads import FacebookAdsApi
from facebookads.adobjects.targeting import Targeting
from facebookads import FacebookSession
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative
from facebookads.specs import ObjectStorySpec, LinkData

import json
import os

class AdManager:

    def __init__(self, account_id, business_id, resource_path):
        config_filename = os.path.join(resource_path, 'config.json')
        config_file = open(config_filename)
        config = json.load(config_file)
        config_file.close()

        session = FacebookSession(
            config['app_id'],
            config['app_secret'],
            config['access_token'],
        )
        api = FacebookAdsApi(session)
        FacebookAdsApi.set_default_api(api)

        self.resource_path = resource_path
        self.api = api
        self.account_id = account_id
        self.business_id = business_id
        self.pageId = config['page_id']

    def listAllCampaigns(self):
        my_account = AdAccount(fbid=self.account_id)
        my_account.remote_read(fields=[Campaign.Field.id, Campaign.Field.name])
        return my_account.get_campaigns()

    def deleteAllCampaigns(self):
        my_account = AdAccount(fbid=self.account_id)
        my_account.remote_read()
        for c in my_account.get_campaigns():
            c.remote_delete()

    def readCampaignFromJson(self, jsonFile):
        campaign = Campaign(parent_id = self.account_id)
        config_file = open(jsonFile)
        config = json.load(config_file)
        config_file.close()
        for key in config.keys():
            campaign[key] = config[key]
        return campaign

    def readCampaignsFromResources(self):
        campaigns = []
        campaigns_dir = os.path.join(self.resource_path, "campaigns")
        for file in os.listdir(campaigns_dir):
            if file.endswith(".json"):
                print os.path.join(campaigns_dir, file)
                campaign = self.readCampaignFromJson(os.path.join(campaigns_dir, file))
                campaigns.append(campaign)
        return campaigns

    def createCampaign(self, campaign):
        campaign.remote_create()

    def readCampaign(self, campaign_id):
        campaign = Campaign(fbid=campaign_id)
        campaign.remote_read(fields=[Campaign.Field.id, Campaign.Field.name])
        return campaign

    def listAllAdsets(self):
        adsets = []
        campaigns = self.listAllCampaigns()
        for c in campaigns:
            adsets.extend(c.get_ad_sets([AdSet.Field.id, AdSet.Field.name]))
        return adsets

    def readAdSet(adset_id):
        ad_set = AdSet(fbid=adset_id)
        ad_set.remote_read(fields=[AdSet.Field.id])
        return ad_set

    def readAdsetFromJson(self, jsonFile):
        adset = AdSet(parent_id = self.account_id)
        config_file = open(jsonFile)
        config = json.load(config_file)
        config_file.close()
        for key in config.keys():
            adset[key] = config[key]
        return adset

    def readAdsetsFromResources(self):
        adsets = []
        adset_dir = os.path.join(self.resource_path, "adsets")
        for file in os.listdir(adset_dir):
            if file.endswith(".json"):
                print os.path.join(adset_dir, file)
                adset = self.readAdsetFromJson(os.path.join(adset_dir, file))
                adsets.append(adset)
        return adsets

    def createAdSet(self, adset, campaign_id):
        adset[AdSet.Field.campaign_id] = campaign_id
        adset.remote_create()

    def listAllAds(self):
        ads = []
        campaigns = self.listAllCampaigns()
        for c in campaigns:
            ads.extend(c.get_ads([Ad.Field.id, Ad.Field.name]))
        return ads

    def readAdFromJson(self, jsonFile):
        ad = Ad(parent_id = self.account_id)
        config_file = open(jsonFile)
        config = json.load(config_file)
        config_file.close()
        for key in config.keys():
            ad[key] = config[key]
        return ad

    def readAdsFromResources(self):
        ads = []
        ads_dir = os.path.join(self.resource_path, "ads")
        for file in os.listdir(ads_dir):
            if file.endswith(".json"):
                print os.path.join(ads_dir, file)
                adset = self.readAdFromJson(os.path.join(ads_dir, file))
                ads.append(adset)
        return ads

    def createAd(self, ad, adset_id):
        ad[Ad.Field.adset_id] = adset_id
        ad['creative']['object_story_spec']['page_id'] = self.pageId
        ad.remote_create()

    def createSplitTestAdStudy(self, name, start, end, adsets):
        adstudy = AdStudy(parent_id=self.business_id)
        adstudy[AdStudy.Field.name] = name
        adstudy[AdStudy.Field.type] = AdStudy.Type.split_test
        adstudy[AdStudy.Field.start_time] = start
        adstudy[AdStudy.Field.end_time] = end
        cells = []
        for adset in adsets:
            cell = {'name' : 'Men', 'adsets' : [adset.get_id()], 'treatment_percentage' : 1 / len(adsets) * 100}
            cells.append(cell)
        adstudy[AdStudy.Field.cells] = cells
        adstudy.remote_create()
        return adstudy