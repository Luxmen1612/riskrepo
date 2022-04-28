import pandas as pd

def update_cf(_id, collection):

    """
    Each transaction is to be recorded as capital call (Acquisition) or distribution (Divestment)
    Reported NAVs to be stored separately

    :param _id: subfund if in mongo db
    :param collection: collection of deals
    :return: stream of cashflows for IRR calculation or other analytics --> feed realized cfs into our db improve JCurve model
    """

    data = None

    return data
