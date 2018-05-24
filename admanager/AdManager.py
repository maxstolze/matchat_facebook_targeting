import datetime
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.adstudy import AdStudy
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.adobjects.adset import AdSet
from facebook_business import FacebookAdsApi
from facebook_business import FacebookSession
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adimage import AdImage

import json
import os

# class to manage campaigns, adsets, ads
class AdManager:

    # constructor: read in the config file from the resource folder and
    # use the parameters to init the facebook ads api
    def __init__(self, resource_path):
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
        self.account_id = config['act_id']
        self.business_id = config['business_id']
        self.pageId = config['page_id']

    def getAccount(self):
        return AdAccount(fbid=self.account_id)

    # return list of campaigns of the ad account
    def listAllCampaigns(self):
        my_account = AdAccount(fbid=self.account_id)
        my_account.remote_read(fields=[Campaign.Field.id, Campaign.Field.name])
        return my_account.get_campaigns()

    # delete all campaigns of ad account
    def deleteAllCampaigns(self):
        my_account = AdAccount(fbid=self.account_id)
        my_account.remote_read()
        for c in my_account.get_campaigns():
            c.remote_delete()

    # load a campaign from a json file (see resource folder)
    def loadCampaignFromJson(self, jsonFile):
        campaign = Campaign(parent_id = self.account_id)
        config_file = open(jsonFile)
        config = json.load(config_file)
        config_file.close()
        for key in config.keys():
            campaign[key] = config[key]
        return campaign

    # load all campaigns from the resource folder
    def loadCampaignsFromResources(self):
        campaigns = []
        campaigns_dir = os.path.join(self.resource_path, "campaigns")
        for file in os.listdir(campaigns_dir):
            if file.endswith(".json"):
                print os.path.join(campaigns_dir, file)
                campaign = self.loadCampaignFromJson(os.path.join(campaigns_dir, file))
                campaigns.append(campaign)
        return campaigns

    def createCampaign(self, campaign):
        campaign.remote_create()

    # read data from a campaign and return it
    def readCampaign(self, campaign_id):
        campaign = Campaign(fbid=campaign_id)
        campaign.remote_read(fields=[Campaign.Field.id, Campaign.Field.name])
        return campaign

    # search for targeting interests by existing category names
    # (e.g. use "sharing", "sharing economy" as category names for example)
    def searchForTargetingInterests(self, category_names):
        interests = []

        for category_name in category_names:
            params = {
                'q': category_name,
                'type': 'adinterest',
            }
            response = TargetingSearch.search(params)
            for result in response:
                if result['name'] == category_name:
                    interests.append(result)
        return interests

    # return a list of all adsets in every campaigns of the ad account
    def listAllAdsets(self):
        adsets = []
        campaigns = self.listAllCampaigns()
        for c in campaigns:
            adsets.extend(c.get_ad_sets([AdSet.Field.id, AdSet.Field.name, AdSet.Field.targeting]))
        return adsets

    # read the data of the adset and return it
    def readAdSet(adset_id):
        ad_set = AdSet(fbid=adset_id)
        ad_set.remote_read(fields=[AdSet.Field.id])
        return ad_set

    # return all fields of a specific adset insights object to analyse the results of an adset
    all_adsinsights_fields = AdsInsights.Field.__dict__.keys()
    all_adsinsights_fields.remove('__module__')
    all_adsinsights_fields.remove('__doc__')

    def readInsightsForAdset(self, adset_id, params = None, fields = all_adsinsights_fields):
        # query all fields by default
        ad_set = AdSet(fbid=adset_id)
        return ad_set.get_insights(fields=fields, params=params)

    # load an adset from a json file (see resource folder)
    def loadAdsetFromJson(self, jsonFile):
        adset = AdSet(parent_id = self.account_id)
        config_file = open(jsonFile)
        config = json.load(config_file)
        config_file.close()
        for key in config.keys():
            adset[key] = config[key]
        return adset

    # load all adsets from the resource folder
    def loadAdsetsFromResources(self):
        adsets = []
        adset_dir = os.path.join(self.resource_path, "adsets")
        for file in os.listdir(adset_dir):
            if file.endswith(".json"):
                print os.path.join(adset_dir, file)
                adset = self.loadAdsetFromJson(os.path.join(adset_dir, file))
                adsets.append(adset)
        return adsets

    # create an adset for a campaign
    def createAdSet(self, adset, campaign_id):
        adset[AdSet.Field.campaign_id] = campaign_id
        adset.remote_create()

    # return the potential reach estimate for a targeting specification (used in adsets for example)
    # NOTE: you can add the targeting option "targeting_optimization" : "expansion_all" to let facebook expand your
    # audience and reach more users than specified by interests
    def getPotentialReachForTargeting(self, targeting_spec):
        my_account = AdAccount(fbid=self.account_id)
        params = {
            'targeting_spec' : targeting_spec
        }
        reach_estimate = my_account.get_reach_estimate(params=params).get_one() # can there be mutliple reach estimates ??
        if reach_estimate['estimate_ready']:
            return reach_estimate['users']
        else:
            return None

    # return al list of all ads of the ad account
    def listAllAds(self):
        ads = []
        campaigns = self.listAllCampaigns()
        for c in campaigns:
            ads.extend(c.get_ads([Ad.Field.id, Ad.Field.name]))
        return ads

    # load an ad from a json file specification (see resource folder)
    def loadAdFromJson(self, jsonFile):
        ad = Ad(parent_id = self.account_id)
        config_file = open(jsonFile)
        config = json.load(config_file)
        config_file.close()
        for key in config.keys():
            ad[key] = config[key]
        return ad

    # load all ads from the resource folder
    def loadAdsFromResources(self):
        ads = []
        ads_dir = os.path.join(self.resource_path, "ads")
        for file in os.listdir(ads_dir):
            if file.endswith(".json"):
                adset = self.loadAdFromJson(os.path.join(ads_dir, file))
                ads.append(adset)
        return ads

    # create an ad with a image for a specific adset,
    # the image must be created before to pass the image_hash
    def createAd(self, ad, adset_id, image_hash, name=None):
        if name is not None:
            ad['name'] = name
        ad[Ad.Field.adset_id] = adset_id
        ad['creative']['object_story_spec']['page_id'] = self.pageId
        ad['creative']['object_story_spec']['link_data']['image_hash'] = image_hash
        ad.remote_create()

    # create an image (e.g. for an ad) from a resource (must be certain format, 16:9 and png is working)
    def createImageFromResources(self, image_path):
        img = AdImage(parent_id=self.account_id)
        img[AdImage.Field.filename] = image_path
        img.remote_create()
        return img

    # create all images in the resource folder
    def createAllImagesFromResources(self):
        images = []
        img_dir = os.path.join(self.resource_path, "ads", "images")
        for file in os.listdir(img_dir):
            if file.endswith(".png"):
                img_path = os.path.join(img_dir, file)
                img = self.createImageFromResources(img_path)
                images.append(img)
        return images

    # create a adstudy as a split test with a specific start and end date for a list of adsets
    # the audience should be divided between the adsets in equal sized parts
    def createSplitTestAdStudy(self, name, start_datetime, end_datetime, adsets):

        # convert datetime start and end date to UNIX millis
        epoch = datetime.datetime.utcfromtimestamp(0)
        start = int((start_datetime - epoch).total_seconds())
        end = int((end_datetime - epoch).total_seconds())

        adstudy = AdStudy(parent_id=self.business_id)
        adstudy[AdStudy.Field.name] = name
        adstudy[AdStudy.Field.type] = AdStudy.Type.split_test
        adstudy[AdStudy.Field.start_time] = start
        adstudy[AdStudy.Field.end_time] = end
        cells = []
        for adset in adsets:
            name = adset[AdSet.Field.name]  + "_" + str(adset.get_id())
            cell = {'name' : name, 'adsets' : [adset.get_id()], 'treatment_percentage' : round((1.0 / len(adsets)) * 100, 2)}
            cells.append(cell)
        adstudy[AdStudy.Field.cells] = cells
        adstudy.remote_create()
        return adstudy