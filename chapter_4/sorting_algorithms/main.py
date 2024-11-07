class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer): 
    #using hasattr to handle unexpected inputs more gracefully
    #if influencer is not None, empty or zero we execute the code, else we return None
    if hasattr(influencer, "num_bio_links") and hasattr(influencer, "num_selfies"):    
        num_bio_links = influencer.num_bio_links
        num_selfies =influencer.num_selfies 
        vanity = (num_bio_links * 5) + num_selfies
        return vanity

    return None

def vanity_sort(influencers):
    
    if influencers:
        sort = sorted(influencers, key=vanity)
        return sort
    return []

