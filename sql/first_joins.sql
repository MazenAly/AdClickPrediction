.timer ON
CREATE TABLE SearchInfo_ AS SELECT
	a.SearchID,
	a.SearchDate, 
	a.IPID, a.UserID, 
	a.IsUserLoggedOn, 
	a.SearchQuery, 
	a.LocationID as SearchLocationID, 
	a.CategoryID as SearchCategoryID, 
	a.SearchParams, 
	b.Level as SearchLocationLevel, 
	b.RegionID as SearchRegionID, 
	b.CityID as SearchCityID, 
	c.Level as SearchCategoryLevel, 
	c.ParentCategoryID as SearchParentCategoryID, 
	c.SubcategoryID as SearchSubcategoryID 
FROM SearchInfo a 
LEFT OUTER JOIN Location b ON a.LocationID=b.LocationID
LEFT OUTER JOIN Category c ON a.CategoryID=c.CategoryID;

CREATE INDEX index_SearchInfo_ ON SearchInfo_ (SearchID);
CREATE INDEX index_SearchInfo_UserID ON SearchInfo_ (UserID);

CREATE TABLE AdsInfo_ AS SELECT
	  a.AdID
	, a.LocationID as AdLocationID
	, a.CategoryID as AdCategoryID
	, a.Params
	, a.Price
	, a.Title
	, a.IsContext
	, b.Level as AdLocationLevel
	, b.RegionID as AdRegionID
	, b.CityID as AdCityID
	, c.Level as AdCategoryLevel
	, c.ParentCategoryID as AdParentCategoryID
	, c.SubcategoryID as AdSubcategoryID
FROM AdsInfo a 
LEFT OUTER JOIN Location b ON a.LocationID=b.LocationID
LEFT OUTER JOIN Category c ON a.CategoryID=c.CategoryID;

CREATE INDEX index_AdsInfo_ ON AdsInfo_ (AdID);
.timer off
