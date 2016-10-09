.timer ON
CREATE TABLE BigData5Train AS SELECT
	  a.SearchID
	, a.AdID
	, a.Position
	, a.ObjectType
	, a.HistCTR
	, b.SearchDate
	, b.IPID
	, b.UserID
	, b.IsUserLoggedOn
	, b.SearchLocationID
	, b.SearchCategoryID
	, b.SearchLocationLevel
	, b.SearchRegionID
	, b.SearchCityID
	, b.SearchCategoryLevel
	, b.SearchParentCategoryID
	, b.SearchSubcategoryID
	, c.AdLocationID
	, c.AdCategoryID
	, c.Price
	, c.AdLocationLevel
	, c.AdRegionID
	, c.AdCityID
	, c.AdCategoryLevel
	, c.AdParentCategoryID
	, c.AdSubcategoryID
	, d.UserAgentID 
	, d.UserAgentOSID
	, d.UserDeviceID 
	, d.UserAgentFamilyID
FROM trainSearchStream a 
LEFT OUTER JOIN SearchInfo_ b ON b.SearchID=a.SearchID
LEFT OUTER JOIN AdsInfo_ c ON c.AdID=a.AdID
LEFT OUTER JOIN UserInfo d ON d.UserID=b.UserID;
.timer off
