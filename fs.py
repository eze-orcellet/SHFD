
from sklearn.base import BaseEstimator, TransformerMixin
class FeatureSelection(BaseEstimator, TransformerMixin):

    def __init__(self,selected_features):
        self.selected_features=selected_features
    
    def fit(self,X,y=None):
        return self

    def transform(self, X, y=None):
        return X[self.selected_features]